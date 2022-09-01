import xlsxwriter
from constVariable import *

def create_excel():
    workbook = xlsxwriter.Workbook('demo.xlsx')
    worksheet = workbook.add_worksheet()

    return worksheet, workbook

def width_row_sound(worksheet):
    for x in range(17):
        # print(x)
        if(x >= 2 and x <= 9):
            worksheet.set_column("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)), WIDTH_SOUND[2])
        elif(x >= 10 and x <= 14):
            worksheet.set_column("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)), WIDTH_SOUND[3])
        elif(x == 0):
            worksheet.set_column("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)), WIDTH_SOUND[0])
        elif(x == 1):
            worksheet.set_column("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)), WIDTH_SOUND[1])
        elif(x == 15):
            worksheet.set_column("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)), WIDTH_SOUND[4])
        elif(x == 16):
            worksheet.set_column("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)), WIDTH_SOUND[5])

def width_row_picture(worksheet):
    for x in range(17):
        # print(x)
        if(x >= 8 and x <= 11):
            worksheet.set_column("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)), WIDTH_PICTURE[8])
        elif(x <= 7):
            worksheet.set_column("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)), WIDTH_PICTURE[x])
        elif(x >= 12):
            worksheet.set_column("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)), WIDTH_PICTURE[x-3])
            # print("{0}:{1}".format(chr(ord(START_CHAR) + x),chr(ord(START_CHAR) + x)))

def fill_cell(workbook, worksheet, pos_cell, value, align, border, background, background_color, font_color = "#000000", font_size = 14):
    cell_format = workbook.add_format()

    if(align == "C"):
        cell_format.set_align('center')
        cell_format.set_align('vcenter')
    elif(align == "R"):
        cell_format.set_align('right')
        cell_format.set_align('vcenter')
    elif(align == "L"):
        cell_format.set_align('left')
        cell_format.set_align('vcenter')

    if(border == True):
        cell_format.set_border()
        cell_format.set_border_color("#000000")
    else:
        cell_format.set_border(0)
    
    if(background == True):
        cell_format.set_pattern(1)
        cell_format.set_bg_color(background_color)

    cell_format.set_font_color(font_color)
    cell_format.set_font_size(font_size)

    worksheet.write(pos_cell, value, cell_format)