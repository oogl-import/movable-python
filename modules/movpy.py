#### Movable Python
#### movpy.py

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
from _pathutils import get_main_dir
from movpy_tools import joinPaths

__all__ = (
    'movpydir',
    'libdir', 
    'docdir',
    'configdir',
    'filedir',
    'curdir',
    'go_interactive',
    'interactive',
    'interactive_mode',
)

movpydir = get_main_dir()
libdir = joinPaths(movpydir, 'lib')
docdir = joinPaths(movpydir, 'docs_html')
configdir = joinPaths(libdir, 'config')

if not hasattr(sys, 'movpy'):
    # Only works when
    libdir = joinPaths(movpydir, '../files')
    configdir = joinPaths(libdir, 'test_config')
    docdir = joinPaths(movpydir, 'docs_html')

filedir = None
curdir = None
interactive = False
__version__ = ''
go_interactive = False

# Moved to the end to avoid circular imports
from movpy_tools import interactive_mode
