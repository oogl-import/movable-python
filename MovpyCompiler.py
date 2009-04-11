# Movable Python
# MovpyCompiler.py

# This script creates standalone, portable Python distributions.
# It needs py2exe and will work with Python 2.2, 2.3, 2.4 and 2.5

# Homepage : http://www.voidspace.org.uk/python/movpy/

# Written by : Michael Foord
# With input from :
#   Bruno Thoorens
#   Stani, the creator of SPE the Python IDE - http://spe.pycs.net

# Copyright Michael Foord, 2004-2005.
# Released with non-redistribution rights.
# Please see http://www.voidspace.org.uk/python/movpy/license.html

# For information about bugfixes, updates and support, please join the
# Movable Python mailing list.
# http://groups.google.com/group/movpy/
# Comments, suggestions and bug reports welcome.
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk


"""
This script searches for python modules.

It compiles the list in a script, in such a way that py2exe thinks we're
trying to import them. It then uses py2exe to build the distribution, and
cleans up the intermediate files.

The executable distribution that py2exe generates will run any script passed
to it as the first argument. Additional arguments are passed to the script,
which will 'feel' like it is running in a normal python environment.

This means you can build distributions for different versions of python
(2.2, 2.3, 2.4), and test your programs with them. (for backwards/forward
compatibility testing). It also allows running any python script on a machine
that doesn't have python installed. (Portable Python runtime environment).
"""

##################################################

from __future__ import generators
import os
import sys
from StringIO import StringIO
from traceback import print_exc
import time
from pathutils import walkfiles, walkdirs, relpath, splitall, readlines

RT_MANIFEST = 24

sys.path.append('files')

# FIXME: Need to copy idle for Python 2.2
# FIXME: Add firedrop.pyw and check templates
# FIXME: Add wx addons for Python 2.5
# FIXME: Create good standard config files and copy them

# for python 2.2
try:
    __file__
except NameError:
    __file__ = ''

# set current directory to the directory this script is in
os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
# doesn't work if run from IDLE
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'files', sys.version[:3]))

# Set the options
exclude_modules = ['pty', 'test', 'idle', 'idlelib', 'tzparse',
    'ctypes.com.samples', 'wx', 'wxPython', 'win32api', 'Pmw', 'pywin', 'pythonwin']

# extra modules that you explictly want to import as well
include_modules = ('psyco', 'readline', 'ctypes', 'wxversion', 'pythoncom')

# Actually build distribution ?
# (set to False to produce 'movpy.py' without building distribution)
build = True

# any whole packages (directories) to copy into the lib directory. 
# Package must be somewhere on sys.path. Names are case-sensitive
include_packages = ['Pmw', 'idlelib', 'wax', 'docutils',
    'pythonutils', 'enchant', 'Crypto', 'isapi', 'PIL', 'win32', 'win32com',
    'win32comext', 'firedrop2', 'pythonwin']

wx_packages = ['wx-2.8-msw-unicode', 'wx-2.6-msw-unicode', 'wx-2.5.3-msw-unicode']

if sys.version_info[:2] < (2, 3):
    include_packages.remove('Pmw')
    exclude_modules.remove('Pmw')

# include the unicows.dll for windows 98 compatibility ?
# (only needed if you are using unicode features of python)
include_unicows = True

# in included packages, delete '.pyc' and '.pyo' files *if* the corresponding 
# '.py' file exists (reduces distribution size)
delete_pyc = True

# set to '' to disable logging
logfile = 'MovpyCompiler.log'

# should 0, 1, or 2 - for optimized bytecode files (only used if 
# extended_options is True - not used in Python 2.2)
optimize = 0

# should be 0 or 1 - 1 for a compressed library (only used if extended_options
# is True - not used in Python 2.2)
compress = 0

# set to True to include all modules on sys.path (including 'site-packages')
build_full = False

############################

