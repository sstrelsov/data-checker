import gspread
import argparse
from os.path import exists

# Authenticate Google Sheets
gc = gspread.oauth()

# Help statements
input_help = "input flag. names of spreadsheets to check, both as strings or .txt files containing Google Sheet names."
output_help = "output flag. name of Google Sheet to write to."
sample_help = "number of random samples to take from each input sheet to display in output."

def check_input_type(a):
    if exists(a):
        with open(a,'r') as f:
            sheet_lst = [line.split(',') for line in f][0]
            print(f"SHEETS ADDED FROM FILE: {a}")
            for sheet in sheet_lst:
                print(f"    \u2713 {sheet}")
        return sheet_lst
    if not check_sheet(a):
        raise argparse.ArgumentTypeError(f"No such input file or Google Sheet named '{a}'")
    print("SHEET ADDED BY NAME: ")
    print(f"    \u2713 {a}")
    return [a]

def check_output_type(a):
    if not check_sheet(a):
        raise argparse.ArgumentTypeError(f"No such Google Sheet named '{a}'")
    return

def check_sheet(a):
    # User didn't enter a valid file name
    try:
        gc.open(a)
    # User didn't enter a valid spreadsheet name either
    except gspread.exceptions.SpreadsheetNotFound:
        return False
    else:
        return True