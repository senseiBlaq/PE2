from process_workbook import process_xl
from pathlib import Path


# finds all the files with the .xlsx extension
xl_files = Path('spreadsheet').glob('*.xlsx')

for file in xl_files:
    result = process_xl(file)

print('End of program')