version_num = '2.0.0'
version_date = '17th January 2007'
versionstring = 'Movable Python. Version %s, %s.' % (version_num,
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
outfile = 'main.py'
outfile_win = 'mainw.py'
mainfile = 'modules/main.py'
pyversion = float(sys.version[:3])

# default directories to search for modules in 'Lib' and 'lib-tk'
libdirs = [os.path.join(sys.prefix, 'Lib'), os.path.join(sys.prefix,
    'Lib', 'lib-tk')]
get_win32 = True

filelist = []
liblist = ['files/customize.py', 'files/syspaths.pth']

# Need to add config files - e.g. 'files/config.txt', 'files/quicklaunch.txt'

try:
    import IPython
except ImportError:
    pass
else:
    liblist.append('files/ipythonrc.ini')

if pyversion > 2.3:
    # Need to add extra files
    filelist.append('files/msvcp71.dll')
    filelist.append('files/mfc71.dll')
else:
    filelist.append('files/mfc42.dll')
if include_unicows:
    filelist.append('files/unicows.dll')

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
    global fullpath, libdirs
    fullpath = getfullpath()
    if build_full:
        libdirs = fullpath
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
    for entry in include_modules:
        # if include_modules contains any packages - we need to add subpackages
        for directory in fullpath:
            for item in os.listdir(directory):
                fullitem = os.path.join(directory, item)
                if os.path.isdir(fullitem):
                    if item != entry:
                        continue
                    importlist += getimports(fullitem, entry)
                    if fullitem in fullpath:
                        # if the package directory is in the 'full path' we
                        # need to do direct imports as well as import as a
                        # subpackage
                        importlist += getimports(fullitem)
        #
        if entry not in importlist:
            importlist.append(entry)
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
    if pyversion < 2.3:
        # modifications for Python 2.2
        thecode = thecode.replace('("320x150")', '("465x150")')
        win_thecode = thecode
        # Add ``sys.frozen``
        thecode = thecode.replace('##sys.frozen = ##',
            "sys.frozen = 'console_exe'")
        win_thecode = win_thecode.replace('##sys.frozen = ##',
            "sys.frozen = 'windows_exe'")
        # create a bigger window
    else:
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
    if build:
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
    if pyversion >= 2.3:
        options = {'py2exe': {'dist_dir' : 'movpy' }}
        if extended_options:
            options['py2exe']['excludes'] = exclude_modules
            options['py2exe']['compressed'] = compress
            options['py2exe']['optimize'] = optimize
            
        setup(
            console = [{
                'script': outfile,
                'icon_resources': [(1, 'files/movpy.ico')],
                'other_resources': [(RT_MANIFEST, 1, open('files/movpy.exe.manifest').read())],
            }],
            windows = [{
                'script': outfile_win,
                'icon_resources': [(1, 'files/movpy.ico')],
                'other_resources': [(RT_MANIFEST, 1, open('files/movpyw.exe.manifest').read())],
            }],
            #
            version = version_num,
            description = ('Portable distribution of Python ' +
                sys.version.split(" ")[0]),
            name = 'Movable Python',
            author = 'Michael Foord',
            author_email = 'fuzzyman@voidspace.org.uk',
            url = 'http://www.voidspace.org.uk/python/movpy/',
            #
            data_files = [('', filelist),
                        ('lib', liblist)],
            zipfile = 'lib/library.zip',
            #
            options = options,
        )
    else:
        # for versions of python < 2.3 we have to use an older version of
        # py2exe (0.4.1) which takes arguments different
        print 'Building for Python < 2.3'
        sys.argv.append('--icon')
        sys.argv.append('files/movpy.ico')
        sys.argv.append('--force-imports')
        sys.argv.append('encodings')
        # FIXME: could use -d option to force a directory
        if extended_options:
            # The only extended options used for python 2.2 are exclude_modules
            # and optimize
            if exclude_modules:
                sys.argv.append('-e'+','.join(exclude_modules))
            sys.argv.append('-O'+str(optimize))
        print 'Building console version.'
        setup(
            # could do an external config file for the 'author' details etc
            scripts=['main.py'],
            data_files=   [('', filelist),
                            ('lib', liblist)],
            version=      version_num,
            description=  ('Portable distribution of Python '
                + sys.version.split(' ')[0]),
            name=         'Movable Python',
        )
        print 'Building windows version.'
        sys.argv.append('--windows')
        setup(
            # could do an external config file for the 'author' details etc
            scripts=['mainw.py'],
            version=      version_num,
            description=  ('Portable distribution of Python '
                + sys.version.split(' ')[0]),
            name=         'Movable Python',
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
    #
    print 'Intermediate files removed.'
    print 'Copying additional packages.'
    #
    prefix = ''
    if not os.path.isdir('movpy') and os.path.isdir('dist/main'):
        prefix = 'dist'
        shutil.copy('dist/mainw/mainw.exe', 'dist/main')
        shutil.rmtree('dist/mainw')
        os.rename('dist/main', 'dist/movpy')
        os.rename('dist/movpy/main.exe', 'dist/movpy/movpy.exe')
        os.rename('dist/movpy/mainw.exe', 'dist/movpy/movpyw.exe')
    else:
        os.rename('movpy/main.exe', 'movpy/movpy.exe')
        os.rename('movpy/mainw.exe', 'movpy/movpyw.exe')
    #
    packagepaths = []
    # deal with 'include_packages'
    wx_done = False
    package_dir = os.path.join(prefix, 'movpy', 'lib')
    for package in include_packages + wx_packages:
        done = False
        for pathdir in fullpath:
            if done:
                break
            if not os.path.isdir(pathdir):
                continue
            for entry in os.listdir(pathdir):
                thisentry = os.path.join(pathdir, entry)
                if os.path.isdir(thisentry) and entry == package:
                    if package in wx_packages:
                        if wx_done:
                            done = True
                            break
                        else:
                            wx_done = True
                            # write the wx.pth file
                            open(os.path.join(package_dir, 'wx.pth'), 'w').write(package + '\n')
                    #
                    print 'Copying', package
                    targetdir = os.path.join(package_dir, package)
                    if os.path.isdir(targetdir):
                        shutil.rmtree(targetdir)
                    shutil.copytree(thisentry, targetdir)
                    if delete_pyc:
                        delpyc(os.path.join(package_dir, package))
                    done = True
                    if thisentry in fullpath:
                        packagepaths.append(entry)
                    for subdir in walkdirs(thisentry):
                        if subdir in fullpath:
                            packagepaths.append(os.path.join(entry,
                                relpath(thisentry, subdir)))
                    break
        if not done and not package in wx_packages:
            print 'Failed to find package <%s>.' % package
    if packagepaths:
        handle = open(os.path.join(prefix, 'movpy\\lib\\packagepaths.pth'), 'w')
        handle.write('\n'.join(packagepaths))
        handle.close()
    #deal with docs
    print 'Copying docs.'
    shutil.copytree('docs_html', os.path.join(prefix, 'movpy', 'docs_html'))
    # overwrite the default menuhistory/firemail.ini for firedrop2
    shutil.copyfile('files/.menuhistory.txt', os.path.join(prefix,
        'movpy/lib/firedrop2/.menuhistory.txt'))
    shutil.copyfile('files/firemail.ini', os.path.join(prefix,
        'movpy/lib/firedrop2/plugins/firemail.ini'))
    #
    os.mkdir(os.path.join(prefix, 'movpy/lib/config'))
    print
    print 'Completed.'

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
    raw_input('>>>')
