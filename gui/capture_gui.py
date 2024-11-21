import tkinter as tk
from tkinter import filedialog, messagebox
from config.config import config

def capture_settings_window(root):
    def save_settings():
        try:
            config["capture"]["file_naming"] = file_naming_var.get()
            config["capture"]["num_captures"] = int(num_captures_var.get())
            config["capture"]["save_location"] = save_location_var.get()
            messagebox.showinfo("Success", "Capture settings saved successfully!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {e}")

    window = tk.Toplevel(root)
    window.title("Capture Settings")

    file_naming_var = tk.StringVar(value=config["capture"].get("file_naming", "page_{:03d}.jpg"))
    num_captures_var = tk.StringVar(value=str(config["capture"].get("num_captures", 10)))
    save_location_var = tk.StringVar(value=config["capture"].get("save_location", "./captured_images"))

    tk.Label(window, text="File Naming Format:").pack()
    tk.Entry(window, textvariable=file_naming_var).pack()

    tk.Label(window, text="Number of Captures:").pack()
    tk.Entry(window, textvariable=num_captures_var).pack()

    tk.Label(window, text="Save Location:").pack()
    tk.Entry(window, textvariable=save_location_var).pack()
    tk.Button(window, text="Browse", command=lambda: browse_directory(save_location_var)).pack()

    tk.Button(window, text="Save", command=save_settings).pack()

def browse_directory(var):
    folder = filedialog.askdirectory()
    print(browse_directory)