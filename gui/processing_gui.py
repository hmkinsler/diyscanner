# This script handles the function for calling the image processing settings to the GUI dynamic window

# Libraries
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Utilities
from config.config import config

class ProcessingWindow():
    def __init__(self, parent):
        self.parent=parent
        self.build_processing_settings()
        self.load_images()

    def load_images(self):
        try:
            image = ImageTk.PhotoImage(Image.open("gui/images/save_transparent.png").resize((50, 50)))
            return image
        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image due to: {str(e)}")

    def build_processing_settings(self):
        def save_processing_settings():
            try:
                config["processing"]["rotate"] = int(rotate_entry.get())
                config["processing"]["contrast"] = float(contrast_entry.get())
                config["processing"]["brightness"] = float(brightness_entry.get())
                messagebox.showinfo("Success", "Processing settings saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save settings: {e}")

        # Main frame
        processing_frame = ttk.Frame(
            master=self.parent, 
            bootstyle="dark",
            padding=20
            )
        processing_frame.pack(fill=BOTH, expand=True)

        # Header section
        first_header_divider = ttk.Separator(
            master=processing_frame,
            bootstyle="light")
        first_header_divider.pack(fill=X, pady=20)

        header_label = ttk.Label(
            master=processing_frame,
            text="Processing Settings",
                font=("Helvetica", 31, "bold"),
                anchor=CENTER,
                bootstyle="dark inverse"
        ).pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        second_header_divider = ttk.Separator(
            master=processing_frame,
            bootstyle="light")
        second_header_divider.pack(fill=X, pady=20)
        
        # Form section
        form_frame = ttk.Frame(
            master=processing_frame,
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

        # Create form rows
        rotate_entry = create_form_row("Rotate Images:", config["processing"]["rotate"])
        contrast_entry = create_form_row("Adjust Contrast:", config["processing"]["contrast"])
        brightness_entry = create_form_row("Adjust Brightness:", config["processing"]["brightness"])

        # Second set of separators
        first_button_divider = ttk.Separator(
            master=processing_frame,
            bootstyle="light")
        first_button_divider.pack(fill=X, pady=20)

        second_button_divider = ttk.Separator(
            master=processing_frame,
            bootstyle="light")
        second_button_divider.pack(side=BOTTOM, fill=X, pady=20)

        # Button container
        button_container = ttk.Frame(
            master=processing_frame,
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
            text=" Save Processing Settings",
            image=save_icon,
            compound="left",
            bootstyle="success",
            style="success.Outline.TButton",
            width=25,
            command=save_processing_settings
        )
        save_button.image = save_icon
        save_button.pack(expand=YES, ipady=10)

def build_processing_settings(parent):
    return ProcessingWindow(parent)