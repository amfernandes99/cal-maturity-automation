from pathlib import Path
import pandas as pd

# Writing the master workbook to an Excel file.
def write_master_workbook(
    master_data: pd.DataFrame,
    output_path: Path,
) -> None:
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        master_data.to_excel(
            writer,
            sheet_name="Master",
            index=False,
        )

    print(f"Master workbook created: {output_path}")