# **version**
#### Movable Python
#### movpy.py

# This script becomes the executable part of portable Python distributions.

# Homepage : http://www.voidspace.org.uk/python/movpy/
# Download from : http://voidspace.tradebit.com

# Copyright Michael Foord, 2004-2006.
# Commercial software.

# For information about bugfixes, updates and support, 
# or for bug reports and feature requests - join the movpy mailing list.
# http://groups.google.com/group/movpy/
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

#*** replace imports **

import atexit
import sys
import os
import traceback
import __builtin__
from _pathutils import get_main_dir
from movpy_tools import *
from _standout import StandOut
from command_line import get_config, parse_options, warning

# So we can check if we are in a Movable Python environment
if hasattr(sys, 'frozen') and hasattr(sys, 'movpy'):
    del sys.movpy
    del sys.frozen
elif hasattr(sys, 'frozen') or sys.version_info[:2]:
    sys.movpy = True

if len(sys.argv) > 1:
    if sys.argv[1] == 'testMJF':
        sys.movpy = 'test'
        del sys.argv[1]


if hasattr(sys, 'frozen') and (sys.frozen == "windows_exe"):
    # get rid of the error box
    sys.stderr = sys.stdout
    if (len(sys.argv) > 1) and (sys.argv[1] == 'testMJF'):
        def excepthook(type, value, traceback):
            errorFile = open(os.path.join(get_main_dir(), 'error.txt'), 'a')
            import traceback
            traceback.print_tb(traceback, file=errorFile)
        sys.excepthook = excepthook
        del excepthook


import movpy
from movpyLogging import getLogFileName, writeHeader
from movpy import movpydir, libdir


##sys.frozen = ##
__version__ = '**version**'


######################################

def check_expired(expire):
    """Compare current date with expiry date."""
    if not expire:
        return False
    import time
    if time.time() > expire:
        return True
    else:
        return False

def display_expired(expire):
    try:   
        import Tkinter
    except ImportError:
        print 'This demo version of Movable Python Has Expired.'
        print 'Visit http://voidspace.tradebit.com/groups.php'
    else:
        import Tkinter
        from movpySharewareDialog import ExpiredDialog
        #
        root = Tkinter.Tk()
        #
        d = ExpiredDialog(root, __version__)
        Tkinter.mainloop()
    #
    sys.exit(1)

## change to True to enable shareware test
shareware = False

if not shareware:
    valid = None
else:
    # Valid from 6th October - for 160 days
    valid = 1191679775 + (210*24*3600)

if (shareware and check_expired(valid)):
    # Is this an expired shareware version
    display_expired(valid)

######################################
# Some general stuff

if False:
    # fake for py2exe which misses these modules
    # doesn't matter if these imports would fail or not :-)
    import unicodedata
    import winsound
    # gets missed from recent versions of IPython
    import IPython.hooks
    # to ensure inclusion for docutils :-)
    import roman

#########################################

if sys.version_info[:2] > (2, 2):
    from zip_imp import patch
    patch()

#########################################

movpyw = False
try:
    if sys.frozen.lower() == 'windows_exe':
        # it prevents interactive mode when run from the console-less version,
        # unless you insist with '-' !
        movpyw = True
except AttributeError:
    # allows testing from the source (sys.frozen only exists in executable)
    if sys.executable.endswith('pythonw.exe'):
        movpyw = True

# to be filled in by PyDistFreeze
movversion = '#*** replace version **'
sys.winver = '**winver**'

# new modules can be located in the lib directory
sys.path.insert(0, libdir)
_setlibdir(libdir)

if not os.environ.setdefault('PATH', '').endswith(libdir):
    os.environ['PATH'] += (';' + libdir)

# paths to add to sys.path, relative to the libdir
if os.path.isfile(os.path.join(libdir, 'syspaths.pth')):
    thepaths = remcom(os.path.join(libdir, 'syspaths.pth'))
    for entry in thepaths:
        thispath = os.path.abspath(os.path.join(libdir, entry))
        if not thispath in sys.path:
            sys.path.append(thispath)

