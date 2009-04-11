# Movable IDLE


##################################################

import os
import sys
from StringIO import StringIO
from traceback import print_exc
import time
from pathutils import walkfiles, walkdirs, relpath, splitall, readlines

sys.path.append('files')
sys.path.insert(0, r'C:\Python24\Lib\idlelib')

# set current directory to the directory this script is in
os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
# doesn't work if run from IDLE
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'files', sys.version[:3]))

# Set the options
exclude_modules = ['pty', 'test', 'tzparse']

# in included packages, delete '.pyc' and '.pyo' files *if* the corresponding 
# '.py' file exists (reduces distribution size)
delete_pyc = True

# set to '' to disable logging
logfile = 'MovableIdleCompiler.log'

# should 0, 1, or 2 - for optimized bytecode files (only used if 
# extended_options is True - not used in Python 2.2)
optimize = 0

# should be 0 or 1 - 1 for a compressed library (only used if extended_options
# is True - not used in Python 2.2)
compress = 0

############################

version_num = '0.1.0'
version_date = '7th October 2006'
versionstring = 'Movable IDLE. Version %s, %s.' % (version_num,
    version_date)

#
# if py2exe crashes, try setting this to False
# (see the ISSUES.html file in the docs)
# FIXME: issues.html no longer exists
extended_options = True
##############################

# the different types of file we will attempt to import from.
# FIXME: What about '.pyd' ? (you can import from some, but attempting to
#   import from others causes core dumps)
module_extensions = ['.py', '.pyc', '.pyo',]
outfile =r'C:\Python24\Lib\idlelib\MovableIdleConsole.py'
outfile_win = r'C:\Python24\Lib\idlelib\MovableIdle.pyw'
mainfile = 'modules/MovableIdle.py'
pyversion = float(sys.version[:3])

# default directories to search for modules in 'Lib' and 'lib-tk'
libdirs = [os.path.join(sys.prefix, 'Lib'), os.path.join(sys.prefix,
    'Lib', 'lib-tk')]
get_win32 = True

filelist = ['files/unicows.dll']

#######################################################################
# support functions - mainly for dealing with paths

join = os.path.join
isdir = os.path.isdir
isfile = os.path.isfile

def delpyc(thisdir):
    """
    Delete all '.pyc' and '.pyo' files in a package dir, if the corresponding
    '.py' file exists.
    
    This reduces the size of precompiled distributions.
    """
    for thisfile in walkfiles(thisdir):
        if thisfile.endswith('.pyc') or thisfile.endswith('.pyo'):
            pyname = thisfile[:-3] + 'py'
            if os.path.isfile(pyname):
                os.remove(thisfile)

def remcom(fname):
    """A version of readlines that removes comments and strips lines."""
    return [line.strip() for line in readlines(fname) if line.strip()
        and not line.strip().startswith('#')]

#####################################
# support functions that actually do the work for PyDistFreeze

def getimports(libdir, basepackage=''):
    """Recursively find modules and subpackages."""
    global get_win32
    importlist = []
    if not os.path.isdir(libdir):
        return importlist
    for entry in os.listdir(libdir):
        if (entry.startswith('_') or '-' in entry or entry.count('.') > 1 or
            ' ' in entry):
            continue
        if os.path.isfile(libdir + '\\' + entry):
            if entry.endswith('.pth'):
                # this follow .pth files that python might not of course...
                print '\nPathfile found :', libdir + '\\' + entry, '\n'
                dirlist = readlines(libdir + '\\' + entry)
                for newdir in dirlist:
                    importlist += getimports(libdir + '\\' + newdir)
                continue
                # can import from .py, .pyc, and .pyo
            if not os.path.splitext(entry)[1] in module_extensions:
                continue
            entry = entry[:entry.find('.')]
            if basepackage:
                # for including modules and subpackages
                entry = basepackage + '.' + entry
            if entry in importlist or entry in exclude_modules:
                continue
            importlist.append(entry)
        elif os.path.isdir(libdir + '\\' + entry):
            if '.' in entry:
                continue
            if entry == 'win32com' and ('win32com' not in exclude_modules):
                # a hack to make sure we properly include win32com if necessary
                get_win32 = True
            if os.path.isfile(libdir + '\\' + entry + '\\__init__.py'):
                if basepackage:
                    thisentry = basepackage + '.' + entry
                else:
                    thisentry = entry
                if thisentry in importlist or thisentry in exclude_modules:
                    continue
                print 'Subpackage found :', thisentry
                importlist.append(thisentry)
                importlist += getimports(libdir + '\\' + entry, thisentry)
    return importlist

