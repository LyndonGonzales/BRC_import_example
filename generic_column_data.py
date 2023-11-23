import pandas as pd

column_widths = [10, 15, 20, 12]  # Example column widths
column_names = ['Column1', 'Column2', 'Column3', 'Column4']  # Example column names

file_path = 'path/to/your/file.txt'
df = pd.read_fwf(file_path, widths=column_widths, names=column_names)
