from gspread_pandas import Spread
from gspread_formatting import *
from helpers import create_input_sheet_dict, create_output
import argparse
from arg_parsing import *

# Parse through command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', type=check_input_type, nargs='+', required=True, help=input_help)
parser.add_argument('-o', type=str, required=True, help=output_help)
parser.add_argument('--sample', type=int, required=True, help=sample_help)
args=parser.parse_args()

# Flatten list of inputs
args.i = [sheet for sub_lst in args.i for sheet in sub_lst]

# TODO
## Create new spreadsheet from output string if it doesn't exist
## Open output spreadsheet if it does exist (do all of these things in the helper functions)
output_spreadsheet_name = Spread(args.o)
output_gspread = gc.open(output_spreadsheet_name)

# Clean input and generate output
input_dict = create_input_sheet_dict(args.i)
create_output(input_dict,args.o,args.sample)