""" Argument parsing module """
import argparse
from os.path import exists
from helpers import spread_exists

# Help statements
INPUT_HELP = "input flag. names of spreadsheets to check,\
              both as strings or .txt files containing Google Sheet names."
OUTPUT_HELP = "output flag. name of Google Sheet to write to."
SAMPLE_HELP = "number of random samples to take from each input sheet to display in output."

def check_input_type(a):
    """Checks whether the -i inputs spreadsheets are spreadsheet names or files containing spreadsheet names"""
    if exists(a):
        with open(a,'r') as f:
            sheet_lst = [line.split(',') for line in f][0]
            print(f"SHEETS ADDED FROM FILE: {a}")
            for sheet in sheet_lst:
                print(f"    \u2713 {sheet}")
        return sheet_lst
    if not spread_exists(a):
        raise argparse.ArgumentTypeError(f"No such input file or Google Sheet named '{a}'")
    print("SHEET ADDED BY NAME: ")
    print(f"    \u2713 {a}")
    return [a]