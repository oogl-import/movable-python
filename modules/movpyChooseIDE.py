#### Movable Python
#### movpyChooseIDE.py

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

import Pmw

from _CallTipWindow import bindButtonImages, createCallTip
from _pathutils import relpath
from image_data import open_document, open_document_h
from movpyFileDialog import fileDialog
from movpy_tools import joinPaths
from movpy import movpydir

TITLE = "Choose an IDE"
MSG = "Pick Your Integrated Development Program."

calltip = (
"""
Choose the program that will be launched when
you press the "IDE" button.

This can be any program (Python script,
executable or batch file). If it is a Python script
it will be run using the default interpreter.

The args will be passed to the IDE when it is
launched.

The file is stored using a path relative to your
Movable Python directory.
"""
)[1:-1]

FONT = ("tahoma", "8", "bold")
FONT2 = ("tahoma", "8", "normal")

W = Tkinter.W
E = Tkinter.E


class ChooseIDE(Tkinter.Toplevel):
    
    def __init__(self, parent, IDEPath, args):
        parent.grab_release()
        Tkinter.Toplevel.__init__(self, parent)
        self.title(TITLE)
        self.protocol("WM_DELETE_WINDOW", self.exit)
        self.resizable(0, 0)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                      parent.winfo_rooty()+50))
        #
        self.dir = os.path.dirname(os.path.abspath(joinPaths(movpydir, IDEPath)))
        self.save = False
        self.parent = parent
        self.IDEPath = IDEPath
        self.args = args
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
        l.grid(row=0, column=0, columnspan=4, padx=5, pady=8)
        #
        #
        self._idePathVar = Pmw.EntryField(self)
        self._idePathVar.grid(row=1, column=1, padx=4, pady=2)
        self._idePathVar.setvalue(self.IDEPath)
        Tkinter.Label(self, text="IDE :", font=FONT).grid(row=1, column=0,
                                                               padx=5, pady=8)
        b = Tkinter.Button(self, image=self._openIMG, command=self.choose)
        bindButtonImages(b, self._openIMG, self._openIMG_H, "Pick Your IDE Program")
        b.grid(row=1, column=2, padx=5, pady=5)
        #
        Tkinter.Label(self, text="Args :", font=FONT).grid(row=2, column=0,
                                                               padx=5, pady=8)
        #
        self._argsVar = Pmw.EntryField(self)
        self._argsVar.grid(row=2, column=1, padx=4, pady=2)
        self._argsVar.setvalue(self.args)
        #
        f = Tkinter.Frame(self)
        b1 = Tkinter.Button(f, text=" OK ", width=12, command=self.yes, default=Tkinter.ACTIVE,
            font=FONT2)
        b1.focus()
        b1.bind("<Return>", self.yes)
        b1.pack(side=Tkinter.LEFT, padx=15)
        b2 = Tkinter.Button(f, text="Cancel", width=12, command=self.exit,
            font=FONT2)
        b2.bind("<Return>", self.exit)
        b2.pack(side=Tkinter.RIGHT, padx=15)
        #
        self.bind("<Escape>", self.exit)
        self.bind("<Return>", self.yes)
        #
        f.grid(row=3, column=0, columnspan=4, padx=5, pady=8, sticky=E+W)


    def yes(self, event=None):
        #
        self.save = True
        self.IDEPath = self._idePathVar.getvalue()
        self.args = self._argsVar.getvalue()
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
        filename = fileDialog("Choose an IDE...", self.dir)
        self.lift()
        self.focus()
        if not filename:
            return
        if os.path.isfile(filename):
            self.dir = os.path.dirname(filename)
        filename = relpath(movpydir, filename)
        self._idePathVar.setvalue(filename)
