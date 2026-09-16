import pandas as pd

from src.helpers.constants import MASTER_COLUMNS

# Note - A production version could validate required source columns before transformation, and raise a clear error if expected fields are missing.

# Transforming the calibration data by enriching it with metadata and reordering the columns to match the master sheet format.
def enrich_calibration_data(
    calibration_data: pd.DataFrame,
    metadata: dict,
) -> pd.DataFrame:
    df = calibration_data.copy()

    df["CAL_ID"] = metadata["CAL_ID"]
    df["Description"] = metadata["Description"]
    df["Created"] = pd.to_datetime(metadata["Created"]).date()
    df["CAL_Lead"] = metadata["CAL_Lead"]
    df["Variant"] = metadata["Variant"]
    df["Software"] = metadata["Software"]

    df["Function Version"] = df["Function Version"].astype(str)

    df = df[MASTER_COLUMNS]

    return df
