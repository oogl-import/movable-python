#### Movable Python
#### movpy_tools.py

# This script provides tools for portable Python distributions.

# Homepage : http://www.voidspace.org.uk/python/movpy/
# Download from : http://voidspace.tradebit.com

# Written by : Michael Foord
# With input from :
#   Bruno Thoorens
#   Stani, the creator of SPE the Python IDE - http://spe.pycs.net

# Copyright Michael Foord, 2004-2006.
# Commercial software.

# For information about bugfixes, updates and support, 
# or for bug reports and feature requests - join the movpy mailing list.
# http://groups.google.com/group/movpy/
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

__all__ = (
    'remcom',
    'interactive_mode',
    'joinPaths',
    'psycofullon',
    '_Printer',
    '_Helper',
    'setquit',
    'setcopyright',
    'modulefinder',
    '_setlibdir',
    'launch_pylab',
)

def joinPaths(*args):
    return os.path.normpath(os.path.join(*args))

######################################

import os
import sys
import __builtin__
from _pathutils import readlines

######################################

libdir = None

def _setlibdir(the_dir):
    global libdir
    libdir = the_dir

######################################

def remcom(fname):
    """A version of readlines that removes comments and strips lines."""
    return [line.strip() for line in readlines(fname) if line.strip()
        and not line.strip().startswith('#')]

def interactive_mode(localvars=None, globalvars=None, IPOFF=False, argv=None):
    """A very simple function to embed an interactive interpreter into movpy."""
    # FIXME: could have the banner passed in as an optional argument
    #        plus maybe the IPython config file location
    if localvars is not None and globalvars is None:
        globalvars = localvars
    #
    try:
        from IPython.Shell import IPShell
    except ImportError:
        IPShell = None
    # NOTE: psyco and IPython are incompatible
    if (IPShell is None) or (IPOFF or psycofullon()):
        if localvars is None:
            # extract locals from the calling frame - taken from IPython
            localvars = sys._getframe(0).f_back.f_locals
        from code import InteractiveConsole
        con = InteractiveConsole(localvars)
        con.interact()
    else:
        banner = ('Movable Python\nIPython Interactive Shell. See the manual '
                  'for a list of features and tips.\nCtrl-D to exit.')
        # where to find the ipython config file
        if libdir:
            argv = ['-ipythondir', libdir] + (argv or [])
        try:
            ipshell = IPShell(argv, user_ns=localvars, user_global_ns=globalvars)
            ipshell.mainloop(banner=banner)
        except AttributeError, e:
            print e
            # if psyco is on, IPython will fail immediately with an AttributeError
            if localvars is None:
                # extract locals from the calling frame - taken from IPython
                localvars = sys._getframe(0).f_back.f_locals
            from code import InteractiveConsole
            con = InteractiveConsole(localvars)
            con.interact()

def launch_pylab():
    sys.argv = sys.argv[:1] + ['-pylab', '-ipythondir', libdir] + sys.argv[1:]
    import IPython
    IPython.Shell.start().mainloop()

##########################################

# Functions from site.py
# Used by IPython
# These add objects would normally be available as builtins in the python
# environment but aren't in a normal py2exe program !

# NOTE: What about the rest of the stuff from site.py ?
# We could also add to copyrights and credits like IPython does


class _Printer(object):
    """
    interactive prompt objects for printing the license text, a list of
    contributors and the copyright notice.
    """
    MAXLINES = 23

    def __init__(self, name, data, files=(), dirs=()):
        self.__name = name
        self.__data = data
        self.__files = files
        self.__dirs = dirs
        self.__lines = None

    def __setup(self):
        if self.__lines:
            return
        data = None
        for dir in self.__dirs:
            for filename in self.__files:
                filename = os.path.join(dir, filename)
                try:
                    fp = file(filename, "rU")
                    data = fp.read()
                    fp.close()
                    break
                except IOError:
                    pass
            if data:
                break
        if not data:
            data = self.__data
        self.__lines = data.split('\n')
        self.__linecnt = len(self.__lines)

    def __repr__(self):
        self.__setup()
        if len(self.__lines) <= self.MAXLINES:
            return "\n".join(self.__lines)
        else:
            return "Type %s() to see the full %s text" % ((self.__name,)*2)

    def __call__(self):
        self.__setup()
        prompt = 'Hit Return for more, or q (and Return) to quit: '
        lineno = 0
        while 1:
            try:
                for i in range(lineno, lineno + self.MAXLINES):
                    print self.__lines[i]
            except IndexError:
                break
            else:
                lineno += self.MAXLINES
                key = None
                while key is None:
                    key = raw_input(prompt)
                    if key not in ('', 'q'):
                        key = None
                if key == 'q':
                    break


