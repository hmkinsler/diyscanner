import os
from tkinter import filedialog

def browse_directory(var):
    """Open a folder dialog and update the variable."""
    folder = filedialog.askdirectory()
    if folder:
        var.set(folder)