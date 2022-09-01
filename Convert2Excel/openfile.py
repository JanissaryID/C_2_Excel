from processPicture import *

def read_c_file(workbook, worksheet):
    lineCount = 0
    filename = "pic.c"

    # open the file for reading
    filehandle = open(filename, 'r')
    while True:
        # read a single line
        line = filehandle.readline()
        if not line:
            break

        lineCount+=1
        processPicture(line=lineCount, lineValue=line, workbook=workbook, worksheet=worksheet)
        

    # close the pointer to that file
    filehandle.close()