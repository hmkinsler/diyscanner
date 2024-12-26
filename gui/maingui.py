# Run this script with python -m gui.maingui

# Call script dependencies
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkinter import colorchooser
from gui.capture_gui import build_capture_settings
from gui.processing_gui import build_processing_settings
from gui.pdf_gui import build_pdf_settings
from gui.preview_gui import call_preview

# Create frame and define the hierarchy for the GUI
class BookScannerGUI(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)  # Initialize ttk.Frame with the root ("master") window
        self.grid()

        # Create the three main GUI components
        self.create_header()
        self.create_sidebar()
        self.create_content_frame()

        # Show the default view for the content frame on GUI startup
        self.show_default_view()

    # Format the content for GUI header
    def create_header(self):
        self.header_frame = ttk.Frame(self, bootstyle="primary")
        self.header_frame.grid(columnspan=2, sticky="EW")
        print(self.header_frame.grid_size())

        header_label = ttk.Label(
            self.header_frame,
            text="DIY Book Scanner",
            font=("Helvetica", 24, "bold"),
            bootstyle="primary inverse",
            padding=10
        )

        header_label.grid()

    # Format the content for GUI sidebar
    def create_sidebar(self):
        self.sidebar_frame = ttk.Frame(self, bootstyle="primary")
        self.sidebar_frame.grid(column=0, row=1, sticky="NS") 
        print(self.sidebar_frame.grid_size())

        # Sidebar label
        sidebar_label = ttk.Label(
            self.sidebar_frame,
            text="Settings",
            font=("Helvetica", 20, "bold"),
            bootstyle="primary inverse"
        )

        sidebar_label.grid()
        
        # Sidebar buttons
        buttons = [
            ("Image Capture Settings", build_capture_settings, "#4c98d9"),
            ("Image Processing Settings", build_processing_settings, "#4c98d9"),
            ("PDF Settings", build_pdf_settings, "#4c98d9"),
            ("Preview Image Capture", call_preview, "#4c98d9"),
            ("Exit", self.quit_application, "red")
        ]

        for label, command, color in buttons:
            tk.Button(
                self.sidebar_frame,
                text=label,
                font=("Helvetica", 15),
                bg=color,
                command=lambda cmd=command: self.show_content_frame(cmd)
            ).grid()
    
    # Create the dynamic content window, which calls to each of the GUI modular functions
    def create_content_frame(self):
        # First create a container for this content frame
        self.content_container = ttk.Frame(self, bootstyle="dark")
        self.content_container.grid(column=1, row=1)
        print(self.grid_size())
        # And then the actual content frame that fills the container
        self.content_frame = ttk.Frame(self.content_container)
        self.content_frame.grid()

    # Clear the content frame and load new contentS
    def show_content_frame(self, content_builder):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        try:
            # Build and display new content
            if callable(content_builder):
                content = content_builder(self.content_frame)
                if content and isinstance(content, (ttk.Frame, tk.Frame)):
                    content.grid()
        except Exception as e:
            self.show_error_message(f"Error loading content: {str(e)}")

    # Set-up a default view option for when the GUI is opened
    def show_default_view(self):
        self.show_content_frame(self.build_welcome_view)

    def build_welcome_view(self, parent):
        welcome_frame = ttk.Frame(parent)
        welcome_frame.grid()
        # Welcome message
        ttk.Label(
            welcome_frame,
            text="Welcome to DIY Book Scanner!",
            font=("Helvetica", 18),
            bootstyle="light inverse"
        ).grid()
        # User welcome tip(s)
        ttk.Label(
            welcome_frame,
            text="Select an option from the sidebar to begin configuring your scan settings.",
            bootstyle="dark"
        ).grid()

        return welcome_frame
    
    # Error message function for identify issues with calling frames for the dynamic content frame
    def show_error_message(self, message):
        """Display error message in the content frame."""
        error_frame = ttk.Frame(self.content_frame)
        ttk.Label(
            error_frame,
            text=message,
            bootstyle="danger"
        ).grid()
        error_frame.grid()

    # Exit button function
    def quit_application(self):
        self.quit()

if __name__ == "__main__":
    root = ttk.Window(
        title="DIY Book Scanner",
        themename="flatly",
        minsize=(800, 400),
        maxsize=(1000, 600)
    )
    # Add "BookScannerGUI" to the root and make it fill the window
    app = BookScannerGUI(root)
    app.grid()
    print(app.grid_size())

    root.mainloop()
