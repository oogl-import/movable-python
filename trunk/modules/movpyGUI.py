#### Movable Python
#### movpyGUI.py

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
import sys
import tkMessageBox
import Tkinter

import Pmw

from copy import copy, deepcopy
from webbrowser import open as openbrow

from _CallTipWindow import bindButtonImages, createCallTip
from _pathutils import relpath

from command_line import the_options
from image_data import arrow_right, open_document, properties, rocket
from image_data import arrow_right_h, open_document_h, properties_h
from movpy_tools import joinPaths, remcom
from movpyAbout import AboutDialog
from movpyChooseDirectory import ChooseDirectory
from movpyChooseIDE import ChooseIDE
from movpyConfigureInterpreter import ConfigureInterpreter
from movpyFileDialog import fileDialog
from movpyLoggingDialog import showConfigureLogging
from movpy import movpydir, libdir, configdir, docdir
from movpyQuickLaunch import QuickLaunch
from movpySharewareDialog import SharewareDialog
from movpyURLs import aboutPage, mailingList, shop, website

from movpyGUITools import *

WIN98 = False
try:
    import win32api
except ImportError:
    pass
else:
    if win32api.GetVersionEx()[3] == 1:
        WIN98 = True
    from win32api import GetShortPathName

W = Tkinter.W
E = Tkinter.E
N = Tkinter.N
S = Tkinter.S
DISABLED = Tkinter.DISABLED
NORMAL = Tkinter.NORMAL

FONT = ("tahoma", "8", "bold")
FONT2 = ("tahoma", "8", "normal")

CFGOPTLBL = "Configure Movpy Options"
CFGOPTTIP = """
Configure the options that scripts are launched with.

It should be obvious what all these options do. For
more details see the docs page on options.

Your saved options will also be used by Movpy from
the command line, unless you override them with the
'-o' option.
"""[1:-1]

_LOG_MODE = {None: 0, 'w': 1, 'a': 2}
_MODE_FROM_VAL = {0: None, 1: 'w',2: 'a'}

TEST = False
try:
    TEST = (sys.movpy == 'test')
except AttributeError:
    pass

X = 460
Y = 140
if sys.version[:3] > '2.2':
    X = 420
size = '%sx%s' % (X, Y)

