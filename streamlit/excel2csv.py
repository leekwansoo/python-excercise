from pathlib import Path
import pandas as pd
import openpyxl

def convert_excel_to_csv(excel_file_path):
    excel_path = Path(excel_file_path)

    if not excel_path.exists():
        raise FileNotFoundError(f"File not found: {excel_path.resolve()}")

    if excel_path.stat().st_size == 0:
        raise ValueError(
            f"{excel_path} is empty (0 bytes). Save/export the Excel file again and retry."
        )

    # For .xlsx files, use the openpyxl engine explicitly.
    excel_file = pd.ExcelFile(excel_path, engine="openpyxl")
    csv_files = []
    for sheet in excel_file.sheet_names:
        df = pd.read_excel(excel_path, sheet_name=sheet, engine="openpyxl")
        output_csv = excel_path.with_name(f"{excel_path.stem}_{sheet}.csv")
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")
        csv_files.append(output_csv)
    return csv_files