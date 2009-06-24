# **version**

#*** replace imports **

import sys
import os
import traceback

if hasattr(sys, 'frozen') and (sys.frozen == "windows_exe"):
    # get rid of the error box
    sys.stderr = sys.stdout

##sys.frozen = ##
__version__ = '**version**'


######################################

args = sys.argv[1:]
if args and args[0] == '-c':
    del sys.argv[1:3]
    exec args[1]
    sys.exit()

######################################
# Some general stuff

if False:
    # fake for py2exe which misses these modules
    # doesn't matter if these imports would fail or not :-)
    import unicodedata
    import winsound

#########################################

# to be filled in by PyDistFreeze
sys.winver = '**winver**'

try:
    import idlelib.PyShell
except ImportError:
    # IDLE is not installed, but maybe PyShell is on sys.path:
    try:
        import PyShell
    except ImportError:
        raise
    else:
        import os
        idledir = os.path.dirname(os.path.abspath(PyShell.__file__))
        if idledir != os.getcwd():
            # We're not in the IDLE directory, help the subprocess find run.py
            pypath = os.environ.get('PYTHONPATH', '')
            if pypath:
                os.environ['PYTHONPATH'] = pypath + ':' + idledir
            else:
                os.environ['PYTHONPATH'] = idledir
        PyShell.main()
else:
    idlelib.PyShell.main()
