#### Movable Python
#### movpyConfigureInterpreter.py

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
from movpy import movpydir
from movpyFileDialog import fileDialog
from movpyRegisterDialog import RegisterDialog
from movpyTkdialog import Dialog
from YesNoCancelDialog import CANCEL, NO, showYesNoCancel, YES


W = Tkinter.W
E = Tkinter.E
N = Tkinter.N
S = Tkinter.S

FONT = ("tahoma", "8", "bold")
FONT2 = ("tahoma", "8", "normal")

interpreterCallTip = (
"""
Configure your available interpreters here.
"""
)[1:-1]


class ConfigureInterpreter(object):
    def __init__(self, parent, interpreterData):
        self.interpreterData = interpreterData
        self.topLevel = Tkinter.Toplevel(parent)
        self.topLevel.title("Configure Interpreters")
        self.topLevel.protocol("WM_DELETE_WINDOW", self.quit)
        self.topLevel.resizable(0, 0)
        self.topLevel.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))
        #
        self._buttonPanel = None
        self.parent = parent
        self.dir = os.getcwd()
        self.save = False
        self._previousEntry = None
        self._interpreterPanel = None
        #
        self.loadImages()
        self.setupDialog()
        self.setupInterpreterSelectButtons()
        #
        if self.interpreterData:
            self._entryVar.set(0)
            self.copyValues(0)
        else:
            self._currentLabel.config(text="No Interpreters Available")
        #
        self.topLevel.focus()
        self.topLevel.grab_set()
        self.topLevel.lift()
        self.topLevel.wait_window()
    
    
    def loadImages(self):
        self._openIMG = Tkinter.PhotoImage(format='gif', data=open_document)
        self._openIMG_H = Tkinter.PhotoImage(format='gif', data=open_document_h)
    
    
    def setupDialog(self):
        Tkinter.Label(self.topLevel, text="Interpreter:", font=FONT).grid(row=0,
                                                                      column=0,
                                                                      padx=4,
                                                                      pady=2,
                                                                      sticky=E)
        self._entryVar = Tkinter.IntVar()
        #
        b = Tkinter.Button(self.topLevel,
                       font=FONT,
                       text="   New   ",
                       command=self.addInterpreter
                      )
        createCallTip(b, "Create a New Interpreter")
        b.grid(row=3, column=0, sticky=S, padx=5, pady=5)
        b = Tkinter.Button(self.topLevel,
                       font=FONT,
                       text="Remove",
                       command=self.removeInterpreter,
                       state=Tkinter.DISABLED
                      )
        createCallTip(b, "Remove Current Interpreter")
        b.grid(row=4, column=0, sticky=N, padx=5, pady=5)
        self._removeButton = b
        #
        f = Tkinter.Frame(self.topLevel)
        b = Tkinter.Button(f,
                       font=FONT,
                       text=" OK ",
                       command=self.finish
                      )
        b.focus()
        createCallTip(b, "Save & Exit")
        b.grid(row=0, column=0, sticky=W, padx=50, pady=5)
        b = Tkinter.Button(f,
                       font=FONT,
                       text="Cancel",
                       command=self.quit
                      )
        createCallTip(b, "Undo Changes & Exit")
        b.grid(row=0, column=1, sticky=E, padx=50, pady=5)
        f.grid(row=4, column=1, sticky=E+W)
        self.topLevel.bind('<Escape>', self.quit)
        #
        l = Tkinter.Label(self.topLevel, text="Configure Interpreters",
                      font=FONT)
        createCallTip(l, interpreterCallTip)
        l.grid(row=0, column=1)
        bl = Tkinter.Label(self.topLevel, font=FONT, anchor=N)
        bl.grid(row=1, column=1, sticky=N)
        self._currentLabel = bl
    
    
    def setupInterpreterSelectButtons(self):
        if self._buttonPanel is not None:
            self._buttonPanel.destroy()
        f = Tkinter.Frame(self.topLevel)
        for i in range(len(self.interpreterData)):
            Tkinter.Radiobutton(f, variable=self._entryVar, value=i,
                                text=str(i + 1),
                                command=self.change,
                                font=FONT2,
                                anchor=N).grid(row=i, column=0,
                                               padx=4, pady=4,
                                               sticky=N)
        f.grid(row=2, column=0, padx=4, pady=4)
        self._buttonPanel = f
    
    
    def setupPanel(self):
        #
        f = Tkinter.Frame(self.topLevel, borderwidth=4, relief='groove')
        Tkinter.Label(f, text="Name:", font=FONT).grid(row=0,
                                                       column=0,
                                                       padx=4,
                                                       pady=2,
                                                       sticky=E)
        Tkinter.Label(f, text="Executable:", font=FONT).grid(row=1,
                                                       column=0,
                                                       padx=4,
                                                       pady=2,
                                                       sticky=E)
        #
        self._chooseName = Pmw.EntryField(f)
        self._chooseName.grid(row=0, column=1, padx=4, pady=2, columnspan=2)
        #
        self._chooseInterpreter = Pmw.EntryField(f)
        self._chooseInterpreter.grid(row=1, column=1, padx=4, pady=2, columnspan=2)
        b = Tkinter.Button(f, image=self._openIMG,
                       command=self.chooseFile)
        bindButtonImages(b, self._openIMG, self._openIMG_H, "Choose an Interpreter")
        b.grid(row=1, column=3, padx=4, pady=2)
        #
        b = Tkinter.Button(f, text="Register",
                          command=self.registerInterpreter,
                          font=FONT)
        createCallTip(b, "Register Installed Python")
        b.grid(row=2, column=4, padx=4, pady=15, sticky=W)
        #
        f2 = Tkinter.Frame(f)
        b = Tkinter.Button(f2,
                       text="Save Entry",
                       command=self.storeEntry,
                       font=FONT2
                      )
        createCallTip(b, "Save these Settings")
        b.pack(side=Tkinter.LEFT, padx=15, pady=5)
        b = Tkinter.Button(f2,
                       text="Reset Entry",
                       command=self.resetEntry,
                       font=FONT2
                      )
        createCallTip(b, "Restore to Previous Settings")
        b.pack(side=Tkinter.RIGHT, padx=15, pady=5)
        f2.grid(row=7, column=0, columnspan=5, sticky=E+W)
        #
        f.grid(row=2, column=1, rowspan=2, pady=5, padx=5,
               ipadx=5, ipady=5, sticky=S+N)
        self._interpreterPanel = f
        self._removeButton.config(state=Tkinter.NORMAL)
    
    
    def change(self):
        if self._currrentModified():
            choice = showYesNoCancel(parent=self.topLevel,
                msg=("Unsaved Changes in \"%s\"."
                     "\n Save Changes ?" % self._chooseName.getvalue()))
            if choice == YES:
                self.storeEntry(self._previousEntry)
            elif choice == CANCEL:
                self._self._entryVar.set(self._previousEntry)
                return
        self.copyValues(self._entryVar.get())
    
    
    def copyValues(self, index):
        if self._interpreterPanel is None:
            self.setupPanel()
        name, path = self.interpreterData[index]
        if not name:
            name = name.strip() or 'Interpreter %s' % (index +1)
            self.interpreterData[index] = (name, path)
        self._chooseInterpreter.setvalue(path)
        self._chooseName.setvalue(name)
        self._currentLabel.config(text=name)
        self._previousEntry = self._entryVar.get()
    
    
    def quit(self, event=None):
        self.topLevel.withdraw()
        self.topLevel.update_idletasks()
        self.parent.focus_set()
        self.topLevel.destroy()
    
    
    def finish(self):
        if self._currrentModified():
            choice = showYesNoCancel(parent=self.topLevel,
                msg=("Unsaved Changes in \"%s\"."
                     "\n Save Changes ?" % self._chooseName.getvalue()))
            if choice == YES:
                self.storeEntry(self._previousEntry)
            elif choice == CANCEL:
                return
        self.save = True
        self.quit()
    
    
    def chooseFile(self):
        filename = fileDialog("Choose an Interpreter...", self.dir, pyFirst=False)
        self.topLevel.lift()
        self.topLevel.focus()
        if not filename:
            return
        directory = os.path.abspath(os.path.dirname(filename))
        if os.path.isdir(directory):
            self.dir = directory
        self._chooseInterpreter.setvalue(relpath(movpydir, filename))
    
    
    def addInterpreter(self):
        index = len(self.interpreterData)
        if not self.interpreterData:
            self.setupPanel()
        elif self._currrentModified():
            choice = showYesNoCancel(parent=self.topLevel,
                msg=("Unsaved Changes in \"%s\"."
                     "\n Save Changes ?" % self._chooseName.getvalue()))
            if choice == YES:
                self.storeEntry(self._previousEntry)
            elif choice == CANCEL:
                return
        name = 'Interpreter %s' % (index + 1)
        self.interpreterData.append((name, ''))
        self.setupInterpreterSelectButtons()
        self._entryVar.set(index)
        self.copyValues(index)
    
    
    def registerInterpreter(self):
        r = RegisterDialog(self.topLevel)
        if r.save:
            path = os.path.join(r.save[2], 'python.exe')
            name = 'Python %s' % r.save[1]
            index = self._entryVar.get()
            self._chooseInterpreter.setvalue(path)
            self._chooseName.setvalue(name)
        
    
    def storeEntry(self, index=None):
        if index is None:
            index = self._entryVar.get()
        self.interpreterData[index] = (self._chooseName.getvalue(), self._chooseInterpreter.getvalue())
    
    
    def resetEntry(self):
        index = self._entryVar.get()
        name, path = self.interpreterData[index]
        self._chooseName.setvalue(name)
        self._chooseInterpreter.setvalue(path)
    
    
    def removeInterpreter(self):
        d = Dialog(self.topLevel, "Are You Sure ?", font=FONT, label="Please Confirm")
        if not d.result:
            return
        index = self._entryVar.get()
        self.interpreterData.pop(index)
        if index and (index >= (len(self.interpreterData) - 1)):
            index -= 1
        self.setupInterpreterSelectButtons()
        if self.interpreterData:
            self._entryVar.set(index)
            self.copyValues(index)
        else:
            self._previousEntry = None
            self._interpreterPanel.destroy()
            self._removeButton.config(state=Tkinter.DISABLED)
            self._currentLabel.config(text="No Interpreters Available")
    
    
    def _currrentModified(self):
        if self._previousEntry is None:
            return False
        name, path = self.interpreterData[self._previousEntry]
        return (name, path) != (self._chooseName.getvalue(), self._chooseInterpreter.getvalue())
    
    