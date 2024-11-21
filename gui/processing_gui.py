import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from config.config import config


def render_processing_settings(content_frame):
    """Render Processing Settings in the provided content frame."""
    # Clear the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    ttk.Label(content_frame, text="Processing Settings", font=("TkDefaultFont", 16, 'bold')).pack(pady=10)

    # Resize Dimensions
    ttk.Label(content_frame, text="Resize Dimensions (Width x Height):").pack(anchor=W, padx=10)
    width_var = ttk.StringVar(value=str(config["processing"]["resize_dimensions"][0]))
    height_var = ttk.StringVar(value=str(config["processing"]["resize_dimensions"][1]))
    ttk.Entry(content_frame, textvariable=width_var).pack(side=LEFT, padx=5)
    ttk.Entry(content_frame, textvariable=height_var).pack(side=LEFT, padx=5)

    # Contrast
    ttk.Label(content_frame, text="Contrast:").pack(anchor=W, padx=10)
    contrast_var = ttk.StringVar(value=str(config["processing"]["contrast"]))
    ttk.Entry(content_frame, textvariable=contrast_var).pack(padx=10, pady=5)

    # Brightness
    ttk.Label(content_frame, text="Brightness:").pack(anchor=W, padx=10)
    brightness_var = ttk.StringVar(value=str(config["processing"]["brightness"]))
    ttk.Entry(content_frame, textvariable=brightness_var).pack(padx=10, pady=5)

    # Save Button
    ttk.Button(
        content_frame,
        text="Save Settings",
        command=lambda: save_processing_settings(width_var, height_var, contrast_var, brightness_var),
        bootstyle=SUCCESS
    ).pack(pady=10)


def save_processing_settings(width_var, height_var, contrast_var, brightness_var):
    """Save processing settings to the config."""
    try:
        config["processing"]["resize_dimensions"] = (int(width_var.get()), int(height_var.get()))
        config["processing"]["contrast"] = float(contrast_var.get())
        config["processing"]["brightness"] = float(brightness_var.get())
        messagebox.showinfo("Success", "Processing settings saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save processing settings: {e}")
