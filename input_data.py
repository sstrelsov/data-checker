import gspread

def get_input_data(cl_args,gc):
    if len(cl_args) > 1:
        sheet_lst = []
        for arg in cl_args[1:]:
            sheet_lst.append(get_sheets_from_arg(arg,gc))
        sheet_lst = [sheet for sub_lst in sheet_lst for sheet in sub_lst]
        return sheet_lst
    # User didn't enter any command line arguments
    print("USAGE: python3 check.py <file_name_or_sheet_name> <file_name_or_sheet_name> ...")
    exit()
    
def get_sheets_from_arg(arg,gc):
    try:
        f = open(arg,'r')
    # User didn't enter a valid file name
    except FileNotFoundError as fne:
        try:
            gc.open(arg)
        # User didn't enter a valid spreadsheet name either
        except gspread.exceptions.SpreadsheetNotFound:
            print(f"[gspread error] No such Google Sheet named '{arg}'")
            print(fne)
            exit()
        # User entered valid spreadsheet name. Return the name of the spreadsheet
        else:
            sheet_lst = [arg]
            print("SHEET ADDED: ")
            print(f"    \u2713 {arg}")
            return sheet_lst
    # User entered valid file of spreadsheet name(s). Return the name of the spreadsheet(s)
    else:
        sheet_lst = [line.split(',') for line in f][0]
        print(f"SHEETS ADDED FROM FILE: {arg}")
        for sheet in sheet_lst:
            print(f"    \u2713 {sheet}")
        f.close()
        return sheet_lst