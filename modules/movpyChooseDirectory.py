#### Movable Python
#### movpyChooseDirectory.py

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
import Tkinter
from tkFileDialog import askdirectory

import Pmw

from _CallTipWindow import bindButtonImages, createCallTip
from _pathutils import relpath
from image_data import folder, folder_h
from movpy_tools import joinPaths
from movpy import movpydir

TITLE = "Choose the Working Directory"
MSG = "Choose the Directory Your Scripts Run In."

calltip = (
"""
Choose the directory that your scripts will be run in.

This directory is overriden by the '-f' option.

Leave this blank to run scripts in the current working
directory.

The directory is stored as a path relative to your
Movable Python directory.
"""
)[1:-1]

FONT = ("tahoma", "8", "bold")
FONT2 = ("tahoma", "8", "normal")

W = Tkinter.W
E = Tkinter.E


class ChooseDirectory(Tkinter.Toplevel):
    
    def __init__(self, parent, directory='.'):
        parent.grab_release()
        Tkinter.Toplevel.__init__(self, parent)
        self.title(TITLE)
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.resizable(0, 0)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                      parent.winfo_rooty()+50))
        #
        self.parent = parent
        self.directory = directory
        self.original_directory = directory
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
        self._folderIMG = Tkinter.PhotoImage(format='gif', data=folder)
        self._folderIMG_H = Tkinter.PhotoImage(format='gif', data=folder_h)


    def buildDialog(self):
        # add standard button box. override if you don't want the
        # standard buttons
        #
        l = Tkinter.Label(self, text=MSG, font=FONT)
        createCallTip(l, calltip)
        l.grid(row=0, column=0, columnspan=4, padx=5, pady=8)
        #
        Tkinter.Label(self, text="Directory:", font=FONT).grid(row=1, column=0,
                                                               padx=5, pady=8)
        #
        self._directoryVar = Pmw.EntryField(self)
        self._directoryVar.grid(row=1, column=2, padx=4, pady=2)
        self._directoryVar.setvalue(self.directory)
        b = Tkinter.Button(self, image=self._folderIMG, command=self.choose)
        bindButtonImages(b, self._folderIMG, self._folderIMG_H, "Choose Directory")
        b.grid(row=1, column=3, padx=5, pady=5)
        #
        f = Tkinter.Frame(self)
        b1 = Tkinter.Button(f, text=" OK ", width=12, command=self.yes, default=Tkinter.ACTIVE,
            font=FONT2)
        b1.focus()
        b1.bind("<Return>", self.yes)
        b1.pack(side=Tkinter.LEFT, padx=15)
        b2 = Tkinter.Button(f, text="Cancel", width=12, command=self.cancel,
            font=FONT2)
        b2.bind("<Return>", self.cancel)
        b2.pack(side=Tkinter.RIGHT, padx=15)
        #
        self.bind("<Escape>", self.cancel)
        self.bind("<Return>", self.yes)
        #
        f.grid(row=2, column=0, columnspan=4, padx=5, pady=8, sticky=E+W)


    def yes(self, event=None):
        #
        self.directory = self._directoryVar.getvalue()
        self.exit()


    def cancel(self, event=None):
        #
        self.directory = self.original_directory
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


    def choose(self):
        directory = askdirectory(parent=self, title="Choose a Directory",
                     initialdir=joinPaths(movpydir, self.directory))
        if directory:
            directory = relpath(movpydir, directory)
            self.directory = directory
            self._directoryVar.setvalue(directory)


def showChooseDirectory(*args, **keywargs):
    dialog = ChooseDirectory(*args, **keywargs)
    return dialog.directory
