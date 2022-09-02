from excel import *
from openfile import *

def setup_width(worksheet):
    width_row_sound(worksheet=worksheet)
    # width_row_picture(worksheet=worksheet)

def main():
    worksheet, workbook = create_excel()
    setup_width(worksheet=worksheet)

    read_c_file(workbook=workbook, worksheet=worksheet)

    workbook.close()

if __name__ == "__main__":
    main()
    # read_c_file()
    # processCoba()