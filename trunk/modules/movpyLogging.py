#### Movable Python
#### movpyLogging.py

# Homepage : http://www.voidspace.org.uk/python/movpy/
# Download from : http://voidspace.tradebit.com

# Copyright Michael Foord, 2004-2006.
# Commercial software.

# For information about bugfixes, updates and support, 
# or for bug reports and feature requests - join the movpy mailing list.
# http://groups.google.com/group/movpy/
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

import os
import time

from movpy_tools import joinPaths
from movpy import movpydir

# %DATE%, %TIME%, %FILE%

FILENAME = 'Filename: "%s"\n'
DATE = 'Date: %s\n'

def getLogFileName(filename, executedFile):
    dateStruct = time.localtime()
    year = str(dateStruct[0])
    month = str(dateStruct[1]).zfill(2)
    day = str(dateStruct[2]).zfill(2)
    hour = str(dateStruct[3]).zfill(2)
    minutes = str(dateStruct[4]).zfill(2)
    seconds = str(dateStruct[5]).zfill(2)
    dateStr = year + month + day
    timeStr = hour + minutes + seconds
    filename = filename.replace('{DATE}', dateStr).replace('{TIME}', timeStr)
    filename = filename.replace('{FILE}', os.path.split(executedFile)[1])
    #
    directories = os.path.dirname(filename)
    if not os.path.isdir(directories):
        try:
            os.makedirs(directories)
        except (IOError, OSError):
            return None
    return filename


def writeHeader(openFile, filename, logMode):
    if logMode == 'a':
        openFile.write('\n\n')
    openFile.write(FILENAME % filename)
    openFile.write(DATE % time.ctime())
    openFile.write('\n')


if __name__ == '__main__':
    print getLogFileName('log/{DATE}-{TIME}-{FILE}.log', 'test.txt')
