import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

from utils.settings import config

class CaptureWindow():
    def __init__(self, parent):
        self.parent=parent
        self.build_capture_settings()
        self.load_images()

    def load_images(self):
        try:
            image = ImageTk.PhotoImage(Image.open("assets/save_icon.png").resize((50, 50)))
            return image
        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image due to: {str(e)}")

    def build_capture_settings(self):            
        def save_capture_settings(): 
            try:
                config["capture"]["file_naming"] = file_naming_entry.get()
                config["capture"]["num_captures"] = int(num_captures_entry.get())
                config["capture"]["save_location"] = save_location_entry.get()
                messagebox.showinfo("Success", "Capture settings saved successfully!")
            except ValueError:
                messagebox.showerror("Error", "Number of captures must be a valid number.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save capture settings: {e}")

        # Create the main container frame with padding
        main_container = ttk.Frame(
            master=self.parent,
            bootstyle="primary"
        )
        main_container.pack(fill=BOTH, expand=TRUE, ipadx=30, ipady=20)

        # Main frame
        capture_frame = ttk.Frame(
            master=main_container, 
            bootstyle="dark",
            padding=20
            )
        capture_frame.pack(fill=BOTH, expand=True)

        # Header section  
        first_header_divider = ttk.Separator(
            master=capture_frame,
            bootstyle="light")
        first_header_divider.pack(fill=X, pady=20)
        
        header_label = ttk.Label(
            master=capture_frame,
            text="Capture Settings",
                font=("Helvetica", 31, "bold"),
                anchor=CENTER,
                bootstyle="dark inverse"
        ).pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        second_header_divider = ttk.Separator(
            master=capture_frame,
            bootstyle="light")
        second_header_divider.pack(fill=X, pady=20)

        # Form section
        form_frame = ttk.Frame(
            master=capture_frame,
            padding=30, 
            bootstyle="dark",
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

        # Form row info for function
        file_naming_entry = create_form_row("File Naming Format:", config["capture"]["file_naming"])
        num_captures_entry = create_form_row("Number of Captures:", config["capture"]["num_captures"])
        save_location_entry = create_form_row("File Output Location:", config["capture"]["save_location"])

        # Second set of separators
        first_button_divider = ttk.Separator(
            master=capture_frame,
            bootstyle="light")
        first_button_divider.pack(fill=X, pady=20)

        second_button_divider = ttk.Separator(
            master=capture_frame,
            bootstyle="light")
        second_button_divider.pack(side=BOTTOM, fill=X, pady=20)

        # Button container
        button_container = ttk.Frame(
            master=capture_frame,
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
            text=" Save Capture Settings",
            image=save_icon,
            compound="left",
            bootstyle="success",
            style="success.Outline.TButton",
            width=25,
            command=save_capture_settings
        )
        save_button.image = save_icon
        save_button.pack(expand=YES, ipady=10)

def build_capture_settings(parent):
    return CaptureWindow(parent)