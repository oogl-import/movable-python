#### Movable Python
#### YesNoCancelDialog.py

# Homepage : http://www.voidspace.org.uk/python/movpy/
# Download from : http://voidspace.tradebit.com

# Copyright Michael Foord, 2004-2006.
# Commercial software.

# For information about bugfixes, updates and support, 
# or for bug reports and feature requests - join the movpy mailing list.
# http://groups.google.com/group/movpy/
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

import Tkinter

_DEFAULT_TITLE = "Changes Detected"

_DEFAULT_MSG = "Changes Detected. Save ?"

FONT = ("tahoma", "8", "bold")
FONT2 = ("tahoma", "8", "normal")

__all__ = (
    'YES',
    'NO',
    'CANCEL',
    'YesNoCancelDialog',
    'showYesNoCancel'
)

YES = 2
NO = 1
CANCEL = None

class YesNoCancelDialog(Tkinter.Toplevel):
    
    def __init__(self, parent, title=_DEFAULT_TITLE, msg=_DEFAULT_MSG):
        parent.grab_release()
        Tkinter.Toplevel.__init__(self, parent)
        self.title(title)
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.resizable(0, 0)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                      parent.winfo_rooty()+50))
        #
        self.parent = parent
        self.result = CANCEL
        self.msg = msg
        #
        body = Tkinter.Frame(self)
        body.pack(padx=5, pady=5)
        #
        self.buttonbox()
        #
        self.transient(parent)
        self.grab_set()
        self.focus_set()
        #
        self.wait_window(self)


    def buttonbox(self, ok="OK", save="Save", cancel="Cancel"):
        # add standard button box. override if you don't want the
        # standard buttons
        box = Tkinter.Frame(self)
        #
        Tkinter.Label(self, text=self.msg, font=FONT).pack(side=Tkinter.TOP, padx=5, pady=8)
        b1 = Tkinter.Button(box, text=" Yes ", width=10, command=self.yes, default=Tkinter.ACTIVE,
            font=FONT2)
        b1.focus()
        b1.bind("<Return>", self.yes)
        b1.pack(side=Tkinter.LEFT, padx=5, pady=8)
        b2 = Tkinter.Button(box, text=" No ", width=10, command=self.no,
            font=FONT2)
        b2.bind("<Return>", self.no)
        b2.pack(side=Tkinter.LEFT, padx=5, pady=8)
        b3 = Tkinter.Button(box, text="Cancel", width=10, command=self.cancel,
            font=FONT2)
        b3.bind("<Return>", self.cancel)
        b3.pack(side=Tkinter.LEFT, padx=5, pady=8)
        #
        self.bind("<Escape>", self.cancel)
        self.bind("<Return>", self.yes)
        #
        box.pack()


    #
    # standard button semantics

    def yes(self, event=None):
        self.withdraw()
        self.update_idletasks()
        #
        self.result = YES
        #
        self.cancel()


    def cancel(self, event=None):
        # put focus back to the parent window
        self.parent.focus_set()
        self.parent.grab_set()
        self.parent.focus()
        self.parent.lift()
        self.destroy()


    def no(self, event=None):
        self.withdraw()
        self.update_idletasks()
        #
        self.result = NO
        #
        self.cancel()


def showYesNoCancel(*args, **keywargs):
    dialog = YesNoCancelDialog(*args, **keywargs)
    return dialog.result
