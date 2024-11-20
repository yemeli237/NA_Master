from cx_Freeze import setup, Executable

setup(
    name="NA_Master",
    version="0.1",
    description="Mon application",
    executables=[Executable("NA_Master.py")]
)
