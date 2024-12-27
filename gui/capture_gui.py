# This script handles the function for calling the image capture settings to the GUI dynamic window

# Libraries
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Utilities
from config.config import config
from gui.utils.browse import browse_directory

def build_capture_settings(parent):
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

    ttk.Frame(parent, bootstyle="dark").pack(fill=BOTH, expand=TRUE)

    # Main frame
    capture_frame = ttk.Frame(
        master=parent, 
        bootstyle="dark",
        padding=20
        )
    capture_frame.pack(fill=BOTH, expand=True)

    # Header section  
    header_label = ttk.Label(
        master=capture_frame,
        text="Capture Settings",
            font=("Helvetica", 31, "bold"),
            anchor=CENTER,
            bootstyle="dark inverse"
    ).pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)
    
    first_divider = ttk.Separator(
        master=capture_frame,
        bootstyle="light")
    first_divider.pack(fill=X, pady=20)

    # Form section
    form_frame = ttk.Frame(
        master=capture_frame, 
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

    # Form row info for function
    file_naming_entry = create_form_row("File Naming Format:", config["capture"]["file_naming"])
    num_captures_entry = create_form_row("Number of Image Captures:", config["capture"]["num_captures"])
    save_location_entry = create_form_row("Save Location:", config["capture"]["save_location"])

    # Second separator
    second_divider = ttk.Separator(
        master=capture_frame,
        bootstyle="light")
    second_divider.pack(fill=X, pady=20)

    # Button container
    button_container = ttk.Frame(
        master=capture_frame,
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
        text="Save Capture Settings",
        bootstyle="success",
        style="success.TButton",
        width=25,
        command=save_capture_settings
    )
    save_button.pack(ipady=10)

    # Add tooltips for better UX
    #ToolTip(file_naming_entry, text="Enter the format for naming captured files (e.g., 'page_{n}')")
    #ToolTip(num_captures_entry, text="Enter the number of images to capture")
    #ToolTip(save_location_entry, text="Select where to save captured images")

    return capture_frame