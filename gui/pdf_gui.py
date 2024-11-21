import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from config.config import config


def render_pdf_settings(content_frame):
    """Render PDF Settings in the provided content frame."""
    # Clear the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    ttk.Label(content_frame, text="PDF Settings", font=("TkDefaultFont", 16, 'bold')).pack(pady=10)

    # OCR Enabled
    ocr_var = ttk.BooleanVar(value=config["pdf"]["ocr_enabled"])
    ttk.Checkbutton(content_frame, text="Enable OCR", variable=ocr_var).pack(anchor=W, padx=10, pady=5)

    # Output Location
    ttk.Label(content_frame, text="Output Location:").pack(anchor=W, padx=10)
    output_location_var = ttk.StringVar(value=config["pdf"]["output_location"])
    ttk.Entry(content_frame, textvariable=output_location_var).pack(padx=10, pady=5)

    # Save Button
    ttk.Button(
        content_frame,
        text="Save Settings",
        command=lambda: save_pdf_settings(ocr_var, output_location_var),
        bootstyle=SUCCESS
    ).pack(pady=10)


def save_pdf_settings(ocr_var, output_location_var):
    """Save PDF settings to the config."""
    try:
        config["pdf"]["ocr_enabled"] = ocr_var.get()
        config["pdf"]["output_location"] = output_location_var.get()
        messagebox.showinfo("Success", "PDF settings saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save PDF settings: {e}")
