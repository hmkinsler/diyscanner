# This script handles the function for calling the PDF creation settings to the GUI dynamic window

# Libraries
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Utilities
from config.config import config
from gui.utils.browse import browse_directory

def build_pdf_settings(parent):
    def save_pdf_settings():
        try:
            #config["pdf"]["ocr_enabled"] = ocr_var.get()
            config["pdf"]["output_location"] = output_location_entry.get()
            messagebox.showinfo("Success", "PDF settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save PDF settings: {e}")

    ttk.Frame(parent, bootstyle="dark").pack(fill=BOTH, expand=TRUE)

    # Main frame
    pdf_frame = ttk.Frame(
        master=parent, 
        bootstyle="dark",
        padding=20
        )
    pdf_frame.pack(fill=BOTH, expand=True)
    
    # Header section
    header_label = ttk.Label(
        master=pdf_frame,
        text="PDF Settings",
            font=("Helvetica", 31, "bold"),
            anchor=CENTER,
            bootstyle="dark inverse"
    ).pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

    # First divider    
    first_divider = ttk.Separator(
        master=pdf_frame,
        bootstyle="light")
    first_divider.pack(fill=X, pady=20)

    # Form section
    form_frame = ttk.Frame(
        master=pdf_frame, 
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
    
    # Create rows
    output_location_entry = create_form_row("Output location:", config["pdf"]["output_location"])

    # Second separator
    second_divider = ttk.Separator(
        master=pdf_frame,
        bootstyle="light")
    second_divider.pack(fill=X, pady=20)

    # Button container
    button_container = ttk.Frame(
        master=pdf_frame,
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
        text="Save PDF Formatting Settings",
        bootstyle="success",
        style="success.TButton",
        width=25,
        command=save_pdf_settings
    )
    save_button.pack(ipady=10)

    return pdf_frame