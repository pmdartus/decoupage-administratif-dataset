import argparse
import csv
import logging
from pathlib import Path
from typing import Any, List

import pandas as pd

from api import get_coummunes, get_departements, get_regions

JSON_SERIALIZATION_OPTIONS = {
    "orient": "records",
}
CSV_SERIALIZATION_OPTIONS = {
    "index": False,
    "quoting": csv.QUOTE_NONNUMERIC,
}


def run(args: argparse.Namespace) -> None:
    # Get data from API
    region_list = get_regions()
    departement_list = []
    commune_list = []

    for region in region_list:
        departements = get_departements(
            region["code"], fields=["nom", "code", "region"]
        )
        departement_list += departements

        for departement in departements:
            communes = get_coummunes(
                departement["code"],
                fields=[
                    "nom",
                    "code",
                    "departement",
                    "region",
                    "centre",
                    "codesPostaux",
                ],
            )
            commune_list += communes

    process_regions(region_list, args)
    process_departements(departement_list, args)
    process_communes(commune_list, args)


def process_regions(regions: List[Any], args: argparse.Namespace):
    df = pd.DataFrame(regions)

    df.to_csv(f"{args.output}/regions.csv", **CSV_SERIALIZATION_OPTIONS)
    df.to_json(f"{args.output}/regions.json", **JSON_SERIALIZATION_OPTIONS)


def process_departements(departements: List[Any], args: argparse.Namespace):
    df = pd.DataFrame(departements)

    # Save original dataframe to json
    df.to_json(f"{args.output}/departements.json", **JSON_SERIALIZATION_OPTIONS)

    # Flatten columns and save to csv
    df["region_nom"] = df["region"].apply(lambda x: x["nom"])
    df["region_code"] = df["region"].apply(lambda x: x["code"])
    df.drop("region", axis=1, inplace=True)

    df.to_csv(f"{args.output}/departements.csv", **CSV_SERIALIZATION_OPTIONS)


def process_communes(communes: List[Any], args: argparse.Namespace):
    df = pd.DataFrame(communes)

    # Save original dataframe to json
    json_df = df.copy()
    json_df.to_json(f"{args.output}/communes.json", **JSON_SERIALIZATION_OPTIONS)

    # Expand codesPostaux column into multiple rows and save to json
    json_df_expanded = json_df.explode("codesPostaux").rename(
        {"codesPostaux": "codePostal"}, axis=1
    )
    json_df_expanded.to_json(
        f"{args.output}/communes-expanded.json", **JSON_SERIALIZATION_OPTIONS
    )

    # Flatten columns
    df["region_nom"] = df["region"].apply(lambda x: x["nom"])
    df["region_code"] = df["region"].apply(lambda x: x["code"])
    df.drop("region", axis=1, inplace=True)

    df["department_nom"] = df["departement"].apply(lambda x: x["nom"])
    df["departement_code"] = df["departement"].apply(lambda x: x["code"])
    df.drop("departement", axis=1, inplace=True)

    df["longitude"] = df["centre"].apply(lambda x: x["coordinates"][0])
    df["latitude"] = df["centre"].apply(lambda x: x["coordinates"][1])
    df.drop("centre", axis=1, inplace=True)

    df.rename({"codesPostaux": "codes_postaux"}, axis=1, inplace=True)

    # Save to csv with additional additional post-processing on the codesPostaux column
    csv_df = df.copy()
    csv_df["codes_postaux"] = csv_df["codes_postaux"].apply(lambda x: ",".join(x))
    csv_df.to_csv(f"{args.output}/communes.csv", **CSV_SERIALIZATION_OPTIONS)

    # Expand codesPostaux column into multiple rows and save to csv and json
    csv_df_expanded = df.explode("codes_postaux").rename(
        {"codes_postaux": "code_postal"}, axis=1
    )
    csv_df_expanded.to_csv(
        f"{args.output}/communes-expanded.csv", **CSV_SERIALIZATION_OPTIONS
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Build decoupage administrative dataset"
    )
    parser.add_argument(
        "--output", "-o", help="Output folder name", default="data", type=str
    )
    parser.add_argument(
        "--log-level", "-l", help="Set log level", default="warning", type=str
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level.upper())
    Path(args.output).mkdir(parents=True, exist_ok=True)

    run(args)
