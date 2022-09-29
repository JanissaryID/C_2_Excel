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

def bodySound(workbook, worksheet):
    tittle1 = ["DEFAULT PRESCALE 0dB  -->", "<< Unused"]
    tittle2 = ["SETTING PRESCALE", "SOURCE ->", "DTV", "ATV", "AV", "AV2", "YPBPR", "VGA", "HDMI", "HDMI2", "HDMI3", "HDMI4", "USB", "SV", "SCART", "STV"]
    tittle3 = ["SETTING EQUALIZER", "MODE ->", "MUSIC", "NEWS", "SPORTS", "STANDARD", "USER"]
    tittle4 = ["SETTING VOLUME NONLINEAR", "SOURCE ->", "DTV", "ATV", "AV", "AV2", "HDMI", "HDMI2", "HDMI3", "HDMI4", "USB"]
    tittle5 = ["SETTING EQUALIZER NONLINEAR", "SOURCE -->", "DTV", "ATV", "AV", "AV2", "YPBPR", "VGA", "HDMI", "HDMI2", "HDMI3", "HDMI4", "USB", "SV", "SCART", "STV"]
    tittle6 = ["SETTING DRC", "FUNCTION", "VALUE"]
    tittle7 = ["DEFAULT_AVC_THRESHOLD", "SOURCE -->", "DTV", "ATV", "AV", "AV2", "YPBPR", "VGA", "HDMI", "HDMI2", "HDMI3", "HDMI4", "USB", "SV", "SCART", "STV"]
    tittle8 = ["SETTING AVL", "SOURCE -->", "DTV", "ATV", "AV1", "AV2", "AV3", "YPBPR1", "YPBPR2", "VGA", "HDMI1", "HDMI2", "HDMI3", "HDMI4", "USB", "STV"]
    tittle9 = ["VOLUME TABLE", "SOURCE -->", "DTV", "ATV", "AV", "HDMI", "USB"]
    tittle10 = ["SETTING_SUBWOOFER_LOW", "DISPLAY ->"]
    tittle11 = ["SETTING_SUBWOOFER_HIGH", "DISPLAY ->"]
    tittle12 = ["LOUDNESS OFFSET TABLE", "VOL LEVEL", "LowSubw", "LowTreble", "HighSubw", "HighTreble"]
    tittle13 = ["SETTING PEQ", "DISPLAY ->", "BAND1", "BAND2", "BAND3", "BAND4", "BAND5"]
    tittle14 = ["SETTING HPF", "DISPLAY ->", "VALUE"]
    tittle15 = ["SETTING PRE VOLUME", "REGISTER", "VALUE"]
    tittle16 = ["PWM1_PERIOD", "INIT_PWM1_DUTY", "PWM1_DIV"]

    subtittle1 = ["MAINSPEAKER", "LINEOUT_LO", "LINEOUT_HI"]
    subtittle2 = ["120HZ", "500HZ", "1_5KHZ", "5KHZ", "10KHZ", "TREBLE", "BASS"]
    subtittle3 = ["OSD 0", "0SD 25", "OSD 50", "OSD 75", "OSD 100"]
    subtittle4 = ["0", "25", "50", "75", "100"]
    subtittle5 = ["DRC_ENABLE", "DRC_THRESHOLD"]
    subtittle6 = ["(AVC ENABLE - OFF)", "VALUE -->"]
    subtittle7 = ["(AVC ENABLE - ON)", "VALUE -->"]
    subtittle8 = ["VALUE"]
    subtittle9 = ["GAIN", "FO", "Q_VALUE"]
    subtittle10 = ["ENABLE", "FO", "Q_VALUE"]
    subtittle11 = ["0x112D58", "0x112D5A", "0x112D5C", "0x112D5E"]

    subtittle4_1 = ["120HZ", "500HZ", "1_5KHZ", "5KHZ", "10KHZ"]

    color0 = ["#FCD5B4", "#FABF8F", "#CCC0DA", "B8CCE4", "BFBFBF"]
    color0_1 = ["#D8E4BC", "#FABF8F", "#CCC0DA", "B8CCE4", "BFBFBF"]


    for i in range(len(tittle1)):
        alfabetStart = 'A'
        row = 2

        # print(cell)
        if(i < 1):
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(tittle1[i]),
                align="L",
                border=True,
                background=True,
                background_color="#92D050",
                font_color="#000000",
                font_size=14
            )
        else:
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i + 1), row)

            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(tittle1[i]),
                align="L",
                border=False,
                background=True,
                background_color="#FFFFFF",
                font_color="#000000",
                font_size=11
            )

    for i in range(len(tittle2)):
        
        alfabetStart = 'A'
        row = 4

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle2[i]),
            align="L",
            border=True,
            background=True,
            background_color="#8DB4E2",
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
            align="C",
            border=True,
            background=True,
            background_color="#8DB4E2",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle3)):
        
        alfabetStart = 'A'
        row = 9

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle3[i]),
            align="L",
            border=True,
            background=True,
            background_color="#00B050",
            font_color="#000000",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle3[i]),
            align="C",
            border=True,
            background=True,
            background_color="#00B050",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle4)):
        
        alfabetStart = 'A'
        row = 18

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle4[i]),
            align="L",
            border=True,
            background=True,
            background_color="#E26B0A",
            font_color="#000000",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle4[i]),
            align="C",
            border=True,
            background=True,
            background_color="#E26B0A",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle5)):
        
        alfabetStart = 'A'
        row = 25

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
                background_color="#948A54",
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
                background_color="#948A54",
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
                value=str(tittle5[i]),
                align="C",
                border=True,
                background=True,
                background_color="#948A54",
                font_color="#000000",
                font_size=14
            )

    for i in range(len(tittle6)):

        alfabetStart = 'A'
        row = 52

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle6[i]),
            align="L",
            border=True,
            background=True,
            background_color="#00B0F0",
            font_color="#000000",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle6[i]),
            align="C",
            border=True,
            background=True,
            background_color="#00B0F0",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle7)):

        alfabetStart = 'A'
        row = 56

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle7[i]),
            align="L",
            border=True,
            background=True,
            background_color="#92D050",
            font_color="#000000",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle7[i]),
            align="C",
            border=True,
            background=True,
            background_color="#92D050",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle8)):

        alfabetStart = 'A'
        row = 59

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle8[i]),
            align="L",
            border=True,
            background=True,
            background_color="#E26B0A",
            font_color="#000000",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle8[i]),
            align="C",
            border=True,
            background=True,
            background_color="#E26B0A",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle9)):

        alfabetStart = 'A'
        row = 63

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle9[i]),
            align="L",
            border=True,
            background=True,
            background_color="#538DD5",
            font_color="#000000",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle9[i]),
            align="C",
            border=True,
            background=True,
            background_color="#538DD5",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle10)):

        alfabetStart = 'A'
        row = 171

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle10[i]),
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
            value=str(tittle10[i]),
            align="C",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle11)):

        alfabetStart = 'A'
        row = 174

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle11[i]),
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
            value=str(tittle11[i]),
            align="C",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle12)):

        alfabetStart = 'A'
        row = 177

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle12[i]),
            align="L",
            border=True,
            background=True,
            background_color="#FFC000",
            font_color="#000000",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle12[i]),
            align="C",
            border=True,
            background=True,
            background_color="#FFC000",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle13)):

        alfabetStart = 'A'
        row = 197

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle13[i]),
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
            value=str(tittle13[i]),
            align="C",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle14)):

        alfabetStart = 'A'
        row = 203

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle14[i]),
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
            value=str(tittle14[i]),
            align="C",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle15)):

        alfabetStart = 'A'
        row = 209

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle15[i]),
            align="L",
            border=True,
            background=True,
            background_color="#FFFF00",
            font_color="#000000",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle15[i]),
            align="C",
            border=True,
            background=True,
            background_color="#FFFF00",
            font_color="#000000",
            font_size=14
        )

    for i in range(len(tittle16)):

        alfabetStart = 'O'
        row = 171

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        # print(cell)
        if(i == 0):
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle16[i]),
            align="L",
            border=True,
            background=True,
            background_color="#FFC7CE",
            font_color="#9C0006",
            font_size=14
        )
        else:
            fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(tittle16[i]),
            align="C",
            border=True,
            background=True,
            background_color="#FFC7CE",
            font_color="#9C0006",
            font_size=14
        )

    for i in range(len(subtittle1)):
        alfabetStart = 'B'
        row = 5

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle1[i]),
            align="C",
            border=True,
            background=True,
            background_color="#00B0F0",
            font_color="#000000",
            font_size=11
        )

    for i in range(len(subtittle2)):
        alfabetStart = 'B'
        row = 10

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle2[i]),
            align="C",
            border=True,
            background=True,
            background_color="#FFFF00",
            font_color="#000000",
            font_size=11
        )

    for i in range(len(subtittle3)):
        alfabetStart = 'B'
        row = 19

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle3[i]),
            align="C",
            border=True,
            background=True,
            background_color="#D8E4BC",
            font_color="#000000",
            font_size=11
        )

    row0 = 26
    rowColor0 = 0

    for j in range(len(subtittle4_1)):
        alfabetStart1 = 'B'

        cell1 = "{0}{1}".format(chr(ord(alfabetStart1)), row0)
        cell2 = "{0}{1}".format(chr(ord(alfabetStart1)), row0 + 4)

        fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell1,
                pos_cell_end=cell2,
                value=str(subtittle4_1[j]),
                align="C",
                border=True,
                background=True,
                background_color=color0_1[rowColor0],
                font_color="#000000",
                font_size=11,
                merge_cell=True
            )

        for i in range(len(subtittle4)):
            alfabetStart = 'C'
            
            cell = "{0}{1}".format(chr(ord(alfabetStart)), row0)
            
            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(subtittle4[i]),
                align="C",
                border=True,
                background=True,
                background_color=color0[rowColor0],
                font_color="#000000",
                font_size=11
            )

            # print(cell2)

            row0 += 1
        rowColor0 += 1
        if(rowColor0 == 6):
            rowColor0 = 0

    for i in range(len(subtittle5)):
        alfabetStart = 'B'
        row = 53

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle5[i]),
            align="C",
            border=True,
            background=True,
            background_color="#B7DEE8",
            font_color="#000000",
            font_size=11
        )

    for i in range(101):
        alfabetStart = 'B'
        row = 64

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str("VOL {0}".format(i)),
            align="C",
            border=True,
            background=True,
            background_color="#538DD5",
            font_color="#000000",
            font_size=11
        )

    for i in range(len(subtittle6)):
        alfabetStart = 'A'
        row = 57

        # print(cell)
        if(i < 1):
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(subtittle6[i]),
                align="R",
                border=False,
                background=True,
                background_color="#FFFFFF",
                font_color="#000000",
                font_size=11
            )
        else:
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(subtittle6[i]),
                align="L",
                border=True,
                background=True,
                background_color="#C4D79B",
                font_color="#000000",
                font_size=14
            )

    for i in range(len(subtittle7)):
        alfabetStart = 'A'
        row = 60

        # print(cell)
        if(i < 1):
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(subtittle7[i]),
                align="R",
                border=False,
                background=True,
                background_color="#FFFFFF",
                font_color="#000000",
                font_size=11
            )
        else:
            cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

            fill_cell(
                workbook=workbook,
                worksheet=worksheet,
                pos_cell_start=cell,
                pos_cell_end=cell,
                value=str(subtittle7[i]),
                align="L",
                border=True,
                background=True,
                background_color="#FABF8F",
                font_color="#000000",
                font_size=14
            )
    
    for i in range(len(subtittle8)):
        alfabetStart = 'B'
        row = 172

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle8[i]),
            align="L",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=11
        )
    
    for i in range(len(subtittle8)):
        alfabetStart = 'B'
        row = 175

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)

        # print(cell)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle8[i]),
            align="L",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=11
        )

    for i in range(17):
        alfabetStart = 'B'
        row = 178

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str("VOL {0}".format(i)),
            align="C",
            border=True,
            background=True,
            background_color="#FFC000",
            font_color="#000000",
            font_size=11
        )

    for i in range(len(subtittle9)):
        alfabetStart = 'B'
        row = 198

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle9[i]),
            align="L",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=11
        )

    for i in range(len(subtittle10)):
        alfabetStart = 'B'
        row = 204

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle10[i]),
            align="L",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=11
        )

    for i in range(len(subtittle11)):
        alfabetStart = 'B'
        row = 210

        cell = "{0}{1}".format(chr(ord(alfabetStart)), row + i)
        
        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(subtittle11[i]),
            align="L",
            border=True,
            background=True,
            background_color="#FFFF00",
            font_color="#000000",
            font_size=11
        )

    alfabetStart1 = 'D'
    row1 = 204

    cell1 = "{0}{1}".format(chr(ord(alfabetStart1)), row1)

    fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell1,
            pos_cell_end=cell1,
            value=str("( 0 = OFF; 1 = ON )"),
            align="L",
            border=False,
            background=True,
            background_color="#FFFFFF",
            font_color="#000000",
            font_size=11,
            bold=True
        )

    for i in range(11):
        alfabetStart = 'C'
        row = 171

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(i),
            align="C",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=14
        )

    for i in range(11):
        alfabetStart = 'C'
        row = 174

        cell = "{0}{1}".format(chr(ord(alfabetStart) + i), row)

        fill_cell(
            workbook=workbook,
            worksheet=worksheet,
            pos_cell_start=cell,
            pos_cell_end=cell,
            value=str(i),
            align="C",
            border=True,
            background=True,
            background_color="#CCC0DA",
            font_color="#000000",
            font_size=14
        )