class _Helper(object):
    """
    Define the built-in 'help'.
    This is a wrapper around pydoc.help (with a twist).
    """
    def __repr__(self):
        return ("Type help() for interactive help, "
               "or help(object) for help about object.")

    def __call__(self, *args, **kwds):
        import pydoc
        return pydoc.help(*args, **kwds)

###########################################

def psycofullon():
    """
    This function returns True if psyco.full() has been called.
    Thanks to Armin Rigo for this function.
    """
    try:
        return __in_psyco__
    except NameError:
        # Psyco was not imported
        return False

###########################################

def setquit(namespace):
    """
    Define new built-ins 'quit' and 'exit'.
    These are simply strings that display a hint on how to exit.
    """
    if os.sep == ':':
        exit = 'Use Cmd-Q to quit.'
    elif os.sep == '\\':
        exit = 'Use Ctrl-Z plus Return to exit.'
    else:
        exit = 'Use Ctrl-D (i.e. EOF) to exit.'
    namespace['__builtin__'].quit = __builtin__.exit = exit

def setcopyright(namespace):
    """Set 'copyright' and 'credits' in __builtin__"""
    __builtin__.copyright = _Printer("copyright", sys.copyright)
    #
    __builtin__.credits = _Printer("credits", """\
Movable Python by Michael Foord
With assistance from Bruno Thoorens and Stani
Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
for supporting Python development.  See www.python.org for more information.""")
    here = os.path.dirname(os.__file__)
    namespace['__builtin__'].license = _Printer(
    "license", "See http://www.python.org/%.3s/license.html" % sys.version,
    ["LICENSE.txt", "LICENSE"],
        [os.path.join(here, os.pardir), here, os.curdir])

###########################################

def modulefinder(mod):
    """
    Given a module name, return a code object. This is used to simulate the
    ``-m`` Python command line option. You can then use ``exec`` on the
    resulting code object.
    
    Works for modules with an associated file of the following types :
    
        ``('.pyc', '.pyo', '.py', '.pyw')``
    
    If it can't find the associated file on the path, it raises a
    ``ValueError``.
    
    This function could raise a ``SyntaxError`` if the ``compile`` fails.
    
    It could raise a ``ValueError`` if un-marshaling a '.pyc' file fails.
    
    It will find files in a zip file (using zipimporter), but *can't* find
    modules in packages in zip files.
    
    If a package name is specified, with no sub-package, then it will not be
    found. (We could change this to use the ``__init__.py`` file of the
    package.)
    """
    sources = ('.py', '.pyc', '.pyo', '.pyw')
    # Is it a package file ?
    mods = mod.split('.')
    mod1, mods = mods[0], mods[1:]
    #
    for entry in sys.path:
        if entry.endswith('.zip') and not mods:
            # Need to use zipimporter
            import zipimport
            try:
                z = zipimport.zipimporter(entry)
            except zipimport.ZipImportError:
                # not a valid zipfile
                # we'll try this path as a directory
                pass
            else:
                try:
                    return z.get_code(mod)
                except zipimport.ZipImportError:
                    traceback.print_exc()
                    continue
        # try it as a directory
        if mods and os.path.isdir(os.path.join(entry, mod1)):
            # a package
            break
        elif not mods:
            for ending in sources:
                if os.path.isfile(os.path.join(entry, mod1 + ending)):
                    path = os.path.join(entry, mod1 + ending)
                    code = open(path, 'rb').read()
                    if ending in ('.pyc', '.pyo'):
                        import marshal
                        return marshal.loads(code[8:])
                    else:
                        code = code.replace('\r\n', '\n') + '\n'
                        return compile(code, path, 'exec')
            else:
                continue
    else:
        raise ValueError('No file associated with module "%s".' % mod)
    last, mods = mods[-1], mods[:-1]
    the_path = os.path.join(entry, mod1, *mods)
    for ending  in sources:
        path = os.path.join(the_path, last + ending)
        if os.path.isfile(path):
            code = open(path, 'rb').read()
            if ending in ('.pyc', '.pyo'):
                import marshal
                return marshal.loads(code[8:])
            else:
                code = code.replace('\r\n', '\n') + '\n'
                return compile(code, path, 'exec')
    raise ValueError('No file associated with module "%s".' % mod)
