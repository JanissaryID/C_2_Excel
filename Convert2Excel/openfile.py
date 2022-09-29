from processPicture import *
from processSound import *

def read_c_file(workbook, worksheet):
    lineCount = 0
    filename = "sound.c"

    # open the file for reading
    filehandle = open(filename, 'r')
    while True:
        # read a single line
        line = filehandle.readline()
        if not line:
            break

        lineCount+=1
        # processPicture(line=lineCount, lineValue=line, workbook=workbook, worksheet=worksheet)
        processSound(line=lineCount, lineValue=line, workbook=workbook, worksheet=worksheet)

    # bodyPicture(workbook=workbook, worksheet=worksheet)
    bodySound(workbook=workbook, worksheet=worksheet)

    # close the pointer to that file
    filehandle.close()