from pathlib import Path
import random
import pandas as pd

# Defining the location to save the generated sample data
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "sample_data"
OUTPUT_DIR.mkdir(exist_ok=True)


FUNCTIONS = [
    "BrakeControl",
    "SteeringControl",
    "Powertrain",
    "ThermalManagement",
    "VehicleDynamics",
    "Diagnostics",
]

OWNERS = [
    "Engineer_01",
    "Engineer_02",
    "Engineer_03",
    "Engineer_04",
    "Engineer_05",
]

DEPUTIES = [
    "None",
    "Engineer_06",
    "Engineer_07",
    "Engineer_08",
]

# This function generates a DataFrame containing calibration data with random values for each parameter.
def build_calibration_rows(num_rows: int) -> pd.DataFrame:
    rows = []

    for i in range(1, num_rows + 1):
        rows.append(
            {
                "Name": f"Parameter_{i:05d}",
                "Function Name": random.choice(FUNCTIONS),
                "Function Version": f"{random.randint(1, 5)}.{random.randint(0, 9)}",
                "Owner": random.choice(OWNERS),
                "Deputy": random.choice(DEPUTIES),
                "Score": random.choice([0, 5, 10, 15, 20, 25]),
            }
        )

    return pd.DataFrame(rows)

# This function creates an Excel file containing calibration data and metadata, with the specified requirements.
def create_cal_export(
    filename: str,
    cal_id: str,
    description: str,
    variant: str,
    software: str,
    num_rows: int,
):
    calibration_data = build_calibration_rows(num_rows)

# Defining the output path for the generated Excel file
    output_path = OUTPUT_DIR / filename

    metadata = [
        ["Name", cal_id],
        ["Description", description],
        ["Created", pd.Timestamp.today().strftime("%Y-%m-%d")],
        ["Owner", "Engineer_01"],
        ["Project", "Project_Alpha"],
        ["Variant", variant],
        ["Software", software],
    ]

# Coverting metadata to a DataFrame for easier writing to Excel
    metadata_df = pd.DataFrame(metadata)

# Creating an Excel writer to write the data to the same Excel file
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        metadata_df.to_excel(
            writer,
            index=False,
            header=False,
            startrow=0,
        )

# Writing the calibration data to the Excel file
        calibration_data.to_excel(
            writer,
            index=False,
            startrow=8,
        )

    print(f"Created: {output_path}")

# Calling the create_cal_export function to generate sample calibration data for different vehicles.
if __name__ == "__main__":
    create_cal_export(
        filename="Vehicle_A.xlsx",
        cal_id="CAL_DEMO_001",
        description="Synthetic calibration dataset for Vehicle A",
        variant="Vehicle_A",
        software="SW_01.0",
        num_rows=500,
    )

    create_cal_export(
        filename="Vehicle_B.xlsx",
        cal_id="CAL_DEMO_002",
        description="Synthetic calibration dataset for Vehicle B",
        variant="Vehicle_B",
        software="SW_02.0",
        num_rows=500,
    )

    create_cal_export(
        filename="Vehicle_C.xlsx",
        cal_id="CAL_DEMO_003",
        description="Synthetic calibration dataset for Vehicle C",
        variant="Vehicle_C",
        software="SW_03.0",
        num_rows=500,
    )