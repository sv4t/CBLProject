# Crime and Housing Statistics Analysis

This project analyses crime data and housing price statistics within London electoral wards, focusing on crime patterns and property values across different areas.

## Getting Started

### Download Required Data

To use this project, **you must download the crime data** from the [UK Police Data website](https://data.police.uk/data/).
Please ensure you download crime data **only for the following forces**:

* **Metropolitan Police Service**
* **City of London Police** (optional)

> **Important:** After downloading the crime data, place the entire folder inside the cloned repository and **rename the folder to `CrimeData`**.
> The `.gitignore` file is configured to exclude this folder (because it can be quite large), so it will not be committed to the repository.

### Setting File Paths

Before running the project, you will need to specify correct file paths in the `main` script. Below is a guide for setting each path:

| Variable Name           | Description                                                 | Required Path Example                                |
| ----------------------- | ----------------------------------------------------------- | ---------------------------------------------------- |
| `crime_df`              | Path to the **crime data CSV** for a specific month         | `/CrimeData/2022-04/2022-04-metropolitan-street.csv` |
| `lookup_df`             | Path to the **ward lookup file** included in the repository | `LSOA_to_Electoral_Ward.csv`                         |
| `median_home_prices_df` | Path to the **home prices file** included in the repository | `MedianHomePriceByWard.csv`                          |

You will need to edit these paths directly in your `main` script to reflect the correct locations.

### Running the Project

Once the data is downloaded and the paths have been correctly set, simply run the script using Python:

```
python main.py
```

### Output

After successful execution, the script will generate **two new CSV files** containing statistical summaries:

* `ward_crime_statistics.csv` — General crime statistics per electoral ward
* `ward_burglary_statistics.csv` — Burglary-specific statistics per electoral ward

These files will be saved in the project directory.

## Notes

* Ensure all dependencies listed in `requirements.txt` (if applicable) are installed.
* This project is focused on London areas; crime data from other police forces is not supported.

