# This script handles the function for calling the PDF creation settings to the GUI dynamic window
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox
from config.config import config
from gui.browse import browse_directory

def build_pdf_settings(parent):
    def save_pdf_settings():
        try:
            config["pdf"]["ocr_enabled"] = ocr_var.get()
            config["pdf"]["output_location"] = output_location_var.get()
            messagebox.showinfo("Success", "PDF settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save PDF settings: {e}")
                    
# Main frame
    pdf_overall = ttk.Frame(parent, bootstyle="dark")
    pdf_overall.grid(sticky="NSEW")

    # Settings content frame
    pdf_frame = ttk.Frame(pdf_overall, bootstyle="light", padding=20)
    pdf_frame.grid(sticky="NS")
    for col in range(4):
        pdf_frame.grid_columnconfigure(col, weight=1)

    # Header
    header_frame = ttk.Frame(pdf_frame)
    header_frame.grid(row=0, column=0, columnspan=3)
    
    ttk.Label(
        header_frame,
        text="PDF Generation Settings",
        font=("Helvetica", 24, "bold"),
        bootstyle="light inverse"
    ).grid()
    
    ttk.Separator(pdf_frame).grid(row=1, column=0, columnspan=4, sticky=EW, pady=20)

    # OCR Enabled
    ocr_var = ttk.BooleanVar(value=config["pdf"]["ocr_enabled"])
    ttk.Checkbutton(pdf_frame, text="Enable OCR", variable=ocr_var).grid(column=0, columnspan=2, row=1, padx=5, pady=5)

    # Output Location
    ttk.Label(pdf_frame, text="Output Location:").grid(column=0, row=2, padx=5, pady=5)
    output_location_var = ttk.StringVar(value=config["pdf"]["output_location"])
    ttk.Entry(pdf_frame).grid(column=1, row=2, padx=5, pady=5)
    ttk.Button(
        pdf_frame,
        text="Browse Directory",
        command=lambda: browse_directory(output_location_var)
    ).grid(column=1, row=2, padx=5, pady=5)

    # Footer section with separator and save button
    ttk.Separator(pdf_frame).grid(row=3, column=0, columnspan=4, sticky=EW, pady=20)

    # Save button container for better positioning
    button_container = ttk.Frame(pdf_frame)
    button_container.grid(row=4, column=0, columnspan=3)

    save_button = ttk.Button(
        button_container,
        text="Save Settings",
        bootstyle="success",
        command=save_pdf_settings,
        width=15
    )
    save_button.grid(row=0, column=0, ipady=10)

    return pdf_frame