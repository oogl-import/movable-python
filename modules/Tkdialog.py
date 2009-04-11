from Tkinter import *
import tkFont

__all__ = ('Dialog')

class Dialog(Toplevel):

    def __init__(self, parent, title = None, bg=None):
        Toplevel.__init__(self, parent, bg=bg)
        self.font = tkFont.Font(family="Helvetica", size=12,
            weight=tkFont.BOLD)
        self.transient(parent)
        #
        if title:
            self.title(title)
        #
        self.parent = parent
        #
        self.result = None
        #
        body = Frame(self, bg=bg)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        #
        self.bg = bg
        self.buttonbox()
        #
        self.grab_set()
        #
        if not self.initial_focus:
            self.initial_focus = self
        #
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        #
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))
        #
        self.initial_focus.focus_set()
        #
        self.wait_window(self)

    #
    # construction hooks

    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden
        pass

    def buttonbox(self, ok="OK", cancel="cancel"):
        # add standard button box. override if you don't want the
        # standard buttons
        box = Frame(self, bg=self.bg)
        #
        w = Button(box, text=ok, width=10, command=self.ok, default=ACTIVE,
            font=self.font)
        w.pack(side=LEFT, padx=5, pady=8)
        w = Button(box, text=cancel, width=10, command=self.cancel,
            font=self.font)
        w.pack(side=LEFT, padx=5, pady=8)
        #
        self.bind("&lt;Return>", self.ok)
        self.bind("&lt;Escape>", self.cancel)
        #
        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return
        #
        self.withdraw()
        self.update_idletasks()
        #
        self.apply()
        #
        self.cancel()

    def cancel(self, event=None):
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):
        return 1 # override

    def apply(self):
        pass # override