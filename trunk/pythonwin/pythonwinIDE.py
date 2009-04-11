import sys
import win32ui
# importing 'intpyapp' automatically registers an app object.
from pywin.framework import intpyapp

# Remove this script name from sys.argv, else Pythonwin will try and open it!
sys.argv = sys.argv[1:]
# Get the MFC "app" object and boot it up.
app = win32ui.GetApp()
app.InitInstance()
app.Run()
app.ExitInstance()