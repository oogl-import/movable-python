#### Movable Python
#### movpySharewareDialog.py

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
import tkFont
from webbrowser import open as openbrow
from Tkdialog import Dialog
from image_data import movpyLogo
import time

class ExpiredDialog(object):

    url1 = 'http://www.voidspace.org.uk/python/movpy/'
    url2 = 'http://voidspace.tradebit.com/groups.php'

    def __init__(self, parent, version):
        msg = 'Trial Version Has Expired'
        msg2 = 'To Obtain Movable Python'
        msg3 = 'Visit the Shop'
        self.parent = parent
        self.parent.title("Movable Python: Demo Expired")
        # set size of main window
        self.parent.geometry("320x320")
        self.parent.protocol("WM_DELETE_WINDOW", self.quit)
        # make it non-resizable
        self.parent.resizable(0,0)
        f = tkFont.Font(family="Helvetica", size=14, weight=tkFont.BOLD)
        Tkinter.Label(parent, text=version, font=f, bg="white").pack()
        Tkinter.Label(parent, text=msg, font=f, bg="white").pack()
        image1 = Tkinter.PhotoImage(data=movpyLogo)
        b = Tkinter.Button(parent, image=image1, command=self.website)
        b.pack(pady=5)
        self.image1 = image1
        #
        Tkinter.Label(parent, text=msg2, font=f, bg="white").pack()
        Tkinter.Label(parent, text=msg3, font=f, bg="white").pack()
        fr = Tkinter.Frame(parent, bg="white")
        Tkinter.Button(fr, text='   OK   ', command=self.shop, font=f).pack(
            side=Tkinter.LEFT, padx=15, pady=4)
        Tkinter.Button(fr, text='Cancel', command=self.quit, font=f).pack(
            side=Tkinter.LEFT, padx=15, pady=4)
        fr.pack()

    def quit(self, event=None):
        self.parent.destroy()

    def shop(self, event=None):
        openbrow(self.url2)
        self.parent.destroy()

    def website(self, event=None):
        openbrow(self.url1)
        self.parent.destroy()


class SharewareDialog(Dialog):

    url1 = 'http://www.voidspace.org.uk/python/movpy/'
    url2 = 'http://voidspace.tradebit.com/groups.php'

    def __init__(self, root, expires):
        self.expires = expires
        # saves root as self.parent
        Dialog.__init__(self, root, bg="white")
    
    def body(self, master):
        import time
        head = 'Movable Python\nDemo Version'
        msg = 'This Trial Expires On'
        msg2 = 'To Obtain Movable Python'
        msg3 = 'Visit the Shop'
        self.title("Movable Python: Demo Version")
        date = time.strftime('%a %d %b, %Y.', time.localtime(
            self.expires))
        # set size of main window
        self.geometry("320x385")
        # make it non-resizable
        self.resizable(0,0)
        f1 = tkFont.Font(family="Helvetica", size=18,
            weight=tkFont.BOLD)
        f2 = tkFont.Font(family="Helvetica", size=14,
            weight=tkFont.BOLD)
        Tkinter.Label(self, text=head, font=f1, bg="white").pack()
        Tkinter.Label(self, text=msg, font=f2, bg="white").pack()
        Tkinter.Label(self, text=date, font=f2, bg="white").pack()
        image = Tkinter.PhotoImage(data=movpyLogo)
        b = Tkinter.Button(self, image=image,
            command=self.website)
        b.pack(pady=10)
        self.image = image
        #
        Tkinter.Label(self, text=msg2, font=f2, bg="white").pack()
        Tkinter.Label(self, text=msg3, font=f2, bg="white").pack()
        self.focus()
    
    def buttonbox(self):
        Dialog.buttonbox(self, 'Visit', 'Continue')

    def ok(self, event=None):
        openbrow(self.url2)
        Dialog.ok(self)

    def website(self, event=None):
        openbrow(self.url1)
        Dialog.ok(self)