class MovpyGetFile(object):
    """A class to present the GUI."""

    def __init__(self, options, version, expired):
        if expired:
            version += ' Trial'
        self.expired = expired
        self.root = Tkinter.Tk()
        Pmw.initialise(self.root)
        self.root.geometry(size)
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.root.bind('<Escape>', self.quit)
        self.root.resizable(True, False)
        self.root.minsize(X, Y)
        self.root.maxsize(950, Y)
        #
        self.loadImages()
        self.buildVersion(version)
        self._commandLineOptions = options
        self.loadFileHistory()
        #
        self.setupSidePanel()
        self.setupChoosePanel()
        self.setupArgsPanel()
        self.setupOptionsPanel()
        self.setupQuickLaunchPanel()
        self.setupMenu()
        #
        self.loadOptions()
        self.loadInitialDirectory()
        self.loadWorkingDirectory()
        self.loadQuickLaunchConfig()
        self.loadIDE()
        self.loadConsole()
        self.loadLogging()
        self.loadInterpreters()
        self.setupInterpreterMenu()
        #
        if expired:
            self.d = SharewareDialog(self.root, expired)
        else:
            self.root.lift()
        self.root.grid_columnconfigure(3, weight=1)
    
    
    def loadImages(self):
        self._openIMG = Tkinter.PhotoImage(format='gif', data=open_document)
        self._arrowIMG = Tkinter.PhotoImage(format='gif', data=arrow_right)
        self._propertiesIMG = Tkinter.PhotoImage(format='gif', data=properties)
        self._openIMG_H = Tkinter.PhotoImage(format='gif', data=open_document_h)
        self._arrowIMG_H = Tkinter.PhotoImage(format='gif', data=arrow_right_h)
        self._propertiesIMG_H = Tkinter.PhotoImage(format='gif', data=properties_h)
        self._rocketIMG = Tkinter.PhotoImage(format='gif', data=rocket)
    
    
    def buildVersion(self, version):
        self._version = version
        ver = '.'.join([str(i) for i in sys.version_info[:3]])
        if sys.version_info[3] != 'final':
            ver += '.' + sys.version_info[3] + str(sys.version_info[4])
        self.root.title("Movable Python: %s, Python: %s" % (self._version, 
            ver))
    
    
    def loadFileHistory(self):
        self._list = []
        self._fileHistoryFile = joinPaths(configdir, 'file_history.txt')
        try:
            self._list = open(self._fileHistoryFile).read().splitlines()
        except (IOError, OSError):
            pass
    
    
    def setupSidePanel(self):
        b = Tkinter.Button(self.root, text=" IDE ",
                           font=FONT,
                           command=self.launchIDE)
        createCallTip(b, "Launch IDE")
        b.grid(row=0, rowspan=2,
               column=8,
               sticky=W+E+N+S,
               padx=5, pady=10)
        b = Tkinter.Button(self.root, text=" >>> ",
                           font=("arial", "10", "bold"),
                           command=self.launchInterpreter)
        createCallTip(b, "Interactive Interpreter")
        b.grid(row=2, rowspan=2,
                column=8,
                sticky=W+E+N+S,
                padx=5, pady=10)
    
    
    def setupChoosePanel(self):
        Tkinter.Label(self.root, text="Script:",
                      font=FONT).grid(row=0, column=2, padx=4, pady=2, sticky=E)
        self._chooseScript = Pmw.ComboBox(self.root,
                scrolledlist_items = self._list)
        self._chooseScript.component('entryfield').configure(command=self.runScript)
        #e = Tkinter.Entry(self.root, relief='ridge', background="white",
        #              foreground="black", borderwidth=4,
        #              textvariable=self._chooseScript)
        #self._chooseScript.bind('<Return>', self.runScript)
        self._chooseScript.grid(row=0, column=3, columnspan=2, padx=4, pady=2, sticky=E+W)
        
        b = Tkinter.Button(self.root, image=self._openIMG,
                       command=self.chooseScript)
        bindButtonImages(b, self._openIMG, self._openIMG_H, "Choose a Script")
        b.grid(row=0, column=5, padx=4, pady=2)
        b = Tkinter.Button(self.root, image=self._arrowIMG,
                       command=self.runScript)
        bindButtonImages(b, self._arrowIMG, self._arrowIMG_H, "Run Script")
        b.grid(row=0, column=6, padx=4, pady=2)
    
    
    def setupArgsPanel(self):
        Tkinter.Label(self.root, text="Launch:",
                      font=FONT).grid(row=0, column=0, padx=4, pady=2, sticky=E)
        b = Tkinter.Button(self.root, image=self._rocketIMG,
                       command=self.launchScript)
        bindButtonImages(b, self._rocketIMG, self._rocketIMG, "Browse & Run")
        b.grid(row=0, column=1, padx=4, pady=2)
        #
        Tkinter.Label(self.root, text="Args:",
                      font=FONT).grid(row=1, column=2, padx=4, pady=2, sticky=E)
        self._args = Pmw.EntryField(self.root)
        self._args.grid(row=1, column=3, padx=4, pady=2, sticky=E+W)
        self._args.bind('<Return>', self.runScript)
        self._args.focus()
        Tkinter.Label(self.root, text="",
                      font=FONT).grid(row=1, column=4, padx=6, pady=2)
    
    
    def setupOptionsPanel(self):
        Tkinter.Label(self.root, text="Configure:",
                      font=FONT).grid(row=1, column=0, padx=4, pady=2, sticky=E)
        b = Tkinter.Button(self.root, image=self._propertiesIMG,
                       command=self.configureOptions)
        bindButtonImages(b, self._propertiesIMG, self._propertiesIMG_H, "Configure Movpy Command Line Options")
        b.grid(row=1, column=1, padx=4, pady=2)
        Tkinter.Label(self.root, text="Options:",
                      font=FONT).grid(row=2, column=0, padx=4, pady=2, sticky=E)
        #
        self.optionStore = {}
        self.checks = {}
        frame = Tkinter.Frame(self.root)
        for opt, tip in (('f', 'Run in Script Dir'), ('p', 'Psyco On'),
                         ('b', 'Pause After Run'), ('i', 'Inspect After Run')):
            self.optionStore[opt] = Tkinter.IntVar()
            self.checks[opt] = Tkinter.Checkbutton(frame, text=opt,
                                                   variable=self.optionStore[opt],
                                                   font=FONT)
            createCallTip(self.checks[opt], tip)
            self.checks[opt].pack(side=Tkinter.LEFT)
        frame.grid(row=2, column=3, columnspan=3, padx=10, ipadx=10, sticky=W)
    
    
    def setupQuickLaunchPanel(self):
        self._quickLaunchData = {}
        self._quickButtons = {}
        f = Tkinter.Frame(self.root)
        for i in range(8):
            i += 1
            self._quickLaunchData[i] = {
                'filename': '',
                'args': '',
                'use_args': True,
                'options': dict([(option[1:], False) for option in the_options]),
                'name': 'Quick Launch %s' % i,
            }
            #
            def launch(event=None, i=i):
                self.quickLaunch(i)
            b = Tkinter.Button(f, text=(" %s " % (i)),
                           font=FONT,
                           command=launch
                           )
            b.grid(row=0, column=i-1, padx=8, pady=7)
            self._quickButtons[i] = b
            self.root.bind(('<F%s>' % i), launch)
        #
        f.grid(row=3, column=0, columnspan=8, sticky=E+W)
    
    
    def setupMenu(self):
        menubar = Tkinter.Menu(self.root)
        #
        filemenu = Tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Choose", command=self.chooseScript)
        filemenu.add_command(label="Launch", command=self.launchScript)
        ## FIXME: add recent files
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        #
        options = Tkinter.Menu(menubar, tearoff=0)
        options.add_command(label="Options", command=self.configureOptions)
        options.add_command(label="Current Directory", command=self.chooseDirectory)
        options.add_command(label="Choose IDE", command=self.chooseIDE)
        options.add_command(label="Quick Launch", command=self.configureQuickLaunch)
        options.add_command(label="Interpreters", command=self.configureInterpreter)
        options.add_command(label="Logging", command=self.configureLogging)
        menubar.add_cascade(label="Configure", menu=options)
        #
        self._consoleVar = Tkinter.IntVar()
        console = Tkinter.Menu(menubar, tearoff=0)
        console.add_radiobutton(label="Normal", value=0, variable=self._consoleVar)
        console.add_radiobutton(label="Console On", value=1, variable=self._consoleVar)
        console.add_radiobutton(label="Console Off", value=2, variable=self._consoleVar)
        menubar.add_cascade(label="Console", menu=console)
        #
        self._interpreterVar = Tkinter.IntVar()
        self._interpreterMenu = Tkinter.Menu(menubar, tearoff=0)
        self._interpreterMenu.add_radiobutton(label="Default", value=0,
                                              variable=self._interpreterVar,
                                              command=self.saveInterpreterData)
        menubar.add_cascade(label="Interpreter", menu=self._interpreterMenu)
        #
        self._logVar = Tkinter.IntVar()
        logging = Tkinter.Menu(menubar, tearoff=0)
        logging.add_radiobutton(label="Logging Off", variable=self._logVar, value=0,
                                command=self.setLogMode)
        logging.add_radiobutton(label="Logmode Write", variable=self._logVar, value=1,
                                command=self.setLogMode)
        logging.add_radiobutton(label="Logmode Append", variable=self._logVar, value=2,
                                command=self.setLogMode)
        menubar.add_cascade(label="Log Mode", menu=logging)
        #
        help = Tkinter.Menu(menubar, tearoff=0)
        help.add_command(label="About", command=self.launchAbout)
        help.add_command(label="Docs", command=self.launchDocs)
        help.add_command(label="Website", command=self.launchWebsite)
        help.add_command(label="Mailing List", command=self.launchMailingList)
        help.add_command(label="Shop", command=self.launchShop)
        menubar.add_cascade(label="Help", menu=help)
        #
        self.root.config(menu=menubar)
    
    
    def setupInterpreterMenu(self):
        if self._interpreterMenuItems:
            self._interpreterMenu.delete(0, self._interpreterMenuItems - 1)
        numItems = len(self._interpreterData)
        for i in range(numItems):
            name, _ = self._interpreterData[i]
            self._interpreterMenu.insert_radiobutton(i, label=name, value=i + 1,
                                                     variable=self._interpreterVar,
                                                     command=self.saveInterpreterData)
        self._interpreterMenuItems = numItems
        setInterpreter = self._interpreterVar.get()
        if setInterpreter > numItems:
            self._interpreterVar.set(numItems)
        else:
            self._interpreterVar.set(setInterpreter)
    
    
    def loadInitialDirectory(self):
        self.dir_file = joinPaths(configdir, 'initial_directory.txt')
        if os.path.isfile(self.dir_file):
            self.dir = open(self.dir_file).read().strip() or os.getcwd()
            # initial_directory is stored as relative path to the movpydir
            self.dir = joinPaths(movpydir, self.dir)
            if not os.path.isdir(self.dir):
                self.dir = os.getcwd()
            else:
                self.dir = os.path.abspath(self.dir)
        else:
            self.dir = os.getcwd()


    def loadWorkingDirectory(self):
        self.working_dir = ''
        self.working_dir_file = joinPaths(configdir, 'working_directory.txt')
        if os.path.isfile(self.working_dir_file):
            working_dir = open(self.working_dir_file).read().strip()
            # initial_directory is stored as relative path to the lib
            # directory
            if working_dir and os.path.isdir(os.path.abspath(joinPaths(movpydir,
                                                                       working_dir))):
                self.working_dir = working_dir
    
    
    def loadQuickLaunchConfig(self):
        self._quickConfigFile = joinPaths(configdir, 'quicklaunch.txt')
        if not os.path.isfile(self._quickConfigFile):
            # NOTE: Fails silently ??
            line_list = [''] * 40
        else:
            line_list = [l.strip() for l in open(self._quickConfigFile).readlines()]
        #
        if len(line_list) != 40:
            # File is corrupted
            sys.stderr.write('"quicklaunch.txt" has %s lines. Needs 40.\n'
                             % len(line_list))
            tkMessageBox.showerror('Quick Launch File Error', "Quick "
                "Launch data file corrupted :\n\"%s\"." % (self._quickConfigFile))
            return
        #
        for i in range(8):
            values = self._quickLaunchData[i + 1]
            index = i * 5
            values['name'] = line_list[index] or ('Quick Launch %s' % (i + 1))
            values['filename'] = line_list[index + 1]
            values['args'] = line_list[index + 2]
            values['use_args'] = line_list[index + 3].lower() == 'yes'
            #
            options = dict([(option[1:], False) for option in the_options])
            settings = line_list[index + 4].strip()
            if settings:
                settingList = settings.split(' ')
                for opt in settings:
                    if not opt or opt == 'o':
                        continue
                    # FIXME: error handling for invalid options
                    options[opt] = True
            values['options'] = options
            #
        self.setupQLButtonState()
    
    
    def setupQLButtonState(self):
        for i in range(8):
            i += 1
            button = self._quickButtons[i]
            vals = self._quickLaunchData[i]
            if not vals['filename']:
                button.config(state=DISABLED)
            else:
                button.config(state=NORMAL)
                createCallTip(button, vals['name'])
    
    
    def loadOptions(self):
        self.options = dict([(option[1:], False) for option in the_options])
        self._configFile = joinPaths(configdir, 'config.txt')
        if not self._commandLineOptions['o']:
            optionlist = []
            if os.path.isfile(self._configFile):
                optionlist = remcom(self._configFile)
            for opt in optionlist:
                if not opt in the_options:
                    # NOTE: should we raise a dialog here ?
                    sys.stderr.write('Unkown option "%s" in "config.txt".' % opt)
                    continue
                self.options[opt[1:]] = True
        #
        self.options.update(dict([(key, value) for (key, value) in
            self._commandLineOptions.items() if value]))
        #
        for opt in self.optionStore:
            if self.options[opt]:
                self.optionStore[opt].set(1)
    
    
    def loadIDE(self):
        self._ideFile = joinPaths(configdir, 'ide.txt')
        self._ideExecutable = 'lib/pythonwin/PythonwinIDE.py'
        self._ideArgs = ''
        if os.path.isfile(self._ideFile):
            linelist = open(self._ideFile).read().splitlines()
            if len(linelist) not in (1, 2):
                # FIXME: dialog ?
                sys.stderr.write('Corrupted "ide.txt" file.')
            else:
                self._ideExecutable = linelist[0]
                if len(linelist) == 2:
                    self._ideArgs = linelist[1]
    
    
    def loadLogging(self):
        self._logConfigFile = joinPaths(configdir, 'logging.txt')
        self._logMode = None
        self._logFile = 'lib/config/logs/{DATE}-{TIME}-{FILE}.txt'
        if os.path.isfile(self._logConfigFile):
            linelist = open(self._logConfigFile).read().splitlines()
            if not linelist:
                pass
            elif linelist[0] not in ('', 'w', 'a'):
                # FIXME: dialog ?
                sys.stderr.write('Corrupted "logging.txt" file.')
            else:
                self._logMode = linelist[0] or None
                if len(linelist) == 1:
                    linelist.append('')
                self._logFile = linelist[1]
        if self._commandLineOptions['l']:
            self._logMode = self._commandLineOptions['logmode']
            self._logFile = self._commandLineOptions['logfile']
        self._logVar.set(_LOG_MODE[self._logMode])
    
    
    def loadConsole(self):
        if self.options['k']:
            self._consoleVar.set(1)
        elif self.options['koff']:
            self._consoleVar.set(2)
        else:
            self._consoleVar.set(0)
    
    
    def loadInterpreters(self):
        self._interpreterMenuItems = None
        self._interpreterData = []
        self._interpreterFile = joinPaths(configdir, 'interpreters.txt')
        index = 0
        if os.path.isfile(self._interpreterFile):
            raw_data = open(self._interpreterFile).read().splitlines()
            try:
                index =int(raw_data[0])
            except ValueError:
                index = 0
            else:
                raw_data.pop(0)
            if len(raw_data) % 2:
                raw_data.append('')
            for i in range(0, len(raw_data), 2):
                self._interpreterData.append((raw_data[i], raw_data[i + 1]))
        #
        self._interpreterVar.set(index)
    
    
    def quit(self, event=None):
        self.root.destroy()
    
    
    def getDirectory(self):
        if self.working_dir:
            return os.path.abspath(joinPaths(movpydir, self.working_dir))
        return os.getcwd()
    
    
    def launchInterpreter(self):
        menuSelection = self._interpreterVar.get()
        if menuSelection == 0:
            intPath = sys.executable
        else:
            index = menuSelection - 1
            intPath = os.path.abspath(joinPaths(movpydir, self._interpreterData[index][1]))
        #
        intPath, args = unQuote(intPath)
        filename = ''
        script_args = ''
        if isExecutableFile(intPath):
            intPath = getConsoleExe(intPath)
        else:
            filename = intPath
            intPath = getConsoleExe(sys.executable)
            script_args = args
        #
        directory = self.getDirectory()
        args = ''
        if isMovpy(intPath):
            args = '-'
            if self.options['IPOFF']:
                args = '-IPOFF ' + args
        self.launch(filename, intPath, os.getcwd(), args, script_args, False)
        # (filename, executable, directory, executable_args, script_args, force_break)
    
    
    def chooseScript(self):
        filename = fileDialog("Choose a Python Script...", joinPaths(movpydir, self.dir))
        if not filename:
            return
        filePath = relpath(movpydir, filename)
        self.updateFileHistory(filePath)
        self.dir = relpath(movpydir, os.path.dirname(filename))
        try:
            open(self.dir_file, 'w').write(self.dir)
        except (IOError, OSError):
            # ignore write fails - e.g. on a CD
            # QUESTION: raise an alert ?
            pass
        self._chooseScript.setentry(filePath)
    
    
    def launchScript(self):
        filename = fileDialog("Launch a Python Script...", joinPaths(movpydir, self.dir))
        if not filename:
            return
        filePath = relpath(movpydir, filename)
        self.dir = relpath(movpydir, os.path.dirname(filename))
        try:
            open(self.dir_file, 'w').write(self.dir)
        except (IOError, OSError):
            # ignore write fails - e.g. on a CD
            # QUESTION: raise an alert ?
            pass
        self.runfile(filename)
    
    
    def runScript(self, event=None):
        filename = self._chooseScript.get()
        if not filename:
            return
        self.updateFileHistory(filename)
        self.saveFileHistory()
        #
        self.runfile(filename)
    
    
    def updateFileHistory(self, filename):
        if filename in self._list:
            self._list.remove(filename)
        self._list = ([filename] + self._list)[:20]
        self._chooseScript.component('scrolledlist').setlist(self._list)
    
    
    def saveFileHistory(self):
        try:
            open(self._fileHistoryFile, 'w').write('\n'.join(self._list))
        except (IOError, OSError):
            pass
    
    
    def configureOptions(self):
        configOptionsWin = Tkinter.Toplevel(self.root)
        configOptionsWin.title("Configure Options")
        #configOptionsWin.geometry("680x380")
        configOptionsWin.protocol("WM_DELETE_WINDOW", configOptionsWin.destroy)
        configOptionsWin.resizable(0, 0)
        configOptionsWin.geometry("+%d+%d" % (self.root.winfo_rootx()+50,
                                  self.root.winfo_rooty()+50))
        #
        l = Tkinter.Label(configOptionsWin, text=CFGOPTLBL, font=FONT)
        createCallTip(l, CFGOPTTIP)
        l.grid(row=0, column=0, columnspan=4, padx=10, pady=7)
        optDir = {}
        options = (
                    ('f', 'Run in Script Dir'), 
                    ('i', 'Inspect After Run'),
                    ('p', 'Psyco On'),
                    ('u', 'Unbuffered'),
                    ('b', 'Pause After Script'),
                    ('IPOFF', 'IPython Off'),
                    ('x', 'Skip First Line'),
        )
        i = 0
        for opt, text in options:
            optDir[opt] = Tkinter.IntVar()
            c = Tkinter.Checkbutton(configOptionsWin, variable=optDir[opt],
                                    text='-%s: %s' % (opt, text),
                                    font=FONT2)
            c.grid(row=(i/3)+1, column=i%3, padx=4, pady=2, sticky=W)
            i += 1
            if opt in self.optionStore:
                # GUI first
                optDir[opt].set(self.optionStore[opt].get())
            else:
                optDir[opt].set(int(self.options[opt]))
        #
        f = Tkinter.Frame(configOptionsWin)
        Tkinter.Label(f, text='Console: ', font=FONT2).pack(side=Tkinter.LEFT)
        consoleOpt = Tkinter.IntVar()
        b = Tkinter.Radiobutton(f, variable=consoleOpt, value=0,
                            text='Normal',
                            font=FONT2)
        b.pack(side=Tkinter.LEFT)
        createCallTip(b, "Console On for '.py', Off for '.pyw'")
        b = Tkinter.Radiobutton(f, variable=consoleOpt, value=1,
                            text='On',
                            font=FONT2)
        createCallTip(b, "Console On")
        b.pack(side=Tkinter.LEFT)
        b = Tkinter.Radiobutton(f, variable=consoleOpt, value=2,
                            text='Off',
                            font=FONT2)
        createCallTip(b, "Console Off")
        b.pack(side=Tkinter.LEFT)
        f.grid(row=3, column=1, columnspan=2, padx=4, pady=2)
        consoleOpt.set(self._consoleVar.get())
        #
        # Ok, Save, Cancel
        def ok(end=True):
            for opt, var in optDir.items():
                self.options[opt] = bool(var.get())
                if opt in self.optionStore:
                    self.optionStore[opt].set(var.get())
            self._consoleVar.set(consoleOpt.get())
            if end:
                configOptionsWin.destroy()
        def save():
            ok(end=False)
            try:
                h = open(self._configFile, 'w')
            except (IOError, OSError):
                tkMessageBox.showerror('Config File Error', "Couldn't save "
                    "config file :\n\"%s\"." % (self._configFile))
                sys.stderr.write("Can't save config file.\n")
            else:
                console = {0: '', 1: '-k\n', 2:'-koff\n'}
                for opt in optDir:
                    val = self.options[opt]
                    if val:
                        h.write('-%s\n' % opt)
                h.write(console[consoleOpt.get()])
                h.close()
            configOptionsWin.destroy()
        #
        b = Tkinter.Button(configOptionsWin, text=" OK ",
               font=FONT,
               command=ok)
        b.focus()
        createCallTip(b, "Use these options without saving.")
        b.grid(row=4, column=0, padx=5, pady=7)
        b = Tkinter.Button(configOptionsWin, text="Save",
               font=FONT,
               command=save)
        createCallTip(b, "Use & Save.")
        b.grid(row=4, column=1, padx=5, pady=7)
        b = Tkinter.Button(configOptionsWin, text="Cancel",
               font=FONT,
               command=configOptionsWin.destroy)
        createCallTip(b, "Guess :-)")
        b.grid(row=4, column=2, padx=5, pady=7)
        #
        configOptionsWin.focus()
        # disable other windows while I'm open
        configOptionsWin.grab_set()
        configOptionsWin.lift()
        # and wait here until win destroyed
        configOptionsWin.wait_window()
    
    
    def quickLaunch(self, index):
        values = self._quickLaunchData[index]
        filename = values['filename']
        if not filename:
            return
        script_args = values['args']
        use_args = values['use_args']
        if not use_args:
            script_args = self._args.getvalue()
        filename = joinPaths(movpydir, filename)
        options = values['options']
        directory = os.getcwd()
        if options['f']:
            directory = os.path.dirname(filename)
        #
        if not isExecutableFile(filename):
            if options['k']:
                executable = getConsoleExe(sys.executable)
            elif options['koff']:
                executable = getNoConsoleExe(sys.executable)
            else:
                executable = getNormalExe(sys.executable, filename)
            executable_args, force_break = getExecutableArgs(executable, options)
            #
        else:
            executable = filename
            executable_args, force_break = getExecutableArgs(filename, options)
            filename = ''
            executable_args = executable_args + ' ' + script_args
            script_args = ''
        #
        self.launch(filename, executable, directory, executable_args, script_args, force_break)
    
    
    def configureQuickLaunch(self):
        ql = QuickLaunch(self.root, deepcopy(self._quickLaunchData))
        if not ql.save or ql.quickLaunchData == self._quickLaunchData:
            return
        self._quickLaunchData = ql.quickLaunchData
        self.saveQuickLaunchData()
        self.setupQLButtonState()
    
    
    def saveQuickLaunchData(self):
        try:
            h = open(self._quickConfigFile, 'w')
        except (IOError, OSError):
            # FIXME: dialog or write to sys.stderr ?
            return
        for i in range(8):
            values = self._quickLaunchData[i + 1]
            use_args = ''
            if values['use_args']:
                use_args = 'yes'
            index = i * 5
            h.write(values['name'] + '\n')
            h.write(values['filename'] + '\n')
            h.write(values['args'] + '\n')
            h.write(use_args + '\n')
            h.write(' '.join([opt for (opt, val) in values['options'].items() if val]) + '\n')
        h.close()
    
    
    def chooseDirectory(self):
        directory = ChooseDirectory(self.root, self.working_dir).directory
        if directory != self.working_dir:
            self.working_dir = directory
            try:
                open(self.working_dir_file, 'w').write(directory)
            except (IOError, OSError):
                # FIXME: passes without notice
                pass
    
    
    def configureLogging(self):
        logMode, logFile = showConfigureLogging(self.root, self._logFile, self._logMode)
        if (logFile, logMode) == (self._logFile, self._logMode):
            return
        self._logFile = logFile
        self._logMode = logMode
        self._logVar.set(_LOG_MODE[self._logMode])
        self.saveLogging()
    
    
    def saveLogging(self):
        try:
            h = open(self._logConfigFile, 'w')
        except (OSError, IOError):
            # FIXME: dialog ?
            pass
        else:
            h.write((self._logMode or '') + '\n')
            h.write(self._logFile + '\n')
            h.close()
    
    
    def setLogMode(self):
        newMode = _MODE_FROM_VAL[self._logVar.get()]
        if newMode == self._logMode:
            return
        self._logMode = newMode
        self.saveLogging()
    
    
    def configureInterpreter(self):
        ci = ConfigureInterpreter(self.root, copy(self._interpreterData))
        if not ci.save or ci.interpreterData == self._interpreterData:
            return
        self._interpreterData = ci.interpreterData
        self.setupInterpreterMenu()
        self.saveInterpreterData()
    
    
    def saveInterpreterData(self):
        outData = [str(self._interpreterVar.get())]
        for interpreter in self._interpreterData:
            outData.extend(interpreter)
        try:
            open(self._interpreterFile, 'w').write('\n'.join(outData))
        except (IOError, OSError):
            # FIXME: Message ?
            pass
    
    
    def launchAbout(self):
        AboutDialog(self.root, self._version)
    
    
    def chooseIDE(self):
        ci = ChooseIDE(self.root, self._ideExecutable, self._ideArgs)
        if not ci.save:
            return
        path, args = (ci.IDEPath, ci.args)
        if (path, args) == (self._ideExecutable, self._ideArgs):
            return
        self._ideExecutable = ci.IDEPath
        self._ideArgs = ci.args
        try:
            open(self._ideFile, 'w').write('%s\n%s' % (path, args))
        except (IOError, OSError):
            # FIXME: 
            pass
    
    
    def launchIDE(self):
        # No options for IDE - so no console
        executable = self._ideExecutable
        if not executable:
            return
        force_break = False
        executable = joinPaths(movpydir, executable)
        script_args = self._ideArgs
        executable, executable_args = unQuote(executable)
        directory = self.getDirectory()
        if isPythonFile(executable):
            filename = executable
            script_args = executable_args
            executable = getNoConsoleExe(sys.executable)
            executable_args = ''
        else:
            filename = ''
            executable_args = executable_args + ' ' + script_args
            script_args = ''
        self.launch(filename, executable, directory, executable_args, script_args, force_break)
        # (filename, executable, directory, executable_args, script_args, force_break)
    
    
    def launchDocs(self):
        d = os.path.join(docdir, 'reference/index.html')
        if not os.path.isfile(d):
            d = os.path.join(movpydir, '../docs_html/reference/index.html')
        if not os.path.isfile(d):
            d = aboutPage
        else:
            d = 'file://' + d.replace('\\', '/')
        openbrow(d)
    
    
    def launchWebsite(self):
        openbrow(website)
    
    
    def launchShop(self):
        openbrow(shop)
    
    
    def launchMailingList(self):
        openbrow(mailingList)
    
    
    def runfile(self, filename):
        menuSelection = self._interpreterVar.get()
        if menuSelection == 0:
            intPath = sys.executable
        else:
            index = menuSelection - 1
            intPath = os.path.abspath(joinPaths(movpydir, self._interpreterData[index][1]))
        #
        intPath, intArgs = unQuote(intPath)
        intPath = getConsoleExe(intPath)
        directory = self.getDirectory()
        console = self._consoleVar.get()
        if console == 0:
            intPath = getNormalExe(intPath, filename)
        elif console == 1:
            intPath = getConsoleExe(intPath)
        elif console == 2:
            intPath = getNoConsoleExe(intPath)
        #
        filePath, fileArgs = unQuote(filename)
        filePath = os.path.abspath(joinPaths(movpydir, filePath))
        if isExecutableFile(filePath):
            intPath = ''
            intArgs = ''
        scriptArgs = self._args.getvalue()
        if self.optionStore['f'].get():
            directory = os.path.dirname(filePath)
        options = {}
        for opt, val in self.options.items():
            if opt in ('f', 'k', 'koff', ''):
                continue
            if opt in self.optionStore:
                val = self.optionStore[opt].get()
            options[opt] = val
        extra_intArgs, force_break = getExecutableArgs(intPath, options)
        # 0, 1, 2 - off, write, append
        logMode = self._logMode
        logFile = joinPaths(movpydir, self._logFile)
        if logMode and isMovpy(intPath):
            extra_intArgs += ' -l%s "%s"' % (logMode, logFile)
        intArgs = intArgs + ' ' + extra_intArgs
        #
        self.launch(filePath, intPath, directory, intArgs, scriptArgs, force_break)
    
    
    def launch(self, filename, executable, directory, executable_args, script_args, force_break):
        if filename and not os.path.isfile(filename):
            tkMessageBox.showerror('File Error', 'File "%s" Does Not Exist.' % filename)
            return
        if executable and not os.path.isfile(executable):
            tkMessageBox.showerror('File Error', 'Interpreter "%s" Not Found.' % executable)
            return
        if not WIN98:
            if ' ' in filename:
                filename = '"%s"' % filename
            if ' ' in executable:
                if ' ' in filename:
                    executable = GetShortPathName(executable)
                else:
                    executable = '"%s"' % executable
            if ' ' in directory:
                directory = '"%s"' % directory
            if force_break:
                force_break = 'cmd /K '
            else:
                force_break = ''
            cmd = ('start "Movable Python - Press Ctrl+Break to stop" '
                   '/D%s %s%s %s %s %s' % (directory, force_break, executable,
                                           executable_args, filename,
                                           script_args)
                  )
        else:
            if filename:
                filename = GetShortPathName(filename)
            executable = GetShortPathName(executable)
            directory = GetShortPathName(directory)
            if force_break:
                force_break = 'command /K '
            else:
                force_break = ''
            cmd = ('start "Movable Python - %s - Press Ctrl+Break to stop" '
                   '/D%s %s%s %s %s %s' % (directory, executable, force_break,
                                           executable_args, filename,
                                           script_args)
                )
        if TEST:
            print cmd
        os.system(cmd)
        if self.expired:
            self.d = SharewareDialog(self.root, self.expired)


if __name__ == '__main__':
    options = dict([(option[1:], False) for option in the_options])
    for opt in ('o', 'l'):
        options[opt] = False
    #
    app = MovpyGetFile(options, '2.0.0 Preview', None)
    Tkinter.mainloop()

