import sys
import os
import imp
import marshal
from zipimport import zipimporter, ZipImportError

try:
    from cStringIO import StringIO, InputType, OutputType
except ImportError:
    from StringIO import StringIO
    stringio_type = StringIO
else:
    from StringIO import StringIO as String
    stringio_type = (InputType, OutputType, String)
"""
A module that patches several ``imp`` functions to work with py2exe.

It patches ``imp.find_module`` to work for source files contained in zip files.
(It returns a ``cStringIO`` instance instead of a real file.)

It patches ``imp.load_module`` and ``imp.load_compiled`` to work with
``StringIO`` instances. (``imp.load_module`` will also work for source files
contained in a ``StrringIO`` instance - but ``imp.load_source`` *isn't*
patched.

This module exports a single function ``patch``. This should be called before
any code which imports ``imp``.

The patched ``imp.find_module`` will only behave differently if you have a
single zipfile on ``sys.path`` when you call ``zip_imp.patch()``.

"""

__all__ = ('patch',)

_zip_file = None


def patch():
    global _zip_file
    for entry in sys.path:
        if entry.endswith('library.zip'):
            _zip_file = entry
            break
    imp._find_module = imp.find_module
    imp._load_module = imp.load_module
    imp._load_compiled = imp.load_compiled
    imp.find_module = _find_module
    imp.load_module = _load_module
    imp.load_compiled = _load_compiled

def _find_module(name, path=None):
   try:
       return imp._find_module(name, path)
   except ImportError:
        if _zip_file is None:
            raise
        z = zipimporter(_zip_file)
        try:
            code = z.get_code(name)
        except ZipImportError:
            raise ImportError('Failed to find module: %s' % name)
        mod = StringIO(_make_pyc(code))
        mod_names = [_zip_file] + name.split('.')
        mod_names[-1] += '.pyc'
        pathname = os.path.join(*mod_names)
        description = ('.pyc', 'rb', imp.PY_COMPILED)
        return (mod, pathname, description)

def _make_pyc(code):
    """
    Turn a bytecode object back into a string representing a '.pyc' file.
    
    Uses the spec laid out at :
    
        http://bob.pythonmac.org/archives/2005/03/24/pycs-eggs-and-zipimport/
    
    It uses the magic number from the ``imp`` module, and four null bytes to
    represent the modification time of the bytecode file.
    """
    return (imp.get_magic() + chr(0)*4 + marshal.dumps(code))

def _make_codeobj(file_obj):
    """Turn a file representing a bytecode object, into a code object."""
    return marshal.loads(file_obj.read()[8:])

def _load_module(name, file_obj, filename, (suffix, mode, type)):
    """
    Replace imp.load_module with a version that can handle StringIO instances.
    
    Works for byte-code compiled files and source files.
    """
    if not isinstance(file_obj, stringio_type):
        return imp._load_module(name, file_obj, filename, (suffix, mode, type))
    if suffix in ('.pyc', '.pyo'):
        return _load_compiled(name, filename, file_obj)
    elif suffix == '.py':
        return _load_source(name, filename, file_obj)

def _load_compiled(name, pathname, file_obj=None):
    """Replace imp.load_compiled"""
    if not file_obj or not isinstance(file_obj, stringio_type):
        return imp._load_compiled(name, pathname, file_obj)
    return _load(_make_codeobj(file_obj), name, pathname)

def _load_source(name, pathname, file_obj):
    """A version of imp.load_source that will work for Python source files."""
    return _load(fileobj.read(), name, pathname)

def _load(code, name, pathname):
    mod = imp.new_module(name)
    mod.__file__ = pathname
    exec code in mod.__dict__
    sys.modules[name] = mod
    return mod


if __name__ == '__main__':
    if not hasattr(sys, 'frozen'):
        print 'This test only works from *inside* Movable Python or a',
        print 'program frozen with py2exe.'
        sys.exit()
    #
    patch()
    name = 'Cookie'
    try:
        file, pathname, description = imp.find_module(name)
    except ImportError:
        print 'Failed to ``find_module``.'
    else:
        print file, pathname, description
        print '``find_module`` succeeded.'
        m = imp.load_module(name, file, pathname, description)
        print "``load_module`` succeeded."
        file.close()
        #
        print
        print m
        print m.Cookie