# paths to add to sys.path, relative to the libdir - used by packages
if os.path.isfile(os.path.join(libdir, 'packagepaths.pth')):
    thepaths = remcom(os.path.join(libdir, 'packagepaths.pth'))
    for entry in thepaths:
        thispath = os.path.abspath(os.path.join(libdir, entry))
        if not thispath in sys.path:
            sys.path.append(thispath)

# special for 'wx.pth' which needs to exist for wxversion
if os.path.isfile(os.path.join(libdir, 'wx.pth')):
    thepaths = remcom(os.path.join(libdir, 'wx.pth'))
    for entry in thepaths:
        thispath = os.path.abspath(os.path.join(libdir, entry))
        if not thispath in sys.path:
            sys.path.append(thispath)

IPOFF = False
xon = False
Tkinter = None
commandline = None
go_interactive = False
interactive = False
pylab = False
CHANGEDIR = False
PSYCOON = 0
psyco = None
pause = False
run_module = False

try:
    options = parse_options(movversion)
except ValueError, e:
    sys.stderr.write(str(e))
    sys.stderr.write(warning)
    # FIXME: might we want to enter itneractive mode here ?
    sys.exit(1)

if options['config']:
    movpy.configdir = options.pop('config')

try:
    config_options = get_config(os.path.join(movpy.configdir, 'config.txt'))
except ValueError:
    # FIXME: is this a good enough way to handle errors ?
    if not movpyw:
        sys.stderr.write(('Unrecognised option "%s" in config.txt.\n'
            % entry))

######################################

if 'm' in options:
    run_module = True
    del options['m']


## k is still in options
## koff is still in options

if 'c' in options:
    commandline = options['c']
    del options['c']

if not options['o']:
    # NOTE: Only use config options if '-o' isn't set
    options.update(config_options)

if len(sys.argv) == 1 and not commandline:
    try:
        import Tkinter
        import Pmw
    except ImportError:
        sys.stderr.write(("Tkinter or Pmw can't be found and no filename was "
            "specified.\n"))
        sys.exit(1)
    else:
        from movpyGUI import MovpyGetFile
    #
    app = MovpyGetFile(options, __version__, valid)
    Tkinter.mainloop()
    sys.exit()
    #
elif not commandline:
    if sys.argv[1] == '-':
        interactive = True
        filename = sys.executable
        del sys.argv[1]
    elif sys.argv[1] == '-pylab':
        interactive = True
        pylab = True
        filename = sys.executable
        del sys.argv[1]
    else:
        filename = sys.argv[1]
        del sys.argv[1]
        if not os.path.isfile(filename) and (not run_module):
            print "Specified file, <%s>, does not exist" % filename
            print "Try 'movpy -h' for help."
            sys.exit(1)
else:
    # only used if the commandline is used
    filename = '.'

# explicitly deleted to prevent access
del shareware, check_expired, display_expired


logMode = None
logFilename = None
if options['l'] and (filename not in ('.', sys.executable)):
    logMode = options['logmode']
    logFile = options['logfile']
    logFilename = getLogFileName(logFile, filename)
    try:
        h = open(logFilename, logMode)
    except (IOError, OSError):
        print 'dead'
        logMode = logFilename = None
    else:
        writeHeader(h, filename, logMode)
        h.close()
    del logFile
#
if logFilename or options['u']:
    standout = StandOut(logfile=logFilename, logmode='a', unbuffered=options['u'])
    atexit.register(standout.close)

if options['x']:
    xon = True
if options['f']:
    CHANGEDIR = True
if options['i']:
    if not movpyw:
        go_interactive = True
if options['IPOFF']:
    IPOFF = True
if options['b']:
    pause = True
