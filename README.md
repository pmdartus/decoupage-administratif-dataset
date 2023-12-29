# Dataset consolidé du découpage administratif

Dataset des communes, départements et région de France. L'ensemble des datasets se trouvent sur la branch [`dataset`](/pmdartus/decoupage-administratif-dataset/tree/dataset):

**[`regions.csv`](/pmdartus/decoupage-administratif-dataset/tree/dataset/regions.csv):**

| Colonne | Type   | Description               |
| ------- | ------ | ------------------------- |
| `nom`   | string | Nom de la région          |
| `code`  | string | Code (INSEE) de la région |

**[`departements.csv`](/pmdartus/decoupage-administratif-dataset/tree/dataset/departements.csv):**

| Colonne       | Type   | Description                 |
| ------------- | ------ | --------------------------- |
| `nom`         | string | Nom de la département       |
| `code`        | string | Code (INSEE) du département |
| `region_nom`  | string | Nom de la région            |
| `region_code` | string | Code (INSEE) de la région   |

**[`communes.csv`](/pmdartus/decoupage-administratif-dataset/tree/dataset/communes.csv):**

| Colonne            | Type   | Description                                              |
| ------------------ | ------ | -------------------------------------------------------- |
| `nom`              | string | Nom de la commune                                        |
| `code`             | string | Code (INSEE) de la commune                               |
| `code_postaux`     | string | Liste des code postaux associés, séparés par une virgule |
| `longitude`        | float  | Longitude du centre de la commune                        |
| `lalitude`         | float  | Longitude du centre de la commune                        |
| `departement_nom`  | string | Nom de la département                                    |
| `departement_code` | string | Code (INSEE) du département                              |
| `region_nom`       | string | Nom de la région                                         |
| `region_code`      | string | Code (INSEE) de la région                                |

**[`communes-expanded.csv`](/pmdartus/decoupage-administratif-dataset/tree/dataset/communes-expanded.csv):**

| Colonne            | Type   | Description                       |
| ------------------ | ------ | --------------------------------- |
| `nom`              | string | Nom de la commune                 |
| `code`             | string | Code (INSEE) de la commune        |
| `code_postal`      | string | Code postal associé               |
| `longitude`        | float  | Longitude du centre de la commune |
| `lalitude`         | float  | Longitude du centre de la commune |
| `departement_nom`  | string | Nom de la département             |
| `departement_code` | string | Code (INSEE) du département       |
| `region_nom`       | string | Nom de la région                  |
| `region_code`      | string | Code (INSEE) de la région         |

## Détails

- Fréquence de mise à jour: Mensuelle
- Licence : [Licence Ouverte / Open Licence](https://www.etalab.gouv.fr/licence-ouverte-open-licence/)

## Crédits

- [API Découpage administratif - geo.api.gouv.fr](https://geo.api.gouv.fr/decoupage-administratif)
