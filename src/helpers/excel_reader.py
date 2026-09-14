from pathlib import Path
import pandas as pd

from src.helpers.constants import HEADER_ROW

# Extracting the calibration data from the calibration export Excel file.
def read_cal_export(file_path: Path) -> pd.DataFrame:
    df = pd.read_excel(
        file_path,
        header=HEADER_ROW - 1,
    )

    return df

if __name__ == "__main__":
    test_file = Path(__file__).resolve().parents[2] / "sample_data" / "Vehicle_A.xlsx"

    df = read_cal_export(test_file)

    print(df.head())
    print()
    print(f"Rows loaded: {len(df)}")

# Extracting the metadata from the calibration export Excel file.
def extract_metadata(file_path: Path) -> dict:
    metadata_df = pd.read_excel(
        file_path,
        header=None,
        nrows=7,
    )

    metadata = {
        "CAL_ID": metadata_df.iloc[0, 1],
        "Description": metadata_df.iloc[1, 1],
        "Created": metadata_df.iloc[2, 1],
        "CAL_Lead": metadata_df.iloc[3, 1],
        "Variant": metadata_df.iloc[5, 1],
        "Software": metadata_df.iloc[6, 1],
    }

    return metadata