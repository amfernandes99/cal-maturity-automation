from pathlib import Path
import pandas as pd

from src.helpers.excel_reader import read_cal_export, extract_metadata
from src.helpers.transformer import enrich_calibration_data
from src.helpers.writer import write_master_workbook
from src.helpers.db_writer import push_to_bigquery

# Defining paths for sample data and output files.
SAMPLE_DATA_DIR = Path(__file__).resolve().parents[1] / "sample_data"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "output"
OUTPUT_FILE = OUTPUT_DIR / "CAL_Master_Tracker.xlsx"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def process_all_exports(folder: Path) -> pd.DataFrame:
    transformed_files = []

    # Combining all calibration export files in the specified folder into a single DataFrame after transforming them to match the master sheet format.
    for file_path in folder.glob("*.xlsx"):
        calibration_data = read_cal_export(file_path)
        metadata = extract_metadata(file_path)

        transformed_data = enrich_calibration_data(
            calibration_data,
            metadata,
        )

        transformed_files.append(transformed_data)

    # Stacking all transformed DataFrames into a single DataFrame to create the master sheet.
    master_data = pd.concat(
        transformed_files,
        ignore_index=True,
    )

    return master_data

# Runs the process_all_exports function on the sample data.
if __name__ == "__main__":
    master_data = process_all_exports(SAMPLE_DATA_DIR)

    write_master_workbook(master_data, OUTPUT_FILE)

    print(master_data.head())
    print()
    print(f"Total rows: {len(master_data)}")
    print()
    print(master_data["Variant"].value_counts())

# Pushes the master data to BigQuery 
    push_to_bigquery(master_data)