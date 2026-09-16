# TEST 1 - Test file to validate the functionality of the enrich_calibration_data function in transformer.py.

import pandas as pd

from src.helpers.transformer import enrich_calibration_data


def test_enrich_calibration_data_adds_metadata():
    calibration_data = pd.DataFrame(
        {
            "Name": ["Parameter_00001"],
            "Function Name": ["BrakeControl"],
            "Function Version": ["1.0"],
            "Owner": ["Engineer_01"],
            "Deputy": ["Engineer_06"],
            "Score": [20],
        }
    )

    metadata = {
        "CAL_ID": "CAL_DEMO_001",
        "Description": "Synthetic test dataset",
        "Created": "2026-09-10",
        "CAL_Lead": "Engineer_01",
        "Variant": "Vehicle_A",
        "Software": "SW_01.0",
    }

    result = enrich_calibration_data(
        calibration_data,
        metadata,
    )
    assert result.loc[0, "CAL_ID"] == "CAL_DEMO_001"
    assert result.loc[0, "Variant"] == "Vehicle_A"
    assert result.loc[0, "Software"] == "SW_01.0"


# TEST 2 - Testing to see if the "Function Version" column has been correctly converted to string type.

def test_enrich_calibration_data_returns_master_columns():
    calibration_data = pd.DataFrame(
        {
            "Name": ["Parameter_00001"],
            "Function Name": ["BrakeControl"],
            "Function Version": ["1.0"],
            "Owner": ["Engineer_01"],
            "Deputy": ["Engineer_06"],
            "Score": [20],
        }
    )

    metadata = {
        "CAL_ID": "CAL_DEMO_001",
        "Description": "Synthetic test dataset",
        "Created": "2026-09-10",
        "CAL_Lead": "Engineer_01",
        "Variant": "Vehicle_A",
        "Software": "SW_01.0",
    }

    result = enrich_calibration_data(
        calibration_data,
        metadata,
    )

    expected_columns = [
        "Name",
        "Function Name",
        "Function Version",
        "Owner",
        "Deputy",
        "Score",
        "CAL_ID",
        "Description",
        "Created",
        "CAL_Lead",
        "Variant",
        "Software",
    ]

    assert result.columns.tolist() == expected_columns