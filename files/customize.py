#### customize.py
#### Part of Movable Python
#### http://www.voidspace.org.uk/python/movpy/

# This script is not a standalone script,
# It is run by movpy.exe (and movpyw.exe)
# It executes inside the movpy namespace/environment.

# edit this to customise (or diagnose) the environment your scripts run in.

"""
There is a module called 'movpy' which has lots of useful values.

The movpy module defines the following names.

* filename = the path to the script we are running
* filedir = the directory that script is in
* movpydir = the directory of the movpy executable
* curdir = the cwd from which we have been called
* libdir = the 'lib' directory that modules/packages are contained in
* commandline != '' if '-c' was passed
* go_interactive = True if '-i' was set.
* interactive = True if we are in an interactive session
* interactive_mode is a function to enter interactive mode 

    interactive_mode(localvars=None, globalvars=None, IPOFF=False, argv=None)

* movpyw = True if we are running under movpyw rather than movpy
"""

import sys
import movpy

# add a couple of paths to sys.pth
if not movpy.movpydir in sys.path:
    sys.path.append(movpy.movpydir)
if not movpy.curdir in sys.path:
    sys.path.append(movpy.curdir)

# Note: If you want to use the win32 extensions here, uncomment the following line
## del sys.frozen

del sys
del movpy

"""

CHANGELOG
=========

2006/10/03
----------

Now use the 'movpy' module.


2005/11/03
----------

This file *no longer* changes the current directory.

"""