if options['p'] and not interactive:
    try:
        import psyco
    except ImportError:
        pass
    else:
        psyco.full()
        from psyco.classes import *
        PSYCOON = 1
#
del options, logFilename, logMode

filedir = None
if filename != '.' and not run_module:
    filename = os.path.abspath(filename)
    filedir = os.path.dirname(filename)
    # file directory first in sys.path
    sys.path.insert(0, filedir)

curdir = os.path.abspath(".")
__file__ = filename
sys.argv = [filename] + sys.argv[1:]

#################################
# setup the namespace

import imp
# m is a reference to the current __main__ module, to stop it being garbage collected
m = sys.modules['__main__']
module = imp.new_module('__main__')
namespace = module.__dict__

movpy.__version__ = __version__
movpy.interactive = interactive
movpy.movpyw = movpyw
movpy.filename = filename
movpy.curdir = curdir
movpy.go_interactive = go_interactive

namespace['__name__'] = '__main__'
namespace['__builtin__'] = __builtin__
namespace['__builtins__'] = __builtins__
namespace['__file__'] = __file__

namespace['__builtin__'].help = _Helper()
setquit(namespace)
setcopyright(namespace)

sys.modules['__main__'] = module

######################################

# additional file to run (run rather than imported)
if os.path.isfile(os.path.join(libdir, 'customize.py')):
    # any need to compile/exec this ?
    # FIXME: What about trapping errors here ?
    execfile(os.path.join(libdir, 'customize.py'), namespace)

if interactive:
    # FIXME: if this is run from movpyw.exe an error log is generated 
    #   perhaps deservedly so :-)
    #   alternative is to display a dialog
    sys.path.insert(0, movpydir)
    if pylab:
        launch_pylab()
    else:
        interactive_mode(namespace, IPOFF=(IPOFF or PSYCOON),
            argv=(sys.argv[1:] or None))
    sys.exit()

if CHANGEDIR and filedir:
    os.chdir(filedir)
del CHANGEDIR

if xon:
    handle = open(filename)
    commandline = handle.read()
    handle.close()
    x = commandline.find('\n')
    if x < len(commandline)-2:
        # we keep the '\n' so that line number reporting is correct
        commandline = commandline[x:]
    del x, handle

if run_module:
    try:
        codeobj = modulefinder(filename)
    except ValueError:
        print 'Failed to run module "%s".' % filename
        sys.exit(1)
    except SyntaxError:
        traceback.print_exc()
        codeobj = None
    #
    # dummy for later
    fname = ''
elif not commandline:
    handle = open(filename, 'rb')
    commandline = handle.read()
    handle.close()
    if not filename[-3:] in ('pyo', 'pyc'):
        commandline = commandline.replace('\r\n', '\n') + '\n'

del modulefinder

if not run_module:
    # we need to pass a name to compile
    if filename == '.':
        fname = '<string>'
    else:
        fname = os.path.split(filename)[1]
    #
    codeobj = None
    if not filename[-3:] in ('pyo', 'pyc'):
        #
        try:
            codeobj = compile(commandline, fname, 'exec')
        except Exception:
            # print any error without bombing out - probably a syntax error
            traceback.print_exc()
    else:
        import marshal
        try:
            codeobj = marshal.loads(commandline[8:])
        except Exception:
            # print any error without bombing out - probably a syntax error
            traceback.print_exc(file=sys.stderr)
#
del commandline, fname, run_module

exitException = None
if codeobj:
    try:
        exec codeobj in namespace
    except SystemExit, exitException:
        pass
    except Exception:
        # print any error without bombing out
        traceback.print_exc(file=sys.stderr)
    #
    del codeobj

if go_interactive:
    # enter the console with the current locals
    interactive_mode(namespace, IPOFF=(IPOFF or PSYCOON))
elif pause:
    raw_input('Hit Enter...')

if exitException:
    # Re-raise a system exit
    raise exitException
