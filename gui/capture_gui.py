import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
from config.config import config


def render_capture_settings(content_frame):
    """Render Capture Settings in the provided content frame."""
    # Clear the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    ttk.Label(content_frame, text="Capture Settings", font=("TkDefaultFont", 16, 'bold')).pack(pady=10)

    # File Naming Format
    ttk.Label(content_frame, text="File Naming Format:").pack(anchor=W, padx=10)
    file_naming_var = ttk.StringVar(value=config["capture"]["file_naming"])
    ttk.Entry(content_frame, textvariable=file_naming_var).pack(padx=10, pady=5)

    # Number of Captures
    ttk.Label(content_frame, text="Number of Captures:").pack(anchor=W, padx=10)
    num_captures_var = ttk.StringVar(value=str(config["capture"]["num_captures"]))
    ttk.Entry(content_frame, textvariable=num_captures_var).pack(padx=10, pady=5)

    # Save Location
    ttk.Label(content_frame, text="Save Location:").pack(anchor=W, padx=10)
    save_location_var = ttk.StringVar(value=config["capture"]["save_location"])
    ttk.Entry(content_frame, textvariable=save_location_var).pack(padx=10, pady=5)
    ttk.Button(
        content_frame,
        text="Browse",
        command=lambda: browse_directory(save_location_var)
    ).pack(pady=5)

    # Save Button
    ttk.Button(
        content_frame,
        text="Save Settings",
        command=lambda: save_capture_settings(file_naming_var, num_captures_var, save_location_var),
        bootstyle=SUCCESS
    ).pack(pady=10)


def browse_directory(var):
    """Open a folder dialog and update the variable."""
    folder = filedialog.askdirectory()
    if folder:
        var.set(folder)


def save_capture_settings(file_naming_var, num_captures_var, save_location_var):
    """Save capture settings to the config."""
    try:
        config["capture"]["file_naming"] = file_naming_var.get()
        config["capture"]["num_captures"] = int(num_captures_var.get())
        config["capture"]["save_location"] = save_location_var.get()
        messagebox.showinfo("Success", "Capture settings saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save capture settings: {e}")
