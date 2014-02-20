import sys
from cx_Freeze import setup, Executable

includefiles=['python.png', 'freesansbold.ttf', 'pipe.png', 'background.png']

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "Flappy Python",
      version = "0.1",
      description = "Yet another Flappy Bird clone.",
      options = {'build_exe': {'include_files': includefiles}},
      executables = [Executable("main.py")])
