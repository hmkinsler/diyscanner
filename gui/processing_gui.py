# This script handles the function for calling the image processing settings to the GUI dynamic window
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox
from config.config import config

def build_processing_settings(parent):
    def save_processing_settings():
        try:
            #config["processing"]["resize_dimensions"] = (int(width_var.get()), int(height_var.get()))
            config["processing"]["rotate"] = int(rotate_entry.get())
            config["processing"]["contrast"] = float(contrast_entry.get())
            config["processing"]["brightness"] = float(brightness_entry.get())
            #config["processing"]["crop_margins"] = (
                #int(top_var.get()),
                ##int(right_var.get()),
                #int(bottom_var.get()),
                #int(left_var.get())
            #)
            messagebox.showinfo("Success", "Processing settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {e}")

    # Main frame
    processing_overall = ttk.Frame(parent, bootstyle="dark")
    processing_overall.grid()

    # Settings content frame
    processing_frame = ttk.Frame(processing_overall, bootstyle="light", padding=20)
    processing_frame.grid()
    # Configure grid weights
    for col in range(5):
        processing_frame.grid_columnconfigure(col, weight=1)

    # Header
    header_frame = ttk.Frame(processing_frame)
    header_frame.grid(row=0, column=0, columnspan=4)
    
    ttk.Label(
        header_frame,
        text="Processing Settings",
        font=("Helvetica", 24, "bold"),
        bootstyle="light inverse"
    ).grid()
    
    ttk.Separator(processing_frame).grid(row=1, column=0, columnspan=5, sticky=EW, pady=20)

    # Form section
    form_frame = ttk.Frame(
        processing_frame,
        bootstyle="light"
    )
    form_frame.grid(row=2, column=0, columnspan=4)

    # Create form rows
    def create_form_row(label_text, row, entry_var=None, has_button=False):
        ttk.Label(
            form_frame,
            text=label_text,
            font=("Helvetica", 12),
            padding=10,
            bootstyle="light inverse"
        ).grid(column=0, row=row)
        
        entry = ttk.Entry(form_frame)
        entry.grid(column=1, row=row, padx=(10, 10 if has_button else 0))
        
        if entry_var is not None:
            entry.insert(0, str(entry_var))
            
        return entry

    # Form row info for function
    #resize_entry = create_form_row("Resize Images:", 0, config["processing"]["resize_dimensions"])
    rotate_entry = create_form_row("Rotate Images:", 1, config["processing"]["rotate"])
    contrast_entry = create_form_row("Adjust Contrast:", 2, config["processing"]["contrast"])
    brightness_entry = create_form_row("Adjust Brightness", 3, config["processing"]["brightness"])
    #crop_entry = create_form_row("Crop Images:", 4, config["processing"]["crop_margins"])

    ttk.Separator(processing_frame).grid(row=3, column=0, columnspan=5, sticky=EW, pady=20)

    button_container = ttk.Frame(processing_frame)
    button_container.grid(row=4, column=0, columnspan=4)

    save_button = ttk.Button(
        button_container,
        text="Save Settings",
        bootstyle="success",
        command=save_processing_settings,
        width=15
    )
    save_button.grid(row=0, column=0, ipady=10)

    # Return the built frame
    return processing_frame
