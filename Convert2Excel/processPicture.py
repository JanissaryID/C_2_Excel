import re
from excel import fill_cell

DEBUG = 1

rowStart = [3, 8, 8, 11, 77]
rowStartTitle = [7]
alfabetIndex = [0, 0, 0]
rowIndex = [0, 0, 0, 0]
rowColor = [0, 0]

color = ["#B7DEE8", "#FFFF00", "#FFC000", "#DDD9C4", "#B7DEE8", "#FFFF00", "#FFC000", "#B7DEE8"]
color1 = ["#D9D9D9", "#F2DCDB", "#C5D9F1"]

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
                    pos_cell=cell,
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
                    pos_cell=cell,
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
                    pos_cell=cellTitle,
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
                    pos_cell=cell,
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
                pos_cell=cell,
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
                                        pos_cell=cell,
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
                                        pos_cell=cell,
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
                                    pos_cell=cell,
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
                                pos_cell=cell,
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
                    cell = "{0}{1}".format(chr(ord(alfabetStart) + alfabetIndex[2]), rowStart[4] + rowIndex[3])
                    print("{0} {1}".format(cell, value[i]))

                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell=cell,
                        value=value[i],
                        align="C",
                        border=True,
                        background=True,
                        background_color="#00FF00",
                        font_color="#000000",
                        font_size=11
                    )

                    rowIndex[3] += 1
                    if(rowIndex[3] == 18):
                        alfabetIndex[2] += 1
                        rowIndex[3] = 0

            rowIndex[2] += 1
            if(rowIndex[2] == 2):
                rowIndex[2] = 0
                # print(value)
            
            
    elif(line >= 65 and line <= 72):
        pass

    elif(line >= 75 and line <= 82):
        pass

    elif(line >= 85 and line <= 92):
        pass

    elif(line >= 95 and line <= 102):
        pass

    elif(line >= 95 and line <= 102):
        pass

    elif(line >= 105 and line <= 112):
        pass

    elif(line >= 115 and line <= 122):
        pass

    elif(line >= 125 and line <= 132):
        pass

    elif(line >= 135 and line <= 142):
        pass

    elif(line >= 145 and line <= 152):
        pass

    elif(line >= 155 and line <= 162):
        pass

    elif(line >= 165 and line <= 172):
        pass

    elif(line >= 175 and line <= 182):
        pass
    