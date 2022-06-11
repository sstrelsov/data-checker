import sys
from gspread_pandas import Spread, Client
import gspread
from gspread_formatting import *
from helpers import create_input_sheet_dict, create_output
from input_data import get_input_data

# Authenticate Google Sheets
gc = gspread.oauth()

# Check for command line arguments
input_spreadsheet_names = get_input_data(sys.argv, gc)

# Get input and output spreadsheet names, open output spreadsheet
output_sheet_name = input("Enter name of output spreadsheet: ")
entries_per_sample = int(input("Enter the number of samples to be taken per input sheet: "))
num_samples = int(input("Enter the number of times to randomly select the number of samples: "))

output_spreadsheet_name = Spread(output_sheet_name)
output_gspread = gc.open(output_sheet_name)

clean_input_data = create_input_sheet_dict(input_spreadsheet_names)
create_output(clean_input_data,output_sheet_name,entries_per_sample,num_samples)