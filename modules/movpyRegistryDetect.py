#### Movable Python
#### movpyRegistryDetect.py

# Homepage : http://www.voidspace.org.uk/python/movpy/
# Download from : http://voidspace.tradebit.com

# Copyright Michael Foord, 2004-2006.
# Commercial software.

# For information about bugfixes, updates and support, 
# or for bug reports and feature requests - join the movpy mailing list.
# http://groups.google.com/group/movpy/
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

import _winreg

try:
    import win32api
except ImportError:
    def convertPath(path):
        return path
else:
    convertPath = win32api.GetLongPathName

def get_subkey_names(reg_key):
    index = 0
    L = []
    while True:
        try:
            name = _winreg.EnumKey(reg_key, index)
        except EnvironmentError:
            break
        index += 1
        L.append(name)
    return L

def find_installed_pythons():
    """
    Return a list with info about installed versions of Python.

    Each version in the list is represented as a tuple with 3 items:

    0   A long integer giving when the key for this version was last
          modified as 100's of nanoseconds since Jan 1, 1600.
    1   A string with major and minor version number e.g '2.4'.
    2   A string of the absolute path to the installation directory.
    """
    python_path = r'software\python\pythoncore'
    L = []
    for reg_hive in (_winreg.HKEY_LOCAL_MACHINE,
                      _winreg.HKEY_CURRENT_USER):
        try:
            try:
                python_key = _winreg.OpenKey(reg_hive, python_path)
            except EnvironmentError:
                continue
            for version_name in get_subkey_names(python_key):
                key = _winreg.OpenKey(python_key, version_name)
                modification_date = _winreg.QueryInfoKey(key)[2]
                install_path = convertPath(_winreg.QueryValue(key, 'installpath'))
                L.append((modification_date, version_name, install_path))
        except WindowsError:
            continue
    return L

if __name__ == '__main__':
    print find_installed_pythons()