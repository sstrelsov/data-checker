""" Argument Parsing Module """
import argparse as ap
from helpers import create_input_sheet_dict,create_output, spread_exists
from arg_parsing import check_input_type,INPUT_HELP,OUTPUT_HELP,SAMPLE_HELP

# Parse through command line arguments
parser = ap.ArgumentParser()
parser.add_argument('-i', type=check_input_type, nargs='+', required=True, help=INPUT_HELP)
parser.add_argument('-o', type=str, required=True, help=OUTPUT_HELP)
parser.add_argument('--sample', type=int, required=True, help=SAMPLE_HELP)
args=parser.parse_args()

# Flatten list of inputs
args.i = [sheet for sub_lst in args.i for sheet in sub_lst]

# Create dictionary of pandas dataframes and urls from input
input_dict = create_input_sheet_dict(args.i)

# Create output
create_output(input_dict,args.o,args.sample)

# TODO
# Let user specify where to save output file