def getfullpath(exclude_curdir=True):
    """
    This returns all valid directories in ``sys.path`` - including following
    any '.pth' files.
    
    This is needed when manually searching for modules to add.
    """
    # FIXME: this function allows for '.pth' files anywhere on sys.path 
    #   this is more than is technically allowed... in practise unlikely to be
    #   a problem. But is it necessary anyway ? Isn't this just a cleaned up
    #   version of sys.path ? (directories that exist only)
    pathdirs = []
    for directory in sys.path:
        directory = os.path.abspath(directory)
        if not os.path.isdir(directory):
            continue
        if exclude_curdir and directory == os.path.abspath('.'):
            continue
        if directory in pathdirs:
            continue
        pathdirs.append(directory)
        for entry in os.listdir(directory):
            if not entry.endswith('.pth') or not os.path.isfile(entry):
                continue
            pthfile = readlines(os.path.join(directory, entry))
            for line in pthfile:
                if line[0] in '\'\"' and line[0] == line[-1]:
                    line = line[1:-1]
                fullline = os.path.join(directory, line)
                if os.path.isdir(fullline) and not fullline in pathdirs:
                    pathdirs.append(fullline)
    return pathdirs
            
####################################################

def main():
    global libdirs
    for path in getfullpath():
        if not 'site-packages' in path and path.startswith('c:\\Python24\\Lib'):
            libdirs.append(path)
    #
    print 'Directories we are searching : '
    print libdirs
    print
    #
    importlist = []
    for libdir in libdirs:
        # this searches the chosen directories for all modules
        importlist += getimports(libdir)
    #
    print '\nFound %s modules in total.' % len(importlist)
    theimports = ('# -*- coding: UTF-8 -*-\nif False:\n    import ' +
        '\n    import '.join(importlist))
    handle = open(mainfile)
    thecode = handle.read()
    thecode = thecode.replace('#*** replace imports **', theimports)
    thecode = thecode.replace('**version**', version_num)
    thecode = thecode.replace('#*** replace version **', versionstring)
    # inject in the real value of sys.winver
    thecode = thecode.replace('**winver**', sys.winver)
    win_thecode = thecode
    handle = file(outfile, 'w')
    handle.write(thecode)
    handle.close()
    # we save the script twice, once for the windows version...
    handle = file(outfile_win, 'w')
    handle.write(win_thecode)
    handle.close()
    print 'Done'
    print
    dobuild()


def dobuild():
    # solution from http://starship.python.net/crew/theller/moin.cgi/WinShell 
    # (only needed if we are importing win32)
    if get_win32:
        try:
            # does this work with Python 2.2  and py2exe 0.4.1 ?
            print 'Adding win32com path information.'
            print
            import modulefinder
            import win32com
            for p in win32com.__path__[1:]:
                modulefinder.AddPackagePath("win32com", p)
            for extra in ["win32com.shell", "win32com.mapi"]: 
                __import__(extra)
                m = sys.modules[extra]
                for p in m.__path__[1:]:
                    modulefinder.AddPackagePath(extra, p)
        except ImportError:
            # no build path setup, no worries.
            pass
    #
    from distutils.core import setup
    import py2exe
    import shutil
    #
    #  setup can be executed without command line...
    sys.argv.append("py2exe")
    sys.argv.append('--packages')
    sys.argv.append('encodings')
    #
    print 'Handing over to py2exe.'
    print 'Building distribution.'
    options = {'py2exe': {'dist_dir' : 'MovableIdle' }}
    if extended_options:
        options['py2exe']['excludes'] = exclude_modules
        options['py2exe']['compressed'] = compress
        options['py2exe']['optimize'] = optimize
        
    setup(
        console = [{
            'script': outfile,
            # anyone do an icon ?
            'icon_resources': [(1, 'files/movpy.ico')],
        }],
        windows = [{
            'script': outfile_win,
            # anyone do an icon ?
            'icon_resources': [(1, 'files/movpy.ico')],
        }],
        #
        version = version_num,
        description = ('Portable distribution of Idle ' +
            sys.version.split(" ")[0]),
        name = 'Movable Idle',
        author = 'Michael Foord',
        author_email = 'fuzzyman@voidspace.org.uk',
        url = 'http://www.voidspace.org.uk/python/movpy/',
        #
        data_files = [('', filelist)],
        zipfile = 'lib/library.zip',
        #
        options = options,
    )

    print
    print 'Distribution built.'
    #
    # remove the temporary file
    os.remove(outfile)
    # remove the temporary file
    os.remove(outfile_win)
    if os.path.isdir('build'):
        # and the temporary directory
        shutil.rmtree('build')


if __name__ == '__main__':
    from standout import StandOut

    stand = StandOut(logfile=logfile)
    #
    print versionstring
    print 'Building Distribution.'
    # for the logfile
    print time.ctime()
    print
    #
    try:
        main() 
    except Exception, e:
        # print any error without bombing out
        f = StringIO()
        print_exc(file=f)
        # write error to sys.stderr rather than printing to sys.stdout
        sys.stderr.write(f.getvalue()+'\n')
    stand.close()
