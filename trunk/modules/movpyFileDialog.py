#### Movable Python
#### movpyFileDialog.py

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
import sys
import tkFileDialog

_py = ('Python Files', '*.py *.pyw *.pyc *.pyo')
_exe = ('Executable & Batch Files', '*.exe *.bat')
_all = ('All Files', '*')
_txt = ('Text & Log Files', '*.txt *.log')

# NOTE: Multiple file selection is off

def fileDialog(title, directory, pyFirst=True, textTypes=False):
    if textTypes:
        fileTypes = (_txt, _all)
    elif pyFirst:
        fileTypes = (_py, _exe, _all)
    else:
        fileTypes = (_exe, _py, _all)
    #
    if float(sys.version[:3]) > 2.2:
        # no multiple keyword in python 2.2
        filename = tkFileDialog.askopenfilename(
                              filetype=fileTypes,
                              multiple=0,
                              title=title,
                              initialdir=directory).replace("/", os.sep)
    else:
        filename = tkFileDialog.askopenfilename(
                              filetype=fileTypes,
                              initialdir=directory,
                              title=title).replace("/", os.sep)
    return filename
