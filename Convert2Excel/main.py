from excel import *
from openfile import *

def setup_width(worksheet):
    # width_row_sound(worksheet=worksheet)
    width_row_picture(worksheet=worksheet)

def main():
    worksheet, workbook = create_excel()
    setup_width(worksheet=worksheet)

    read_c_file(workbook=workbook, worksheet=worksheet)

    # fill_cell(
    #     workbook=workbook,
    #     worksheet=worksheet,
    #     pos_cell="A1",
    #     value="Hello World",
    #     align="C",
    #     border=True,
    #     background=True,
    #     background_color="#FF00FF",
    #     font_color="#FF0000",
    #     font_size=11
    # )

    # fill_cell(
    #     workbook=workbook,
    #     worksheet=worksheet,
    #     pos_cell="B3",
    #     value="Hello World",
    #     align="C",
    #     border=True,
    #     background=True,
    #     background_color="#FF00FF",
    #     font_color="#FF0000",
    #     font_size=11
    # )

    workbook.close()

if __name__ == "__main__":
    main()
    # read_c_file()
    # processCoba()