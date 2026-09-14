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


if __name__ == "__main__":
    from pathlib import Path
    from src.helpers.excel_reader import read_cal_export, extract_metadata

    test_file = (
        Path(__file__).resolve().parents[2]
        / "sample_data"
        / "Vehicle_A.xlsx"
    )

    calibration_data = read_cal_export(test_file)
    metadata = extract_metadata(test_file)

    transformed_data = enrich_calibration_data(
        calibration_data,
        metadata,
    )

    print(transformed_data.head())
    print()
    print(f"Rows transformed: {len(transformed_data)}")
    print()
    print(transformed_data.columns.tolist())