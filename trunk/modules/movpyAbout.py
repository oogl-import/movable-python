#### Movable Python
#### movpyAbout.py

# Homepage : http://www.voidspace.org.uk/python/movpy/
# Download from : http://voidspace.tradebit.com

# Copyright Michael Foord, 2004-2006.
# Commercial software.

# For information about bugfixes, updates and support, 
# or for bug reports and feature requests - join the movpy mailing list.
# http://groups.google.com/group/movpy/
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

import sys
import Tkinter

from webbrowser import open as openbrow

from _CallTipWindow import createCallTip

from image_data import movpyLogo
from movpyURLs import website

FONT = ("tahoma", "8", "bold")
FONT2 = ("tahoma", "8", "normal")

titleFONT = ("tahoma", "16", "bold")
titleFONT2 = ("tahoma", "12", "bold")

TITLE = "About Movable Python"

text = (
    'Movable Python is a portable distribution of the \n'
    'Python programming language, for Windows.\n\n'
    'Now you can carry a full Python development environment \n'
    'around on a USB stick. It is also useful for testing programs\n'
    'with multiple versions of Python, or as a programmers tool.\n\n'
    'Movable Python is the creation of Michael Foord.\n'
)

copyright = '%s Voidspace.org.uk 2005-2006' % u"\u00A9"


class AboutDialog(Tkinter.Toplevel):
    
    def __init__(self, parent, version):
        self.parent = parent
        parent.grab_release()
        Tkinter.Toplevel.__init__(self, parent)
        self.title(TITLE)
        self.protocol("WM_DELETE_WINDOW", self.exit)
        self.bind('<Escape>', self.exit)
        self.bind('<Return>', self.exit)
        self.resizable(0, 0)
        x = parent.winfo_rootx()+50
        y =parent.winfo_rooty()-100
        if y < 10:
            y = 10
        self.geometry("+%d+%d" % (x, y))
        #
        self.version = version
        self.loadImages()
        self.buildDialog()
        #
        self.transient(parent)
        self.grab_set()
        self.focus_set()
        #
        self.wait_window(self)


    def loadImages(self):
        self._logo = Tkinter.PhotoImage(format='gif', data=movpyLogo)


    def buildDialog(self):
        f = Tkinter.Frame(self, background="white", bd=2, relief="ridge")
        l = Tkinter.Label(f, text="Movable Python", font=titleFONT, bg="white")
        l.grid(row=0, column=0, padx=4, pady=4)
        version = 'Version: %s' % self.version
        l = Tkinter.Label(f, text=version, font=titleFONT2, bg="white")
        l.grid(row=1, column=0, padx=4, pady=4)
        b = Tkinter.Button(f, image=self._logo, command=self.openWeb)
        createCallTip(b, "Visit Movable Python on the Web")
        b.grid(row=2, column=0, padx=4, pady=4)
        pyVersion = 'For Python %s' % '.'.join([str(i) for i in sys.version_info[:3]])
        if sys.version_info[3] != 'final':
            pyVersion += '.' + sys.version_info[3] + str(sys.version_info[4])
        l = Tkinter.Label(f, text=pyVersion, font=titleFONT2, bg="white")
        l.grid(row=3, column=0, padx=4, pady=4)
        l = Tkinter.Label(f, text=text, font=FONT2, bg="white")
        l.grid(row=4, column=0, padx=4, pady=4)
        l = Tkinter.Label(f, text=copyright, font=FONT, bg="white")
        l.grid(row=5, column=0, padx=4, pady=4)
        
        f.grid(row=0, column=0, padx=4, pady=4)
        b = Tkinter.Button(self, text="  OK  ", font=FONT, command=self.exit)
        b.grid(row=1, column=0, padx=4, pady=4)


    def openWeb(self):
        openbrow(website)
    
    
    def exit(self, event=None):
        self.withdraw()
        self.update_idletasks()
        # put focus back to the parent window
        self.parent.focus_set()
        self.parent.grab_set()
        self.parent.focus()
        self.parent.lift()
        self.destroy()
