import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from config.config import config
from gui.browse import browse_directory

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

    # Main frame
    capture_overall = ttk.Frame(parent, bootstyle="dark")
    capture_overall.grid(sticky=NS)

    # Settings content frame
    capture_frame = ttk.Frame(capture_overall, bootstyle="light", padding=20)
    capture_frame.grid()
    for col in range(4):
        capture_frame.grid_columnconfigure(col, weight=1)

    # Header
    header_frame = ttk.Frame(capture_frame)
    header_frame.grid(row=0, column=0, columnspan=3)
    
    ttk.Label(
        header_frame,
        text="Capture Settings",
        font=("Helvetica", 24, "bold"),
        bootstyle="light inverse"
    ).grid()
    
    ttk.Separator(capture_frame).grid(row=1, column=0, columnspan=4, sticky=EW, pady=20)

    # Form section
    form_frame = ttk.Frame(
        capture_frame,
        bootstyle="light")
    form_frame.grid(row=2, column=0, columnspan=3)

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
    file_naming_entry = create_form_row("File Naming Format:", 0, config["capture"]["file_naming"])
    num_captures_entry = create_form_row("Number of Image Captures:", 1, config["capture"]["num_captures"])
    save_location_entry = create_form_row("Save Location:", 2, config["capture"]["save_location"], True)

    # Browse button with improved styling
    browse_button = ttk.Button(
        form_frame,
        text="Browse",
        command=lambda: browse_directory(save_location_entry),
        bootstyle="secondary outline",
        width=10
    )
    browse_button.grid(column=2, row=2, sticky=W)

    # Footer section with separator and save button
    ttk.Separator(capture_frame).grid(row=3, column=0, columnspan=4, sticky=EW, pady=20)

    # Save button container for better positioning
    button_container = ttk.Frame(capture_frame)
    button_container.grid(row=4, column=0, columnspan=3)

    save_button = ttk.Button(
        button_container,
        text="Save Settings",
        bootstyle="success",
        command=save_capture_settings,
        width=15
    )
    save_button.grid(row=0, column=0, ipady=10)

    # Add tooltips for better UX
    #ToolTip(file_naming_entry, text="Enter the format for naming captured files (e.g., 'page_{n}')")
    #ToolTip(num_captures_entry, text="Enter the number of images to capture")
    #ToolTip(save_location_entry, text="Select where to save captured images")

    return capture_frame