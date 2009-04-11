#### Movable IDLE Dialog

import sys
import Tkinter
import tkFont
from webbrowser import open as openbrow
from Tkdialog import Dialog
from image_data import movpyLogo


class MovableIDLEDialog(Dialog):

    url = 'http://www.voidspace.org.uk/python/movpy/'

    def __init__(self, root, version):
        self.version = version
        # saves root as self.parent
        Dialog.__init__(self, root, bg="white")
    
    def body(self, master):
        head = 'Movable IDLE'
        msg = 'For Python %s' % sys.version[:5]
        msg2 = 'By Michael Foord'
        msg3 = 'Try Movable Python' 
        self.title("Movable IDLE: Version %s" % self.version)
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
        Dialog.buttonbox(self, 'Try Movpy', 'Continue')

    def ok(self, event=None):
        openbrow(self.url)
        Dialog.ok(self)

    def website(self, event=None):
        openbrow(self.url)
