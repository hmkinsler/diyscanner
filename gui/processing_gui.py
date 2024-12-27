# This script handles the function for calling the image processing settings to the GUI dynamic window

# Libraries
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Utilities
from config.config import config

def build_processing_settings(parent):
    def save_processing_settings():
        try:
            config["processing"]["rotate"] = int(rotate_entry.get())
            config["processing"]["contrast"] = float(contrast_entry.get())
            config["processing"]["brightness"] = float(brightness_entry.get())
            messagebox.showinfo("Success", "Processing settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {e}")

    ttk.Frame(parent, bootstyle="dark").pack(fill=BOTH, expand=TRUE)

    # Main frame
    processing_frame = ttk.Frame(
        master=parent, 
        bootstyle="dark",
        padding=20
        )
    processing_frame.pack(fill=BOTH, expand=True)

    # Header section  
    header_label = ttk.Label(
        master=processing_frame,
        text="Processing Settings",
            font=("Helvetica", 31, "bold"),
            anchor=CENTER,
            bootstyle="dark inverse"
    ).pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)
    
    first_divider = ttk.Separator(
        master=processing_frame,
        bootstyle="light")
    first_divider.pack(fill=X, pady=20)

    # Form section
    form_frame = ttk.Frame(
        master=processing_frame, 
        bootstyle="dark"
        )
    form_frame.pack(fill=BOTH, expand=True)

    def create_form_row(label_text, entry_var=None):
        # Container for each row
        row_frame = ttk.Frame(
            master=form_frame,
            bootstyle="dark")
        row_frame.pack(fill=X, ipady=5)
        
        # Label
        ttk.Label(
            row_frame,
            text=label_text,
            font=("Helvetica", 12),
            padding=20,
            bootstyle="dark inverse"
        ).pack(side=LEFT, ipadx=10)
        
        # Entry
        entry = ttk.Entry(
            master=row_frame)
        entry.pack(side=RIGHT, fill=X, expand=YES, ipadx=10)
        
        if entry_var is not None:
            entry.insert(0, str(entry_var))
            
        return entry

    # Create form rows
    rotate_entry = create_form_row("Rotate Images:", config["processing"]["rotate"])
    contrast_entry = create_form_row("Adjust Contrast:", config["processing"]["contrast"])
    brightness_entry = create_form_row("Adjust Brightness:", config["processing"]["brightness"])

    # Second separator
    second_divider = ttk.Separator(
        master=processing_frame,
        bootstyle="light")
    second_divider.pack(fill=X, pady=20)

    # Button container
    button_container = ttk.Frame(
        master=processing_frame,
        padding=20,
        bootstyle="dark"
        )
    button_container.pack(fill=X)

    my_style = ttk.Style()
    my_style.configure(
        "success.TButton",
        font=("Helvetica", 15)
        )

    save_button = ttk.Button(
        master=button_container,
        text="Save Processing Settings",
        bootstyle="success",
        style="success.TButton",
        width=25,
        command=save_processing_settings
    )
    save_button.pack(ipady=10)

    return processing_frame