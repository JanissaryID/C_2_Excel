import re
from excel import fill_cell

DEBUG = 1

rowStart = [2, 5, 10, 19, 26, 53, 57, 60, 64, 172, 175, 172, 178, 198, 204, 210]

rowIndex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
alfabetIndex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
colorIndex = [0, 0, 0, 0, 0]

color = ["#FCD5B4", "#FABF8F", "#CCC0DA", "B8CCE4", "BFBFBF"]

def processSound(line, lineValue, workbook, worksheet):
    if(line == 21):
        if DEBUG:
            alfabetStart = 'B'
            
            value = []
            res = re.split(', |{ | }|\n| ', lineValue)

            # print(res)

            for i in range(len(res) - 1):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            # print(value)

            for i in range(len(value)):

                cell = "{0}{1}".format(chr(ord(alfabetStart) + i), rowStart[0])

                fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=str(value[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#808080",
                    font_color="#000000",
                    font_size=11
                )

    if(line >= 24 and line <= 69):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n| ', lineValue)

            for i in range(len(res) - 1):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            for i in range(len(value)):
                alfabet_now = chr(ord(alfabetStart) + int(alfabetIndex[0]))
                cell = "{0}{1}".format(alfabet_now, rowStart[1] + rowIndex[0])

                if(alfabet_now != "N" and alfabet_now != "O" and rowIndex[0] != 1):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#00B0F0",
                        font_color="#FF0000",
                        font_size=11
                    )
                else:
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#00B0F0",
                        font_color="#000000",
                        font_size=11
                    )
            alfabetIndex[0] += 1

            if(len(value) == 0):
                alfabetIndex[0] = 0

            if(alfabetIndex[0] == 14):
                rowIndex[0] += 1

    if(line >= 78 and line <= 120):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n| ', lineValue)

            for i in range(len(res) - 1):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            for i in range(len(value)):
                alfabet_now = chr(ord(alfabetStart) + int(alfabetIndex[1]))
                cell = "{0}{1}".format(alfabet_now, rowStart[2] + rowIndex[1])

                fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=str(value[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#FFFFFF",
                    font_color="#000000",
                    font_size=11
                )

            rowIndex[1] += 1
            if(rowIndex[1] == 8):
                rowIndex[1] = -1
                alfabetIndex[1] += 1

    if(line >= 128 and line <= 136):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(',|{ | }|\n| ', lineValue)

            for i in range(len(res) - 2):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            # print(value)

            for i in range(len(value)):
                alfabet_now = chr(ord(alfabetStart) + int(alfabetIndex[2]))
                cell = "{0}{1}".format(alfabet_now, rowStart[3] + rowIndex[2])

                fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=str(value[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#FFFFFF",
                    font_color="#000000",
                    font_size=11
                )

                rowIndex[2] += 1
                if(rowIndex[2] == 5):
                    rowIndex[2] = 0
                    alfabetIndex[2] += 1

    if(line >= 145 and line <= 240):
        if DEBUG:
            alfabetStart = 'D'
            
            value = []
            res = re.split(',|{ | }|\n| ', lineValue)

            for i in range(len(res) - 2):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            if(len(value) != 0):
                for i in range(len(value)):
                    alfabet_now = chr(ord(alfabetStart) + int(alfabetIndex[3]))
                    cell = "{0}{1}".format(alfabet_now, rowStart[4] + rowIndex[3])

                    if(alfabet_now == "I" or alfabet_now == "O" or alfabet_now == "P" or alfabet_now == "Q"):
                        fill_cell(
                            workbook=workbook,
                            worksheet=worksheet,
                            pos_cell_start=cell,
                            pos_cell_end=cell,
                            value=str(value[i]),
                            align="C",
                            border=True,
                            background=True,
                            background_color=color[colorIndex[0]],
                            font_color="#000000",
                            font_size=11
                        )
                    else:
                        fill_cell(
                            workbook=workbook,
                            worksheet=worksheet,
                            pos_cell_start=cell,
                            pos_cell_end=cell,
                            value=str(value[i]),
                            align="C",
                            border=True,
                            background=True,
                            background_color="#FFFFFF",
                            font_color="#000000",
                            font_size=11
                        )

                    if(
                        (alfabet_now == "I" and rowIndex[3] >= 16 and rowIndex[3] <= 18) or
                        (alfabet_now == "Q" and rowIndex[3] >= 16 and rowIndex[3] <= 18) or
                        (alfabet_now == "Q" and rowIndex[3] >= 3 and rowIndex[3] <= 4) or
                        (alfabet_now == "Q" and rowIndex[3] >= 6 and rowIndex[3] <= 9) or
                        (alfabet_now == "Q" and rowIndex[3] >= 11 and rowIndex[3] <= 14)
                        ):
                        fill_cell(
                            workbook=workbook,
                            worksheet=worksheet,
                            pos_cell_start=cell,
                            pos_cell_end=cell,
                            value=str(value[i]),
                            align="C",
                            border=True,
                            background=True,
                            background_color=color[colorIndex[0]],
                            font_color="#FF0000",
                            font_size=11
                        )

                    rowIndex[3] += 1
                    if(rowIndex[3] == 25):
                        rowIndex[3] = 0
                        alfabetIndex[3] += 1
                        colorIndex[0] = -1

                    if(rowIndex[3] % 5 == 0):
                        colorIndex[0] += 1

    if(line >= 249 and line <= 250):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(',|{ | }|\n| ', lineValue)

            for i in range(len(res)):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            # print(value)

            for i in range(len(value)):
                alfabet_now = chr(ord(alfabetStart))
                cell = "{0}{1}".format(alfabet_now, rowStart[5] + rowIndex[4])

                fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=str(value[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#92CDDC",
                    font_color="#000000",
                    font_size=11
                )

            rowIndex[4] += 1

    if(line >= 257 and line <= 270):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(',|{ | }|\n| ', lineValue)

            for i in range(len(res) - 1):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            # print(value)

            for i in range(len(value)):
                alfabet_now = chr(ord(alfabetStart)  + rowIndex[5])
                cell = "{0}{1}".format(alfabet_now, rowStart[6])

                if(alfabet_now != "N" and alfabet_now != "O"):
                    fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=str(value[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#C4D79B",
                    font_color="#FF0000",
                    font_size=11
                )
                else:
                    fill_cell(
                    workbook=workbook,
                    worksheet=worksheet,
                    pos_cell_start=cell,
                    pos_cell_end=cell,
                    value=str(value[i]),
                    align="C",
                    border=True,
                    background=True,
                    background_color="#C4D79B",
                    font_color="#000000",
                    font_size=11
                )

                

            rowIndex[5] += 1

    if(line >= 278 and line <= 291):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(',|{ | }|\n| ', lineValue)

            for i in range(len(res) - 1):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            for i in range(len(value)):
                alfabet_now = chr(ord(alfabetStart)  + rowIndex[6])
                cell = "{0}{1}".format(alfabet_now, rowStart[7])

                if(alfabet_now == "C" or alfabet_now == "P"):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#FABF8F",
                        font_color="#FF0000",
                        font_size=11
                    )
                else:
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#FABF8F",
                        font_color="#000000",
                        font_size=11
                    )

            rowIndex[6] += 1

    if(line >= 299 and line <= 367):
        if DEBUG:
            alfabetStart = 'C'
            alfabetStart2 = 'B'
            
            value = []
            res = re.split(', |{ | }|\n| ', lineValue)

            for i in range(len(res)):
                if(res[i] != '' and res[i][:2] == "0x"):
                    value.append(res[i])

            for i in range(len(value)):

                alfabet_now = chr(ord(alfabetStart)  + alfabetIndex[4])
                cell = "{0}{1}".format(alfabet_now, rowStart[8] + rowIndex[7])

                if(len(value) != 0):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#B8CCE4",
                        font_color="#000000",
                        font_size=11
                    )

            # for i in range(len(value)):

            #     alfabet_now = chr(ord(alfabetStart2))
            #     cell = "{0}{1}".format(alfabet_now, rowStart[8] + rowIndex[7])

            #     # print(cell)

            #     if(len(value) != 0):
            #         fill_cell(
            #             workbook=workbook,
            #             worksheet=worksheet,
            #             pos_cell_start=cell,
            #             pos_cell_end=cell,
            #             value=str("{0} {1}".format("VOL", rowIndex[7])),
            #             align="C",
            #             border=True,
            #             background=True,
            #             background_color="#B8CCE4",
            #             font_color="#000000",
            #             font_size=11
            #         )

                rowIndex[7] += 1
                if(rowIndex[7] == 101):
                    rowIndex[7] = 0
                    alfabetIndex[4] += 1

    if(line == 376):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n| ', lineValue)

            for i in range(len(res)):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            for i in range(len(value)):

                alfabet_now = chr(ord(alfabetStart)  + alfabetIndex[5])
                cell = "{0}{1}".format(alfabet_now, rowStart[9])

                # print(cell)

                if(len(value) != 0):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#CCC0DA",
                        font_color="#000000",
                        font_size=11
                    )

                alfabetIndex[5] += 1
            
    if(line == 377):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n| ', lineValue)

            for i in range(len(res)):
                if(i > 3 and res[i] != ''):
                    value.append(res[i])

            for i in range(len(value)):

                alfabet_now = chr(ord(alfabetStart)  + alfabetIndex[6])
                cell = "{0}{1}".format(alfabet_now, rowStart[10])

                # print(cell)

                if(len(value) != 0):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#CCC0DA",
                        font_color="#000000",
                        font_size=11
                    )

                alfabetIndex[6] += 1

    if(line >= 379 and line <= 381):
        if DEBUG:
            alfabetStart = 'O'
            
            value = []
            res = re.split(', |{ | }|\n| ', lineValue)

            for i in range(len(res)):
                if(i > 1 and res[i] != ''):
                    value.append(res[i])

            # print(value)

            for i in range(len(value)):

                alfabet_now = chr(ord(alfabetStart)  + alfabetIndex[7])
                cell = "{0}{1}".format(alfabet_now, rowStart[11])

                if(len(value) != 0):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#FFFFFF",
                        font_color="#000000",
                        font_size=11
                    )
                    
            alfabetIndex[7] += 1

    if(line >= 389 and line <= 392):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n|;| ', lineValue)

            for i in range(len(res)):
                if(i > 1 and res[i] != ''):
                    value.append(res[i])

            # print(value)

            for i in range(len(value)):

                alfabet_now = chr(ord(alfabetStart)  + alfabetIndex[8])
                cell = "{0}{1}".format(alfabet_now, rowStart[12] + i)

                if(len(value) != 0):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#FFC000",
                        font_color="#000000",
                        font_size=11
                    )

            alfabetIndex[8] += 1

    if(line >= 400 and line <= 414):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n|;| ', lineValue)

            for i in range(len(res)):
                if(i > 1 and res[i] != ''):
                    value.append(res[i])

            # print(value)

            for i in range(len(value)):

                alfabet_now = chr(ord(alfabetStart)  + alfabetIndex[9])
                cell = "{0}{1}".format(alfabet_now, rowStart[13] + rowIndex[8])

                # print(cell)

                if(len(value) != 0):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#FFFFFF",
                        font_color="#000000",
                        font_size=11
                    )
            
            rowIndex[8] += 1
            if(rowIndex[8] == 3):
                rowIndex[8] = 0
                alfabetIndex[9] += 1

    if(line >= 422 and line <= 424):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n|;| ', lineValue)

            for i in range(len(res)):
                if(i > 1 and res[i] != ''):
                    value.append(res[i])

            # print(value)

            for i in range(len(value)):

                alfabet_now = chr(ord(alfabetStart))
                cell = "{0}{1}".format(alfabet_now, rowStart[14] + rowIndex[9])

                # print(cell)

                if(len(value) != 0):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#FFFFFF",
                        font_color="#000000",
                        font_size=11
                    )

            rowIndex[9] += 1

    if(line >= 432 and line <= 435):
        if DEBUG:
            alfabetStart = 'C'
            
            value = []
            res = re.split(', |{ | }|\n|;| ', lineValue)

            for i in range(len(res)):
                if(i > 1 and res[i] != ''):
                    value.append(res[i])

            # print(value)

            for i in range(len(value)):

                alfabet_now = chr(ord(alfabetStart))
                cell = "{0}{1}".format(alfabet_now, rowStart[15] + rowIndex[10])

                # print(cell)

                if(len(value) != 0):
                    fill_cell(
                        workbook=workbook,
                        worksheet=worksheet,
                        pos_cell_start=cell,
                        pos_cell_end=cell,
                        value=str(value[i]),
                        align="C",
                        border=True,
                        background=True,
                        background_color="#FFFFFF",
                        font_color="#000000",
                        font_size=11
                    )

            rowIndex[10] += 1

