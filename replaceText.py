from pathlib import Path
import openpyxl

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "Files" 
replacement_pair = {"Verify Data from Screen": "Verify Data From Screen", "ClickMenuusingjs": "Click Menu Using JS", "Select Value": "SelectValue"}  

files = list(INPUT_DIR.rglob("*.xls*"))
for file in files:
    wb = openpyxl.load_workbook(file)
    for ws in wb.worksheets:
        # Iterate over the columns and rows, search for the text and replace
        for row in ws.iter_rows():
            for cell in row:
                if cell.value in replacement_pair.keys():
                    cell.value = replacement_pair.get(cell.value)
    wb.save(file)
