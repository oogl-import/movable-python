#### Movable Python
#### movpyGUITools.py

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

def unQuote(path):
    if not path.startswith('"'):
        return path, ''
    path = path[1:]
    rightQuote = path.lfind('"')
    if rightQuote == -1:
        # NOTE: This path is mangled !!
        # FIXME: Report an error ?
        return path, ''
    path, args = path.split('"', 1)
    return path, args.strip()


def getConsoleExe(path):
    directory, executable = os.path.split(path)
    if executable.lower() == 'pythonw.exe':
        executable = 'python.exe'
    elif executable.lower() == 'movpyw.exe':
        executable = 'movpy.exe'
    elif executable.lower() == 'ipyw.exe':
        executable = 'ipy.exe'
    return os.path.join(directory, executable)


def getNoConsoleExe(path):
    directory, executable = os.path.split(path)
    if executable.lower() == 'python.exe':
        executable = 'pythonw.exe'
    elif executable.lower() == 'movpy.exe':
        executable = 'movpyw.exe'
    elif executable.lower() == 'ipy.exe':
        executable = 'ipyw.exe'
    return os.path.join(directory, executable)


def getNormalExe(path, filename):
    filename, _ = unQuote(filename)
    if filename.endswith('.pyw'):
        path = getNoConsoleExe(path)
    elif isPythonFile(filename):
        path = getConsoleExe(path)
    return path


def getExecutableArgs(executable, options):
    args = ' '
    force_break = False
    executable = os.path.split(executable)[1].lower()
    if executable in ('python.exe', 'pythonw.exe'):
        if options['b']:
            force_break = True
        for opt in ('i', 'u', 'x'):
            if options[opt]:
                args += '-%s ' % opt
    elif executable in ('movpy.exe', 'movpyw.exe'):
        for opt in options:
            if opt.strip() in ('f', 'k', 'koff', 'o', ''):
                continue
            if options[opt]:
                args += '-%s ' % opt.strip()
        args += '-o '
    else:
        if options['b']:
            force_break = True
    return args, force_break


def isPythonFile(infile):
    return os.path.splitext(infile)[1].find('py') != -1


def isExecutableFile(path):
    return os.path.splitext(path)[1].lower() in ('.com', '.bat', '.exe')


def isMovpy(path):
    body = os.path.splitext(os.path.split(path)[1])[0]
    return body.lower().startswith('movpy')
