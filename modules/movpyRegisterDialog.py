#### Movable Python
#### movpyRegisterDialog.py

# Homepage : http://www.voidspace.org.uk/python/movpy/
# Download from : http://voidspace.tradebit.com

# Copyright Michael Foord, 2004-2006.
# Commercial software.

# For information about bugfixes, updates and support, 
# or for bug reports and feature requests - join the movpy mailing list.
# http://groups.google.com/group/movpy/
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

import time
import Tkinter

from _CallTipWindow import createCallTip
from movpyRegistryDetect import find_installed_pythons
from movpyTkTable import MultiListbox
from movpyTkdialog import Dialog


W = Tkinter.W
E = Tkinter.E

FONT = ("tahoma", "8", "bold")
FONT2 = ("tahoma", "8", "normal")

registerCallTip = (
"""
Choose an installed version of Python here.

Double click on it, or select it and press
"OK".

The selected installation will be available
as an interpreter from Movable Python.
""")[1:-1]


class RegisterDialog(object):
    def __init__(self, parent):
        self.save = False
        self.pythons = find_installed_pythons()
        self.pythons.sort()
        self.pythons.reverse()
        if not self.pythons:
            Dialog(parent, "Not Found", font=FONT, cancel=False,
                   label="No Installed Python Found")
            return
        self.topLevel = Tkinter.Toplevel(parent)
        self.topLevel.title("Choose an Installed Version of Python")
        self.topLevel.protocol("WM_DELETE_WINDOW", self.quit)
        self.topLevel.resizable(0, 0)
        self.topLevel.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))
        #
        self.parent = parent
        #
        self.setupDialog()
        self.setupTable()
        #
        self.topLevel.transient(parent)
        self.topLevel.focus()
        self.topLevel.grab_set()
        self.topLevel.lift()
        self.topLevel.wait_window()
    
    
    def setupDialog(self):
        l = Tkinter.Label(self.topLevel, text="Pick Your Python", font=FONT)
        l.grid(row=0, column=0, padx=4, pady=2)
        createCallTip(l, registerCallTip)
        #
        f = Tkinter.Frame(self.topLevel)
        b = Tkinter.Button(f,
                           font=FONT,
                           text=" OK ",
                           command=self.finish,
                           anchor=W
                      )
        b.focus()
        createCallTip(b, "Use Selected Installation")
        b.grid(row=0, column=0, sticky=W, padx=50, pady=5)
        b = Tkinter.Button(f,
                           font=FONT,
                           text="Cancel",
                           command=self.quit,
                           anchor=E
                      )
        createCallTip(b, "Exit With No Installation Chosen")
        b.grid(row=0, column=1, sticky=E, padx=50, pady=5)
        f.grid(row=3, column=0, sticky=E+W)
        self.topLevel.bind('<Escape>', self.quit)
    
    
    def setupTable(self):
        mlb = MultiListbox(self.topLevel, (
                            ('Index', 6),
                            ('Version', 8),
                            ('Path', 30)
                           ), self.selectAction)
        for i in range(len(self.pythons)):
            date, version, path = self.pythons[i]
            mlb.insert(Tkinter.END, (str(i+1), version, path))
        mlb.grid(row=2, column=0)
        self._listBox = mlb
    
    
    def selectAction(self, event):
        self.save = self.pythons[self._listBox.lists[0].nearest(event.y)]
        self.quit()
    
    
    def quit(self, event=None):
        self.topLevel.withdraw()
        self.topLevel.update_idletasks()
        self.parent.focus_set()
        self.topLevel.destroy()
    
    
    def finish(self):
        index = self._listBox.lists[0].curselection()
        if index:
            self.save = self.pythons[int(index[0])]
        self.quit()
