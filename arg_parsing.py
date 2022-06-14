""" Argument parsing module """
import argparse
from os.path import exists
from helpers import spread_exists

# Help statements
INPUT_HELP = "input flag. names of spreadsheets to check,\
              both as strings or .txt files containing Google Sheet names."
OUTPUT_HELP = "output flag. name of Google Sheet to write to."
SAMPLE_HELP = "number of random samples to take from each input sheet to display in output."

def check_input_type(user_input):
    """Checks whether the -i inputs spreadsheets are files or spreadsheet names"""
    if exists(user_input):
        with open(user_input,'r', encoding='utf-8') as input_file:
            sheet_lst = [line.split(',') for line in input_file][0]
            print(f"SHEETS ADDED FROM FILE: {user_input}")
            for sheet in sheet_lst:
                print(f"    \u2713 {sheet}")
        return sheet_lst
    if not spread_exists(user_input):
        raise argparse.ArgumentTypeError(f"No such input file or Google Sheet named '{user_input}'")
    print("SHEET ADDED BY NAME: ")
    print(f"    \u2713 {user_input}")
    return [user_input]
