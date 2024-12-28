# This script handles the function for calling the PDF creation settings to the GUI dynamic window

# Libraries
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Utilities
from config.config import config
from gui.utils.browse import browse_directory

class PDFWindow():
    def __init__(self, parent):
        self.parent=parent
        self.build_pdf_settings()
        self.load_images()

    def load_images(self):
        try:
            image = ImageTk.PhotoImage(Image.open("gui/images/save_transparent.png").resize((50, 50)))
            return image
        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image due to: {str(e)}")
    
    def build_pdf_settings(self):
        def save_pdf_settings():
            try:
                #config["pdf"]["ocr_enabled"] = ocr_var.get()
                config["pdf"]["output_location"] = output_location_entry.get()
                messagebox.showinfo("Success", "PDF settings saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save PDF settings: {e}")

        # Main frame
        pdf_frame = ttk.Frame(
            master=self.parent, 
            bootstyle="dark",
            padding=20
            )
        pdf_frame.pack(fill=BOTH, expand=True)
        
        # Header section
        first_header_divider = ttk.Separator(
            master=pdf_frame,
            bootstyle="light")
        first_header_divider.pack(fill=X, pady=20)

        header_label = ttk.Label(
            master=pdf_frame,
            text="PDF Settings",
                font=("Helvetica", 31, "bold"),
                anchor=CENTER,
                bootstyle="dark inverse"
        ).pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        second_header_divider = ttk.Separator(
            master=pdf_frame,
            bootstyle="light")
        second_header_divider.pack(fill=X, pady=20)

        # Form section
        form_frame = ttk.Frame(
            master=pdf_frame,
            padding=30, 
            bootstyle="dark"
            )
        form_frame.pack(fill=BOTH, expand=True)

        def create_form_row(label_text, entry_var=None):
            # Container for each row
            row_frame = ttk.Frame(
                master=form_frame,
                bootstyle="dark")
            row_frame.pack(fill=BOTH, expand=True, ipady=5)
            
            # Label
            ttk.Label(
                master=row_frame,
                text=label_text,
                font=("Helvetica", 20),
                anchor=W,
                bootstyle="dark inverse"
            ).pack(side=LEFT, fill=BOTH)
            
            # Entry
            entry = ttk.Entry(
                master=row_frame,
                font=("Helvetica", 15),
                justify=CENTER
            )
            entry.pack(fill=X, expand=True, ipady=8, padx=50, pady=20)
            
            if entry_var is not None:
                entry.insert(0, str(entry_var))
                
            return entry
        
        # Create rows
        output_location_entry = create_form_row("Output location:", config["pdf"]["output_location"])

        # Second set of separators
        first_button_divider = ttk.Separator(
            master=pdf_frame,
            bootstyle="light")
        first_button_divider.pack(fill=X, pady=20)

        second_button_divider = ttk.Separator(
            master=pdf_frame,
            bootstyle="light")
        second_button_divider.pack(side=BOTTOM, fill=X, pady=20)

        # Button container
        button_container = ttk.Frame(
            master=pdf_frame,
            padding=20,
            bootstyle="dark"
            )
        button_container.pack(fill=X)

        my_style = ttk.Style()
        my_style.configure(
            "success.Outline.TButton",
            font=("Helvetica", 25)
            )
        
        save_icon = self.load_images()

        save_button = ttk.Button(
            master=button_container,
            text=" Save PDF Formatting Settings",
            image=save_icon,
            compound="left",
            bootstyle="success",
            style="success.Outline.TButton",
            width=25,
            command=save_pdf_settings
        )
        save_button.image = save_icon
        save_button.pack(ipady=10)

def build_pdf_settings(parent):
    return PDFWindow(parent)