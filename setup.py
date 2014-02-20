from cx_Freeze import setup, Executable
setup(name = "Flappy Python",
      version = "0.1",
      description = "Yet another Flappy Bird clone.",
      executables = [Executable("main.py")])
