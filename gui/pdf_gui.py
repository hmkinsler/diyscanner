import tkinter as tk
from tkinter import filedialog, messagebox
from config.config import config

def pdf_settings_window(root):
    def save_settings():
        try:
            config["pdf"]["ocr_enabled"] = ocr_var.get() == "1"
            config["pdf"]["output_location"] = output_location_var.get()
            messagebox.showinfo("Success", "PDF settings saved successfully!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {e}")

    window = tk.Toplevel(root)
    window.title("PDF Settings")

    ocr_var = tk.StringVar(value="1" if config["pdf"].get("ocr_enabled", True) else "0")
    output_location_var = tk.StringVar(value=config["pdf"].get("output_location", "./output"))

    tk.Label(window, text="Enable OCR:").pack()
    tk.Checkbutton(window, variable=ocr_var, onvalue="1", offvalue="0").pack()

    tk.Label(window, text="Output Location:").pack()
    tk.Entry(window, textvariable=output_location_var).pack()
    tk.Button(window, text="Browse", command=lambda: browse_directory(output_location_var)).pack()

    tk.Button(window, text="Save", command=save_settings).pack()

def browse_directory(var):
    folder = filedialog.askdirectory()
    print(browse_directory)
