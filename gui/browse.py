# this script ensures that any "browse directory" GUI functions will be able to browse directories and set them as needed
import os
from tkinter import filedialog

def browse_directory(var):
    """Open a folder dialog and update the variable."""
    folder = filedialog.askdirectory()
    if folder:
        var.set(folder)