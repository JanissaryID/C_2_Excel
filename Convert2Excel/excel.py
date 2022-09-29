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

def fill_cell(workbook, worksheet, pos_cell_start, pos_cell_end, value, align, border, background, background_color, font_color = "#000000", font_size = 14, merge_cell = False, bold = False):

    if(bold == False):
        cell_format = workbook.add_format()

        pos_merge_cell = "{0}:{1}".format(pos_cell_start, pos_cell_end)

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

        if(merge_cell):
            worksheet.merge_range(pos_merge_cell, value, cell_format)

        worksheet.write(pos_cell_start, value, cell_format)
    else:
        cell_format_bold = workbook.add_format({'bold': True})

        pos_merge_cell = "{0}:{1}".format(pos_cell_start, pos_cell_end)

        if(align == "C"):
            cell_format_bold.set_align('center')
            cell_format_bold.set_align('vcenter')
        elif(align == "R"):
            cell_format_bold.set_align('right')
            cell_format_bold.set_align('vcenter')
        elif(align == "L"):
            cell_format_bold.set_align('left')
            cell_format_bold.set_align('vcenter')

        if(border == True):
            cell_format_bold.set_border()
            cell_format_bold.set_border_color("#000000")
        else:
            cell_format_bold.set_border(0)
        
        if(background == True):
            cell_format_bold.set_pattern(1)
            cell_format_bold.set_bg_color(background_color)

        cell_format_bold.set_font_color(font_color)
        cell_format_bold.set_font_size(font_size)

        if(merge_cell):
            worksheet.merge_range(pos_merge_cell, value, cell_format_bold)

        worksheet.write(pos_cell_start, value, cell_format_bold)