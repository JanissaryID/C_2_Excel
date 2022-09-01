import re
from excel import fill_cell

DEBUG = 1

rowStart = [3, 8, 8, 11, 77, 97]
rowStartTitle = [7]
alfabetIndex = [0, 0, 0, 0]
rowIndex = [0, 0, 0, 0, 0]
rowColor = [0, 0, 0, 0, 0]

color = ["#B7DEE8", "#FFFF00", "#FFC000", "#DDD9C4", "#B7DEE8", "#FFFF00", "#FFC000", "#B7DEE8"]
color1 = ["#D9D9D9", "#F2DCDB", "#C5D9F1"]
color2 = ["#B7DEE8", "#C4D79B", "#FCD5B4", "CCC0DA", "B8CCE4"]

def processPicture(line, lineValue, workbook, worksheet):
    if(line >= 21 and line <= 23):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n', lineValue)

            for i in range(len(res) - 2):
                if(i > 0 and res[i] != ''):
                    value.append(res[i])

            for i in range(len(value)):

                cell = "{0}{1}".format(chr(ord(alfabetStart) + i), rowStart[0])
                
                if(i < 3 and rowStart[0] > 3):
                    fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=int(value[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#FFFFFF",
                    font_color="#0000FF",
                    font_size=11
                )
                else:
                    fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=int(value[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#FFFFFF",
                    font_color="#000000",
                    font_size=11
                )

                if(i == 5):
                    rowStart[0] += 1

    elif(line == 31):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n', lineValue)

            for i in range(len(res) - 2):
                if(i > 0 and res[i] != ''):
                    value.append(res[i])

            for i in range(len(value)):

                cell = "{0}{1}".format(chr(ord(alfabetStart) + i), rowStart[1])
                cellTitle = "{0}{1}".format(chr(ord(alfabetStart) + i), rowStartTitle[0])

                fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cellTitle,
                    pos_cell_end=cellTitle,
                    value=int(i),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#CCC0DA",
                    font_color="#000000",
                    font_size=14
                )
                
                fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=int(value[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#DDEBF7",
                    font_color="#FF0000",
                    font_size=11
                )

    elif(line >= 33 and line <= 35):
        if DEBUG:
            alfabetStart = 'O'
            
            value = []
            res = re.split(', |\n| ', lineValue)

            for i in range(len(res)):
                if(i > 1 and res[i] != ''):
                    value.append(res[i])

            cell = "{0}{1}".format(chr(ord(alfabetStart) + alfabetIndex[0]), rowStart[2])

            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(value[0]),
                align="C",
                border=True,
                background=True,
                background_color="#CCC0DA",
                font_color="#0000FF",
                font_size=11
            )

            alfabetIndex[0] += 1

    elif(line >= 45 and line <= 182):
        if DEBUG:
            alfabetStart = 'D'
            value = []
            res = re.split(', |\n| ', lineValue)
            
            for i in range(len(res) - 1):
                if(i > 4 and res[i] != ''):
                    value.append(res[i])

            if(len(value) == 1):
                res2 = re.split(',|\n| ', value[0])
                for i in range(len(res2)):
                    if(res2[i] != ''):
                        cell = "{0}{1}".format(chr(ord(alfabetStart) + alfabetIndex[1]), rowStart[3] + rowIndex[0])
                        if(i == 5):
                            if(res2[i][2] == "+"):
                                # print(res2[i][3])
                                if(res2[i][3] == "0"):
                                    fill_cell(
                                        workbook=workbook,
                                        worksheet=worksheet,
                                        pos_cell_start=cell,
                                        pos_cell_end=cell,
                                        value=str(0),
                                        align="C",
                                        border=True,
                                        background=True,
                                        background_color=color[rowColor[0]],
                                        font_color="#000000",
                                        font_size=11
                                    )
                                else:
                                    fill_cell(
                                        workbook=workbook,
                                        worksheet=worksheet,
                                        pos_cell_start=cell,
                                        pos_cell_end=cell,
                                        value=str("{0}{1}".format("c", res2[i][3:])),
                                        align="C",
                                        border=True,
                                        background=True,
                                        background_color=color[rowColor[0]],
                                        font_color="#000000",
                                        font_size=11
                                    )
                            else:
                                fill_cell(
                                    workbook=workbook,
                                    worksheet=worksheet,
                                    pos_cell_start=cell,
                                    pos_cell_end=cell,
                                    value=str("{0}{1}".format("w", res2[i][3:])),
                                    align="C",
                                    border=True,
                                    background=True,
                                    background_color=color[rowColor[0]],
                                    font_color="#000000",
                                    font_size=11
                                )
                        else:
                            fill_cell(
                                workbook=workbook,
                                worksheet=worksheet,
                                pos_cell_start=cell,
                                pos_cell_end=cell,
                                value=str(res2[i]),
                                align="C",
                                border=True,
                                background=True,
                                background_color=color[rowColor[0]],
                                font_color="#000000",
                                font_size=11
                            )

                        rowIndex[0] += 1
                        if(rowIndex[0] == 64):
                            rowIndex[0] = 0
                            alfabetIndex[1] += 1
                            
                rowColor[0] += 1
                if(rowColor[0] == 8):
                    rowColor[0] = 0

    elif(line >= 194 and line <= 218):
        if DEBUG:
            alfabetStart = 'F'
            value = []
            res = re.split(',|\n| ', lineValue)
            
            for i in range(len(res) - 1):
                if(i > 1 and res[i] != '' and res[i] != "0x32" and res[i] != "--"):
                    if(rowIndex[2] == 1):
                        res2 = re.split('_|\n| ', res[i])
                        if(res2[2][10:] == ""):
                            value.append(res2[2][7:])
                        else:
                            if(res2[2][10:11] == "+"):
                                if(res2[2][11:] == "0"):
                                    value.append(res2[2][11:])
                                else:
                                    value.append("{0}{1}".format("R",res2[2][11:]))
                            else:
                                value.append("{0}{1}".format("L",res2[2][11:]))
                    elif(rowIndex[2] == 0):
                        if(res[i][3:] == ""):
                            value.append(res[i])
                        else:
                            if(res[i][3:4] == "+"):
                                if(res[i][4:] == "0"):
                                    value.append(res[i][4:])
                                else:
                                    value.append("{0}{1}".format("R",res[i][4:]))
                            else:
                                value.append("{0}{1}".format("L",res[i][4:]))
            if(len(value) != 0):
                for i in range(len(value)):
                    indexRow = rowStart[4] + rowIndex[3]
                    cell = "{0}{1}".format(chr(ord(alfabetStart) + alfabetIndex[2]), indexRow)
                    # print("{0} {1} {2}".format(cell, value[i], rowColor[2]))

                    if(indexRow == 77 or indexRow == 78 or indexRow == 83 or indexRow == 86):
                        fill_cell(
                            workbook=workbook,
                            worksheet=worksheet,
                            pos_cell_start=cell,
                            pos_cell_end=cell,
                            value=value[i],
                            align="C",
                            border=True,
                            background=True,
                            background_color=color1[rowColor[2]],
                            font_color="#0000FF",
                            font_size=11
                        )
                    else:
                        fill_cell(
                            workbook=workbook,
                            worksheet=worksheet,
                            pos_cell_start=cell,
                            pos_cell_end=cell,
                            value=value[i],
                            align="C",
                            border=True,
                            background=True,
                            background_color=color1[rowColor[2]],
                            font_color="#000000",
                            font_size=11
                        )

                    rowIndex[3] += 1
                    if(rowIndex[3] == 18):
                        alfabetIndex[2] += 1
                        rowIndex[3] = 0
                        rowColor[2] = -1
                    
                    if(rowIndex[3] % 6 == 0):
                        rowColor[2] += 1

            rowIndex[2] += 1
            if(rowIndex[2] == 2):
                rowIndex[2] = 0
            
    elif(line >= 229 and line <= 310):
        # print(lineValue)
        if DEBUG:
            alfabetStart = 'D'
            value = []
            res = re.split(',|\n|{|}| ', lineValue)

            

            for i in range(len(res) - 1):
                if(i > 5 and res[i] != ''):
                    value.append(res[i])

            if(len(value) != 0):
                for i in range(len(value)):
                    indexRow = rowStart[5] + rowIndex[4]
                    alfabet = chr(ord(alfabetStart) + alfabetIndex[3])
                    cell = "{0}{1}".format(alfabet, indexRow)

                    # print("{0} {1} {2}".format(cell, value[i], rowColor[4]))

                    if(
                        indexRow >= 97 and 
                        indexRow <= 106 and 
                        (alfabet != "L" and alfabet != "M" and alfabet != "N") or
                        (alfabet == "D" and indexRow >= 108 and indexRow <= 111) or
                        (alfabet == "O" and indexRow >= 108 and indexRow <= 111) or
                        (alfabet == "D" and indexRow >= 118 and indexRow <= 120)
                        ):
                        fill_cell(
                            workbook=workbook,
                            worksheet=worksheet,
                            pos_cell_start=cell,
                            pos_cell_end=cell,
                            value=value[i],
                            align="C",
                            border=True,
                            background=True,
                            background_color=color2[rowColor[4]],
                            font_color="#0000FF",
                            font_size=11
                        )
                    else:
                        fill_cell(
                            workbook=workbook,
                            worksheet=worksheet,
                            pos_cell_start=cell,
                            pos_cell_end=cell,
                            value=value[i],
                            align="C",
                            border=True,
                            background=True,
                            background_color=color2[rowColor[4]],
                            font_color="#000000",
                            font_size=11
                        )

                    rowIndex[4] += 1

                    if(rowIndex[4] == 25):
                        rowIndex[4] = 0
                        alfabetIndex[3] += 1
                        rowColor[4] = -1

                    if(rowIndex[4] % 5 == 0):
                        rowColor[4] += 1
    
def bodyPicture(workbook, worksheet):
    tittle1 = ["SETTING_ADC_GAIN_OFFSET", "SOURCE", "R-GAIN", "G-GAIN", "B-GAIN", "R-OFFSET", "G-OFFSET", "B-OFFSET"]
    tittle2 = ["SETTING_BACKLIGHT_NONLINEAR_CURVE", "DISPLAY ->"]
    tittle3 = ["SETTING PICTURE MODE", "SOURCE ->", "DTV", "ATV", "AV1", "AV2", "AV3", "YPBPR1", "YPBPR2", "VGA", "HDMI1", "HDMI2", "HDMI3", "HDMI4", "USB", "STV"]
    tittle4 = ["WHITE BALANCE", "SOURCE -->", "ALL", "PC"]
    tittle5 = ["SETTING PICTURE NON LINEAR", "SOURCE -->", "DTV", "TV", "AV", "YPBPR", "HDMI", "HDMI2", "HDMI3", "HDMI4", "VGA", "USB", "SV", "STV"]
    tittle6 = ["PWM0_PERIOD", "INIT_PWM0_DUTY", "PWM0_DIV"]

    subtittle1 = ["VGA", "YPBPR_SD", "YPBPR_HD"]
    subtittle2 = ["VALUE"]
    subtittle3 = ["Contrast", "Brightness", "Color", "Sharpness", "Tint", "ColorTempBar", "Backlight", "Dynamic luminance"]
    subtittle4 = ["DIPE", "STANDARD", "SOFT_STANDARD", "NATURAL", "SOFT_NATURAL", "CINEMA", "ACTION", "USER"]
    subtittle5 = ["R-GAIN", "G-GAIN", "B-GAIN", "R-OFFSET", "G-OFFSET", "B-OFFSET"]
    subtittle6 = ["RGB_GAIN", "RGB_OFFSET"]
    subtittle7 = ["NORMAL", "WARM", "COOL"]
    subtittle8 = ["PAL / SD"]
    subtittle9 = ["0SD 0", "0SD 25", "OSD 50", "OSD 75", "OSD 100"]
    subtittle10 = ["BRIGHTNESS", "CONTRAST", "COLOR", "TINT", "SHARPNESS"]


    for i in range(len(tittle1)):
        alfabetStart = 'A'
        row = 2

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle1[i]),
            align="L",
            border=True,
            background=True,
            background_color="#FCD5B4",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle2)):
        
        alfabetStart = 'A'
        row = 7

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 1):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle2[i]),
            align="L",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle2[i]),
            align="L",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=14
        )
        
    for i in range(len(tittle3)):
        alfabetStart = 'A'
        row = 10

        if(i == 1):
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)
            cell2 = "{0}{1}".format(chr(ord(alfabetStart) + (int(i) + 1)), row)
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell2,
                value=str(tittle3[i]),
                align="C",
                border=True,
                background=True,
                background_color="#FDE9D9",
                font_color="#000000",
                font_size=14,
                merge_cell=True
            )
        elif(i == 0):
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(tittle3[i]),
                align="L",
                border=True,
                background=True,
                background_color="#FDE9D9",
                font_color="#000000",
                font_size=14
            )
        else:
            cell = "{0}{1}".format(chr(ord(alfabetStart) + (int(i) + 1)), row)
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(tittle3[i]),
                align="C",
                border=True,
                background=True,
                background_color="#FDE9D9",
                font_color="#000000",
                font_size=14
            )

    for i in range(len(tittle4)):
        alfabetStart = 'A'
        row = 76

        if(i == 1):
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)
            cell2 = "{0}{1}".format(chr(ord(alfabetStart) + (int(i) + 3)), row)
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell2,
                value=str(tittle4[i]),
                align="C",
                border=True,
                background=True,
                background_color="#D8E4BC",
                font_color="#000000",
                font_size=14,
                merge_cell=True
            )
        elif(i == 0):
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(tittle4[i]),
                align="L",
                border=True,
                background=True,
                background_color="#D8E4BC",
                font_color="#000000",
                font_size=14
            )
        else:
            cell = "{0}{1}".format(chr(ord(alfabetStart) + (int(i) + 3)), row)
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(tittle4[i]),
                align="C",
                border=True,
                background=True,
                background_color="#D8E4BC",
                font_color="#000000",
                font_size=14
            )

    for i in range(len(tittle5)):
        alfabetStart = 'A'
        row = 96

        if(i == 1):
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)
            cell2 = "{0}{1}".format(chr(ord(alfabetStart) + (int(i) + 1)), row)
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell2,
                value=str(tittle5[i]),
                align="C",
                border=True,
                background=True,
                background_color="#538DD5",
                font_color="#000000",
                font_size=14,
                merge_cell=True
            )
        elif(i == 0):
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(tittle5[i]),
                align="L",
                border=True,
                background=True,
                background_color="#0099CC",
                font_color="#000000",
                font_size=14
            )
        else:
            cell = "{0}{1}".format(chr(ord(alfabetStart) + (int(i) + 1)), row)
            if(cell != "L96" and cell != "M96" and cell != "N96"):
                fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=str(tittle5[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#538DD5",
                    font_color="#0000FF",
                    font_size=14
                )
            else:
                fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=str(tittle5[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#538DD5",
                    font_color="#000000",
                    font_size=14
                )

    for i in range(len(tittle6)):

        alfabetStart = 'O'
        row = 7

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle6[i]),
            align="L",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=11
        )

    for i in range(len(subtittle1)):
        alfabetStart = 'B'
        row = 3

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle1[i]),
            align="L",
            border=True,
            background=True,
            background_color="#B7DEE8",
            font_color="#000000",
            font_size=11
        )

    for i in range(len(subtittle2)):
        alfabetStart = 'B'
        row = 8

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle2[i]),
            align="L",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=14
        )

    row1 = 11
    rowColor = 0

    for j in range(len(subtittle4)):
        alfabetStart1 = 'B'

        cell1 = "{0}{1}".format(chr(ord(alfabetStart1)), row1)
        cell2 = "{0}{1}".format(chr(ord(alfabetStart1)), row1 + 7)

        fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell1,
                pos_cell_end=cell2,
                value=str(subtittle4[j]),
                align="L",
                border=True,
                background=True,
                background_color=color[rowColor],
                font_color="#000000",
                font_size=11,
                merge_cell=True
            )

        for i in range(len(subtittle3)):
            alfabetStart = 'C'
            
            cell = "{0}{1}".format(chr(ord(alfabetStart)), row1)
            
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(subtittle3[i]),
                align="L",
                border=True,
                background=True,
                background_color=color[rowColor],
                font_color="#000000",
                font_size=11
            )

            # print(cell2)

            row1 += 1
        rowColor += 1
        if(rowColor == 9):
            rowColor = 0

    row2 = 77
    row3 = 0
    rowColor2 = 0

    for i in range(len(subtittle5)):
        alfabetStart = 'E'
        
        cell = "{0}{1} {2}".format(chr(ord(alfabetStart)), row2, row3)

        print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle5[i]),
            align="L",
            border=True,
            background=True,
            background_color=color1[rowColor2],
            font_color="#000000",
            font_size=11
        )
        if(row3 == 2):
            row3 = -1

        # if(i == 0 or i == 3 ):
        #     alfabetStart1 = 'D'

        #     cell1 = "{0}{1}".format(chr(ord(alfabetStart1)), row2)
        #     cell2 = "{0}{1}".format(chr(ord(alfabetStart1)), row2 + 2)

        #     print("{0} {1}".format(cell1, "Start"))
        #     print("{0} {1}".format(cell2, "End"))

        #     fill_cell(
        #             workbook=workbook,
        #             worksheet=worksheet,
        #             pos_cell_start=cell1,
        #             pos_cell_end=cell2,
        #             value=str(subtittle6[j]),
        #             align="L",
        #             border=True,
        #             background=True,
        #             background_color=color1[rowColor2],
        #             font_color="#000000",
        #             font_size=11,
        #             merge_cell=True
        #         )

        row2 += 1
        row3 += 1
    rowColor2 += 1
    if(rowColor2 == 3):
        rowColor2 = 0

    # for j in range(len(subtittle6)):
        

        
        
        







