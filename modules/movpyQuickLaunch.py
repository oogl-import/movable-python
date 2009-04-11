#### Movable Python
#### movpyQuickLaunch.py

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
from YesNoCancelDialog import CANCEL, NO, showYesNoCancel, YES

W = Tkinter.W
E = Tkinter.E
N = Tkinter.N
S = Tkinter.S

FONT = ("tahoma", "8", "bold")
FONT2 = ("tahoma", "8", "normal")

quickPanelCallTip = (
"""
Configure your Quick Launch Buttons Here.

Each button can have a script associated with it.
(Choose the script using the "File" button.)

If you choose a Python script it will be run using
the default interpreter.

You can also choose a batch file or executable. If
you choose a non-Python file then options other than
"Use Args" will be ignored.

If "Use Args" is selected then whatever you type in
the "Args" entry box will be passed as command line
arguments to the script.

If it is not selected, then the arguments from the
"Args" entry box on the main GUI will be used instead.
"""
)[1:-1]


class QuickLaunch(object):
    def __init__(self, parent, quickLaunchData):
        self.quickLaunchData = quickLaunchData
        configQuickWin = Tkinter.Toplevel(parent)
        self._configQuickWin = configQuickWin
        configQuickWin.title("Configure Quick Launch")
        configQuickWin.protocol("WM_DELETE_WINDOW", self.quit)
        configQuickWin.resizable(0, 0)
        configQuickWin.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))
        self.parent = parent
        self.dir = os.getcwd()
        #
        self.loadImages()
        self.setupDialog()
        #
        self.save = False
        self._previousEntry = None
        self.setupQuickPanel()
        self._previousEntry = 1
        self._quickVar.set(1)
        self.resetEntry()
        #
        configQuickWin.focus()
        configQuickWin.grab_set()
        configQuickWin.lift()
        configQuickWin.wait_window()
    
    
    def loadImages(self):
        self._openIMG = Tkinter.PhotoImage(format='gif', data=open_document)
        self._openIMG_H = Tkinter.PhotoImage(format='gif', data=open_document_h)
    
    
    def setupDialog(self):
        configQuickWin = self._configQuickWin
        Tkinter.Label(configQuickWin, text="Button:", font=FONT).grid(row=0,
                                                                      column=0,
                                                                      padx=4,
                                                                      pady=2,
                                                                      sticky=E)
        self._quickVar = Tkinter.IntVar()
        for i in range(8):
            i += 1
            Tkinter.Radiobutton(configQuickWin, variable=self._quickVar, value=i,
                                text=str(i),
                                command=self.change,
                                font=FONT2).grid(row=i, column=0)
        #
        f = Tkinter.Frame(self._configQuickWin)
        b = Tkinter.Button(f,
                       font=FONT,
                       text=" OK ",
                       command=self.finish
                      )
        b.focus()
        createCallTip(b, "Save & Exit")
        b.grid(row=0, column=0, sticky=W, padx=40, pady=5)
        b = Tkinter.Button(f,
                       font=FONT,
                       text="Cancel",
                       command=self.quit
                      )
        createCallTip(b, "Undo Changes & Exit")
        b.grid(row=0, column=2, sticky=E, padx=40, pady=5)
        f.grid(row=i+1, column=0, columnspan=3, sticky=E+W)
        self._configQuickWin.bind('<Escape>', self.quit)
    
    
    def setupQuickPanel(self):
        l = Tkinter.Label(self._configQuickWin, text="Configure Quick Launch",
                      font=FONT)
        createCallTip(l, quickPanelCallTip)
        l.grid(row=0, column=1, columnspan=2)
        bl = Tkinter.Label(self._configQuickWin, text="Button 1", font=FONT)
        bl.grid(row=1, column=1, columnspan=2)
        #
        f = Tkinter.Frame(self._configQuickWin, borderwidth=4, relief='groove')
        Tkinter.Label(f, text="Name:", font=FONT).grid(row=0,
                                                       column=0,
                                                       padx=4,
                                                       pady=2,
                                                       sticky=E)
        Tkinter.Label(f, text="File:", font=FONT).grid(row=1,
                                                       column=0,
                                                       padx=4,
                                                       pady=2,
                                                       sticky=E)
        Tkinter.Label(f, text="Args:", font=FONT).grid(row=2,
                                                       column=0,
                                                       padx=4,
                                                       pady=2,
                                                       sticky=E)
        #
        self._chooseName = Pmw.EntryField(f)
        self._chooseName.grid(row=0, column=1, padx=4, pady=2, columnspan=4, sticky=E+W)
        #
        self._chooseScript = Pmw.EntryField(f)
        self._chooseScript.grid(row=1, column=1, padx=4, pady=2, columnspan=4, sticky=E+W)
        b = Tkinter.Button(f, image=self._openIMG,
                       command=self.chooseFile)
        bindButtonImages(b, self._openIMG, self._openIMG_H, "Choose a Script")
        b.grid(row=1, column=5, padx=4, pady=2)
        #
        self._chooseArgs = Pmw.EntryField(f)
        self._chooseArgs.grid(row=2, column=1, padx=4, pady=2, columnspan=4, sticky=E+W)
        #
        Tkinter.Label(f, text="Options:", font=FONT).grid(row=3,
                                                          column=0,
                                                          padx=4,
                                                          pady=2,
                                                          sticky=E)
        var = Tkinter.IntVar
        self._optDir = {
                        'Use Args': ('Use Args Specified Here', var()),
                        'f': ('Run in Script Dir', var()),
                        'i': ('Inspect After Run', var()),
                        'p': ('Psyco On', var()),
                        'u': ('Unbuffered', var()),
                        'b': ('Pause After Script', var()),
                        'IPOFF': ('IPython Off', var()),
                        'x': ('Skip First Line', var()),
                       }
        i = 0
        for opt in ('Use Args', 'f', 'i', 'IPOFF', 'p', 'u', 'b', 'x'):
            row = (i / 3) + 3
            col = (i % 3) + 2
            i += 1
            text, var = self._optDir[opt]
            b = Tkinter.Checkbutton(f, variable=var,
                                text=opt, font=FONT2)
            createCallTip(b, text)
            b.grid(row=row, column=col, sticky=W)
        #
        Tkinter.Label(f, text="Console:", font=FONT).grid(row=6,
                                                       column=0,
                                                       padx=4,
                                                       pady=2,
                                                       sticky=E)
        self._consoleOpt = Tkinter.IntVar()
        b = Tkinter.Radiobutton(f, variable=self._consoleOpt, value=0,
                            text='Normal',
                            font=FONT2)
        b.grid(row=6,
               column=2,
               padx=4,
               pady=2,
               sticky=W)
        createCallTip(b, "Console On for '.py', Off for '.pyw'")
        b = Tkinter.Radiobutton(f, variable=self._consoleOpt, value=1,
                            text='On',
                            font=FONT2)
        createCallTip(b, "Console On")
        b.grid(row=6,
               column=3,
               padx=4,
               pady=2,
               sticky=W)
        b = Tkinter.Radiobutton(f, variable=self._consoleOpt, value=2,
                            text='Off',
                            font=FONT2)
        b.grid(row=6,
               column=4,
               padx=4,
               pady=2,
               sticky=W)
        createCallTip(b, "Console Off")
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
        f.grid(row=2, column=1, rowspan=7, columnspan=2, pady=5, padx=5,
               ipadx=5, ipady=5)
        self._quickPanelLabel = bl
    
    
    def change(self):
        if self._currrentModified():
            choice = showYesNoCancel(parent=self._configQuickWin,
                msg=("Changes Detected in Quick Launch Button %s."
                     "\n Save Changes ?" % self._previousEntry))
            if choice == YES:
                self.storeEntry(self._previousEntry)
            elif choice == CANCEL:
                self._quickVar.set(self._previousEntry)
                return
        self._ignore = False
        self._previousEntry = self._quickVar.get()
        self._quickPanelLabel.config(text="Button %s" % self._previousEntry)
        self.resetEntry()
    
    
    def quit(self, event=None):
        self._configQuickWin.withdraw()
        self._configQuickWin.update_idletasks()
        self.parent.focus_set()
        self._configQuickWin.destroy()
    
    
    def finish(self):
        if self._currrentModified():
            choice = showYesNoCancel(parent=self._configQuickWin,
                msg=("Changes Detected in Quick Launch Button %s."
                     "\n Save Changes ?" % self._previousEntry))
            if choice == YES:
                self.storeEntry(self._previousEntry)
            elif choice == CANCEL:
                self._quickVar.set(self._previousEntry)
                return
        self.save = True
        self.quit()
        
    def chooseFile(self):
        filename = fileDialog("Choose a File...", self.dir)
        self._configQuickWin.lift()
        self._configQuickWin.focus()
        if not filename:
            return
        directory = os.path.abspath(os.path.dirname(filename))
        if os.path.isdir(directory):
            self.dir = directory
        self._chooseScript.setvalue(relpath(movpydir, filename))
    
    
    def storeEntry(self, entry=None):
        if entry is None:
            entry = self._quickVar.get()
        values = self.quickLaunchData[entry]
        values['filename'] = self._chooseScript.getvalue().rstrip()
        values['name'] = self._chooseName.getvalue().rstrip()
        values['use_args'] = self._optDir['Use Args'][1].get()
        values['args'] = self._chooseArgs.getvalue().rstrip()
        for opt in self._optDir:
            if opt == 'Use Args':
                continue
            var = self._optDir[opt][1]
            values['options'][opt] = bool(var.get())
        console = self._consoleOpt.get()
        if console == 0:
            values['options']['k'] = False
            values['options']['koff'] = False
        elif console == 1:
            values['options']['k'] = True
            values['options']['koff'] = False
        if console == 2:
            values['options']['k'] = False
            values['options']['koff'] = True
    
    
    def resetEntry(self):
        values = self.quickLaunchData[self._quickVar.get()]
        self._chooseScript.setvalue(values['filename'])
        self._chooseName.setvalue(values['name'])
        self._optDir['Use Args'][1].set(values['use_args'])
        self._chooseArgs.setvalue(values['args'])
        for opt in self._optDir:
            if opt == 'Use Args':
                continue
            self._optDir[opt][1].set(values['options'].get(opt, False))
        console = 0
        if values['options'].get('k'):
            console = 1
        elif values['options'].get('koff'):
            console = 2
        self._consoleOpt.set(console)
    
    
    def _currrentModified(self):
        values = self.quickLaunchData[self._previousEntry]
        if values['filename'] != self._chooseScript.getvalue().rstrip():
            return True
        if values['name'] != self._chooseName.getvalue().rstrip():
            return True
        if values['use_args'] != self._optDir['Use Args'][1].get():
            return True
        if values['args'] != self._chooseArgs.getvalue().rstrip():
            return True
        for opt in self._optDir:
            if opt == 'Use Args':
                continue
            var = self._optDir[opt][1]
            if values['options'].get(opt, False) != bool(var.get()):
                return True
        console = 0
        if values['options'].get('k'):
            console = 1
        elif values['options'].get('koff'):
            console = 2
        if console != self._consoleOpt.get():
            return True
        return False
    