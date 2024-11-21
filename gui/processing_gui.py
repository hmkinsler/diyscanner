import tkinter as tk
from tkinter import filedialog, messagebox
from config.config import config

def processing_settings_window(root):
    def save_settings():
        try:
            config["processing"]["resize_dimensions"] = (int(width_var.get()), int(height_var.get()))
            config["processing"]["contrast"] = float(contrast_var.get())
            config["processing"]["brightness"] = float(brightness_var.get())
            config["processing"]["save_location"] = save_location_var.get()
            messagebox.showinfo("Success", "Processing settings saved successfully!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {e}")

    window = tk.Toplevel(root)
    window.title("Processing Settings")

    width_var = tk.StringVar(value=str(config["processing"]["resize_dimensions"][0]))
    height_var = tk.StringVar(value=str(config["processing"]["resize_dimensions"][1]))
    contrast_var = tk.StringVar(value=str(config["processing"]["contrast"]))
    brightness_var = tk.StringVar(value=str(config["processing"]["brightness"]))
    save_location_var = tk.StringVar(value=config["processing"]["save_location"])

    tk.Label(window, text="Resize Width:").pack()
    tk.Entry(window, textvariable=width_var).pack()

    tk.Label(window, text="Resize Height:").pack()
    tk.Entry(window, textvariable=height_var).pack()

    tk.Label(window, text="Contrast:").pack()
    tk.Entry(window, textvariable=contrast_var).pack()

    tk.Label(window, text="Brightness:").pack()
    tk.Entry(window, textvariable=brightness_var).pack()

    tk.Label(window, text="Save Location:").pack()
    tk.Entry(window, textvariable=save_location_var).pack()
    tk.Button(window, text="Browse", command=lambda: browse_directory(save_location_var)).pack()

    tk.Button(window, text="Save", command=save_settings).pack()

def browse_directory(var):
    folder = filedialog.askdirectory()
    print(browse_directory)
