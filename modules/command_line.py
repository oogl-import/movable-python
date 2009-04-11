#### Movable Python
#### command_line.py

# Handling of command line options.

# Homepage : http://www.voidspace.org.uk/python/movpy/
# Download from : http://voidspace.tradebit.com

# Copyright Michael Foord, 2004-2006.
# Commercial software.

# For information about bugfixes, updates and support, 
# or for bug reports and feature requests - join the movpy mailing list.
# http://groups.google.com/group/movpy/
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

# check if we have a config file and set additional command line options
# if we have any

"""
Handle logging with

    -lmode "logfilename"
    mode is either a for append or w for new file
"""

import os
import sys
from movpy_tools import remcom

# NOTE: Only options that can be set directly in the GUI
#       others must be handled explicitly.
the_options = ('-u', '-i', '-x', '-IPOFF', '-p', '-f', '-k', '-koff',
    '-b', '-o')

ignored = ('-d', '-E', '-O', '-OO', '-Qold', '-Qwarn', '-Qwarnall', '-Qnew',
    '-S', '-t', '-tt', '-v')

defaults = {'config': None}

warning = '''usage: movpy [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `movpy -h' for more information.
'''

helpfile = '''usage: movpy [option] ... [-c cmd | file | -] [arg] ...
Options and arguments :
-c cmd : program passed in as string (terminates option list)
-f     : Change working directory to the script directory
-h     : print this help message and exit
-i     : inspect interactively after running script,
         uses InteractiveConsole or IPython - probably needs a real stdin
-m mod : run library module as a script (terminates option list)
-u     : unbuffered stdout and stderr
-V     : print the movpy version and Python version number and exit
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-IPOFF : Don't use IPython, even if it is available, default to InteractiveConsole
-p     : Attempt pysco.full() (incompatible with IPython interactive shell)
-b     : Pause for <enter> after terminating script
-o     : override saved options, only use comand line options
-koff  : A command line option for the GUI, force no console
-k     : A command line option for the GUI, force a console
-la file : Log output to file, open append in write mode
-lw file : Log output to file, open logfile in write mode
file   : program read from script file
-      : drop straight into InteractiveConsole or IPython
-pylab : Launch IPython in pylab mode
--config dir : Directory for config files (~ will be expanded)
arg ...: arguments passed to program in sys.argv[1:]
Run movpy without a file argument to bring up a lightweight GUI to choose a script
('-c', '-', '-V' or '-h' options override this behaviour)
Python environment variables are ignored.'''

# configfilepath = os.path.join(libdir, 'config.txt')

def get_config(filepath):
    config_options = {}
    if os.path.isfile(filepath):
        optionlist = remcom(filepath)
        for entry in optionlist:
            # a limited set of command line options can be set as default in the
            # config file  - they can't yet be overridden by the commandline
            if entry in the_options:
                config_options[entry[1:]] = True
            else:
                raise ValueError('Unknown Option in config file.')
    return config_options

def parse_options(movversion):
    """Custom command line handling."""
    options = dict([(option[1:], False) for option in the_options])
    options.update(defaults)
    options['l'] = False
    # FIXME: doesn't handle duplicate options
    # FIXME: doesn't handle conflicting -k and -koff
    # FIXME: what about invalid options (that start with '-')
    while len(sys.argv) > 1:
        val = sys.argv[1]
        if val == '-Q':
            # handle warnings
            del sys.argv[1]
            if (len(sys.argv) < 2) or (sys.argv[1] not in ('warn', 'warnall',
                'old', 'new')):
                sys.stderr.write(('Missing or invalid division option. -Q '
                    'Unsupported anyway.\n'))
                sys.stderr.write(warning)
                sys.exit(1)
            else:
                del sys.argv[1]
                sys.stderr.write('Option "-Q" unsupported. Ignored.\n')
        elif val == '-W':
            del sys.argv[1]
            sys.stderr.write('Option "-W" unsupported. Ignored.\n')
            if len(sys.argv) > 2:
                if not ':' in sys.argv[1]:
                    sys.stderr.write(('Argument to "-W" ignored - "%s".\n'
                        % sys.argv[1]))
                del sys.argv[1]
        elif val == '-m':
            del sys.argv[1]
            options['m'] = True
            # terminates options
            break
        elif val in ignored:
            sys.stderr.write('Option "%s" not supported. Ignored.\n' % val)
            del sys.argv[1]
        elif val == '-V':
            print 'Python', sys.version
            print movversion
            sys.exit()
        elif val == '-h':
            print helpfile
            sys.exit()
        elif val == '-c':
            if len(sys.argv) < 3:
                raise ValueError('No command specified with "-c" option.\n')
            options['c'] = sys.argv[2]
            del sys.argv[1:3]
            break
        elif val in ('-la', '-lw', '-lo'):
            options['l'] = True
            if len(sys.argv) < 3:
                raise ValueError('No logfile specified with "%s" option.\n' % val)
            options['logmode'] = val[2]
            options['logfile'] = sys.argv[2]
            del sys.argv[1:3]
        elif val in the_options:
            del sys.argv[1]
            options[val[1:]] = True
        elif val == '-o':
            del sys.argv[1]
            options['o'] = True
        elif val == '--config':
            if len(sys.argv) < 3:
                raise ValueError('No config file specified with "%s" option.\n' % val)
            options['config'] = os.path.expanduser(sys.argv[2])
            del sys.argv[1:3]
        
        else:
            # an unrecognised option
            break
    return options
