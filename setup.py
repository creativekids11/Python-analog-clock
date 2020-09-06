import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"E:\python\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"E:\python\tcl\tk8.6"

executables = [cx_Freeze.Executable("Clock.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Analog Clock",
    options = {"build_exe": {"packages":["tkinter","PIL","datetime","time","math"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll','clock.jpg']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
