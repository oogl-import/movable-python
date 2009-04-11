# pvApi

print "loading pvApi"
LOGGING = True

# -------------------------------------------------------------------- access movpy variables

import movpy

# ---------------------------------------------------------------------- read movpy .INI file

INI = r"%s\lib\config\pywin.ini" % movpy.movpydir # E:\movpy25\movpy-2.0.0beta1-py2.5\movpy\lib\config
print repr(INI)

import ConfigParser

class MyConfigParser(ConfigParser.SafeConfigParser):
    def write(self, fp):
        """Write an .ini-format representation of the configuration state."""
        if self._defaults:
            fp.write("[%s]\n" % ConfigParser.DEFAULTSECT)
            for (key, value) in sorted(self._defaults.items()):
                fp.write("%s = %s\n" % (key, str(value).replace('\n', '\n\t')))
            fp.write("\n")
        for section in sorted(self._sections):
            fp.write("[%s]\n" % section)
            for (key, value) in sorted(self._sections[section].items()):
                if key != "__name__":
                    fp.write("%s = %s\n" %
                             (key, str(value).replace('\n', '\n\t')))
            fp.write("\n")
    def miss(self, section, option = None, value = "FIXME"):
        if not self.has_section(section):
            self.add_section(section)
        if section is not None:
            if not self.has_option(section, option):
                self.set(section, option, value)
    def get_option(self, section, option):
        if self.has_option(section, option):
            return self.get(section, option)
        else:
            self.miss(section, option)
            raise "option [%s] not found" % option

def read_config(ini, defaults = {}):
    aIni = file(ini, "r")
    cp = MyConfigParser(defaults)
    cp.readfp(aIni)
    aIni.close()
    return cp

def write_config(cp, ini):
    print "Writing ini file [%s]" % ini
    aIni = file(ini, "w")
    cp.write(aIni)
    aIni.close()

def joinkeys(key, subKey = None):
    if subKey:
        return key + "\\" + subKey
    else:
        return key

CP = read_config(INI, {'movpydir': movpy.movpydir})

# ---------------------------------------------------------------- access HKEYs from win32con

import win32con

h2k = {}
for k in win32con.__dict__.keys():
    if k.startswith('HKEY'):
        h2k[getattr(win32con, k)] = k

# ------------------------------------------------------------------------ insert my win32api

import win32api
from win32api import *

import sys
old_win32api = sys.modules['old_win32api'] = sys.modules['win32api']

def switch_modules():
    sys.modules['win32api'] = sys.modules['pvApi']
    print "modules switched"

def switch_modules_back():
    sys.modules['win32api'] = sys.modules['old_win32api']
    print "modules switched back"

# --------------------------------------------------------------------- install exit procedure

import atexit

def myexit():
    write_config(CP, INI)
    switch_modules_back()
    
atexit.register(myexit)

# ------------------------------------------------------------------------ hooks for win32api

import traceback
import pywintypes

class HKEY:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<HKEY %s>" % str(self.data)

def Hook(name, *arg):
    try:
        if LOGGING:
            print "* pvApi *", name, arg
        res = getattr(old_win32api, name)(*arg)
        if LOGGING:
            print '->', res
        return res
    except:
        line1 = traceback.format_exception(*(sys.exc_info()))[-1]
        print '-> EXCEPTION', line1.split('\n')[-2]
        raise
    
def RegCloseKey(*arg): 
    "Closes a previously opened registry key. "
    key, = arg # HKEY
    if isinstance(key, HKEY):
        pass
    else:
        return Hook('RegCloseKey', *arg)

def RegConnectRegistry(*arg):
    "Establishes a connection to a predefined registry handle on another computer. "
    computerName, key = arg
    return Hook('RegConnectRegistry', *arg)

def RegCreateKey(*arg):
    "Creates the specified key, or opens the key if it already exists. "
    return Hook('RegCreateKey', *arg)

def RegDeleteKey(*arg):
    "Deletes the specified key. "
    return Hook('RegDeleteKey', *arg)

def RegDeleteValue(*arg):
    "Removes a named value from the specified registry key. "
    return Hook('RegDeleteValue', *arg)

def RegEnumKey(*arg):
    "Enumerates subkeys of the specified open registry key. "
    key, index = arg
    if isinstance(key, HKEY):
        try:
            return CP.options(key.data)[index]
        except IndexError:
            raise pywintypes.error(259, 'pvApi_RegEnum_Key', 'IndexError')
    else:
        return Hook('RegEnumKey', *arg)

def RegEnumValue(*arg):
    "Enumerates values of the specified open registry key. "
    return Hook('RegEnumKey', *arg)

def RegFlushKey(*arg):
    "Writes all the attributes of the specified key to the registry. "
    return Hook('RegFlushKey', *arg)

def RegGetKeySecurity(*arg):
    "Retrieves the security on the specified registry key. "
    return Hook('RegGetKeySecurity', *arg)

def RegLoadKey(*arg):
    "Creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE and stores registration information from a specified file into that subkey. "
    return Hook('RegLoadKey', *arg)

def RegOpenKey(*arg):
    "Alias for win32api::RegOpenKeyEx. "
    key, subKey, reserved, sam = arg # PyHKEY/int, string, int, int -> PyHKey
    try:
        if LOGGING:
            print "* pvApi *", name, arg
        section = joinkeys(h2k[key], subKey)
        if CP.has_section(section):
            return HKEY(section)
        else:
            CP.miss(section)
    except:
        pass
    return Hook('RegOpenKey', *arg)

def RegOpenKeyEx(*arg):
    "Opens the specified key. "
    return Hook('RegOpenKeyEx', *arg)

def RegQueryValue(*arg):
    "Retrieves the value associated with the unnamed value for a specified key in the registry. "
    key, subKey = arg
    name = 'RegQueryValue'
    if LOGGING:
        print "* pvApi *", name, arg
    if isinstance(key, HKEY):
        section = joinkeys(key.data, subKey)
        if CP.has_section(section):
            return CP.get_option(section, '@')
        else:
            raise ConfigParser.NoSectionError(section)
    else:
        try:
            section = joinkeys(h2k[key], subKey)
            if LOGGING:
                print 'section:', section
            return CP.get_option(section, '@')
        except:
            print "RQV3", sys.exc_info()[:2]
            CP.miss(section, '@')
        return Hook('RegQueryValue', *arg)

def RegQueryValueEx(*arg):
    "Retrieves the type and data for a specified value name associated with an open registry key. " 
    return Hook('RegQueryValueEx', *arg)

def RegQueryInfoKey(*arg):
    "Returns information about the specified key. "
    return Hook('RegQueryInfoKey', *arg)

def RegSaveKey(*arg):
    "Saves the specified key, and all its subkeys to the specified file. "
    return Hook('RegSaveKey', *arg)

def RegSetKeySecurity(*arg):
    "Sets the security on the specified registry key. "
    return Hook('RegSetKeySecurity', *arg)

def RegSetValue(*arg):
    "Associates a value with a specified key. Currently, only strings are supported. "
    return Hook('RegSetValue', *arg)

def RegSetValueEx(*arg):
    "Stores data in the value field of an open registry key. "
    return Hook('RegSetValueEx', *arg)

def RegUnLoadKey(*arg):
    "Unloads the specified registry key and its subkeys from the registry. The keys must have been loaded previously by a call to RegLoadKey. "
    return Hook('RegUnLoadKey', *arg)

def RegNotifyChangeKeyValue(*arg):
    "Watch for registry changes. "
    return Hook('RegNotifyChangeKeyValue', *arg)

# ----------------------------------------------------------------------------- initialization

switch_modules()
