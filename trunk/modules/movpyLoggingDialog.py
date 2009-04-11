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
import sys
import Tkinter

import Pmw

from _CallTipWindow import bindButtonImages, createCallTip
from _pathutils import get_main_dir, relpath
from image_data import open_document, open_document_h
from movpy_tools import joinPaths
from movpyFileDialog import fileDialog
from movpy import configdir

FONT = ("tahoma", "8", "bold")
FONT2 = ("tahoma", "8", "normal")

W = Tkinter.W
E = Tkinter.E

TITLE = "Configure Logging"
MSG = "Configure Logging"
calltip = (
"""
Configure Movpy logging here.

Values set here will also be used when
Movpy is run from the command line.

You can use special values in the filename:

    {DATE} - Inserts the date
    {TIME} - Inserts the time
    {FILE} - Inserts the name of the file

The file path is stored relative to your
Movable Python directory.
""")[1:-1]

_LOG_MODE = {None: 0, 'w': 1, 'a': 2}
_MODE_FROM_VAL = {0: None, 1: 'w',2: 'a'}

class ConfigureLogging(Tkinter.Toplevel):
    
    def __init__(self, parent, logFile, logMode):
        parent.grab_release()
        Tkinter.Toplevel.__init__(self, parent)
        self.title(TITLE)
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.resizable(0, 0)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))
        #
        self.parent = parent
        self.logFile = logFile
        self.originalLogFile = logFile
        self.logMode = logMode
        self.originalLogMode = logMode
        #
        self.loadImages()
        self.buildDialog()
        #
        self.transient(parent)
        self.grab_set()
        self.focus_set()
        #
        self.wait_window(self)


    def loadImages(self):
        self._openIMG = Tkinter.PhotoImage(format='gif', data=open_document)
        self._openIMG_H = Tkinter.PhotoImage(format='gif', data=open_document_h)


    def buildDialog(self):
        # add standard button box. override if you don't want the
        # standard buttons
        #
        l = Tkinter.Label(self, text=MSG, font=FONT)
        createCallTip(l, calltip)
        l.grid(row=0, column=0, columnspan=5, padx=5, pady=8)
        #
        Tkinter.Label(self, text="Log Mode:", font=FONT).grid(row=1,
                                                       column=0,
                                                       padx=4,
                                                       pady=2,
                                                       sticky=E)
        self._logModeVar = Tkinter.IntVar()
        b = Tkinter.Radiobutton(self, variable=self._logModeVar, value=0,
                            text='Off',
                            font=FONT2)
        b.grid(row=1,
               column=2,
               padx=4,
               pady=2,
               sticky=W)
        createCallTip(b, "No Logging")
        b = Tkinter.Radiobutton(self, variable=self._logModeVar, value=1,
                            text='Write',
                            font=FONT2)
        createCallTip(b, "Overwrite Files if Necessary")
        b.grid(row=1,
               column=3,
               padx=4,
               pady=2,
               sticky=W)
        b = Tkinter.Radiobutton(self, variable=self._logModeVar, value=2,
                            text='Append',
                            font=FONT2)
        b.grid(row=1,
               column=4,
               padx=4,
               pady=2,
               sticky=W)
        createCallTip(b, "Open Files in Append Mode")
        self._logModeVar.set(_LOG_MODE[self.logMode])
        #
        f = Tkinter.Frame(self)
        Tkinter.Label(f, text="Log File:", font=FONT).pack(side=Tkinter.LEFT, padx=10)
        self._chooseFile = Pmw.EntryField(f)
        self._chooseFile.pack(side=Tkinter.LEFT, padx=5)
        self._chooseFile.setvalue(self.logFile)
        b = Tkinter.Button(f, image=self._openIMG,
                       command=self.chooseFile)
        bindButtonImages(b, self._openIMG, self._openIMG_H, "Choose a File")
        b.pack(side=Tkinter.LEFT, padx=10)
        f.grid(row=2, column=0, columnspan=5, padx=5, pady=8, sticky=E+W)
        #
        f = Tkinter.Frame(self)
        b1 = Tkinter.Button(f, text=" OK ", width=12, command=self.ok, default=Tkinter.ACTIVE,
            font=FONT2)
        b1.focus()
        b1.bind("<Return>", self.ok)
        createCallTip(b1, "Save & Exit")
        b1.pack(side=Tkinter.LEFT, padx=15)
        b2 = Tkinter.Button(f, text="Cancel", width=12, command=self.cancel,
            font=FONT2)
        b2.bind("<Return>", self.cancel)
        createCallTip(b2, "Undo Changes")
        b2.pack(side=Tkinter.RIGHT, padx=15)
        #
        self.bind("<Escape>", self.cancel)
        self.bind("<Return>", self.ok)
        #
        f.grid(row=3, column=0, columnspan=5, padx=5, pady=8, sticky=E+W)


    def chooseFile(self):
        filename = self._chooseFile.getvalue()
        directory = os.getcwd()
        if filename:
            directory = os.path.abspath(joinPaths(configdir, os.path.dirname(filename)))
        filename = fileDialog("Choose a File...", directory, textTypes=True)
        self.lift()
        self.focus()
        if not filename:
            return
        self._chooseFile.setvalue(relpath(configdir, filename))


    def cancel(self, event=None):
        self.logFile = self.originalLogFile
        self.logMode = self.originalLogMode
        self.exit()


    def ok(self, event=None):
        self.logFile = self._chooseFile.getvalue()
        self.logMode = _MODE_FROM_VAL[self._logModeVar.get()]
        self.exit()


    def exit(self):
        self.withdraw()
        self.update_idletasks()
        # put focus back to the parent window
        self.parent.focus_set()
        self.parent.grab_set()
        self.parent.focus()
        self.parent.lift()
        self.destroy()


def showConfigureLogging(*args, **keywargs):
    cl = ConfigureLogging(*args, **keywargs)
    return cl.logMode, cl.logFile
