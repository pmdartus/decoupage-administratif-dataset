from typing import Any, List
from venv import logger
import requests

GOE_API_BASE_URL = "https://geo.api.gouv.fr"


def get_regions() -> List[Any]:
    """Retrieves the list of regions from the GOE API"""

    url = f"{GOE_API_BASE_URL}/regions"
    logger.info(f"Fetching regions from {url}")

    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def get_departements(region_code: str, fields: List[str] = []) -> List[Any]:
    """Retrieves the list of departements in a given region from the GOE API"""

    url = f"{GOE_API_BASE_URL}/regions/{region_code}/departements"
    params = {"fields": ",".join(fields)} if fields else {}

    logger.info(f"Fetching departements for region {region_code} from {url}")

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_coummunes(departement_code: str, fields: List[str] = []) -> List[Any]:
    """Retrieves the list of communes in a given departement from the GOE API"""

    url = f"{GOE_API_BASE_URL}/departements/{departement_code}/communes"
    params = {"fields": ",".join(fields)} if fields else {}

    logger.info(f"Fetching communes for departement from {departement_code} from {url}")

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()
