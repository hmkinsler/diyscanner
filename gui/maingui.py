# Run with: python -m gui.maingui

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from gui.capture_gui import render_capture_settings
from gui.processing_gui import render_processing_settings
from gui.pdf_gui import render_pdf_settings
from main import start_workflow  # Import the workflow function from main.py
from pathlib import Path
from config.config import config

PATH = Path(__file__).parent / 'assets'

class BookScannerGUI(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        # Configure the root window for resizing
        master.minsize(800, 600)  # Set a minimum window size
        master.grid_rowconfigure(1, weight=1)  # Allow vertical resizing
        master.grid_columnconfigure(1, weight=1)  # Allow horizontal resizing

        # Header Area
        self.create_header(master)

        # Sidebar Buttons
        self.create_sidebar(master)

        # Main Content Frame
        self.create_content_frame(master)

        # Show Default View
        self.show_default_view()

    def create_header(self, master):
        """Create the application header."""
        hdr_frame = ttk.Frame(master, padding=20, bootstyle=SECONDARY)
        hdr_frame.grid(row=0, column=0, columnspan=2, sticky=EW)

        hdr_label = ttk.Label(
            master=hdr_frame,
            text="Book Scanner",
            font=('TkDefaultFont', 24, 'bold'),
            bootstyle=INVERSE
        )
        hdr_label.grid(row=0, column=0, padx=20, sticky=W)

    def create_sidebar(self, master):
        """Create the sidebar for navigation."""
        sidebar_frame = ttk.Frame(master, padding=10, bootstyle=PRIMARY)
        sidebar_frame.grid(row=1, column=0, sticky=NS)

        # Sidebar should grow vertically with the window
        sidebar_frame.grid_rowconfigure(1, weight=1)

        # Sidebar buttons
        ttk.Label(
            sidebar_frame,
            text="Settings",
            font=("TkDefaultFont", 14, 'bold'),
            bootstyle=INVERSE
        ).grid(row=0, column=0, pady=(10, 20), sticky=N)

        ttk.Button(
            sidebar_frame,
            text="Capture Settings",
            bootstyle=INFO,
            command=lambda: render_capture_settings(self.content_frame)
        ).grid(row=1, column=0, pady=5, sticky=EW)

        ttk.Button(
            sidebar_frame,
            text="Processing Settings",
            bootstyle=INFO,
            command=lambda: render_processing_settings(self.content_frame)
        ).grid(row=2, column=0, pady=5, sticky=EW)

        ttk.Button(
            sidebar_frame,
            text="PDF Settings",
            bootstyle=INFO,
            command=lambda: render_pdf_settings(self.content_frame)
        ).grid(row=3, column=0, pady=5, sticky=EW)

        ttk.Button(
            sidebar_frame,
            text="Start Workflow",
            bootstyle=SUCCESS,
            command=start_workflow
        ).grid(row=4, column=0, pady=20, sticky=EW)

        ttk.Button(
            sidebar_frame,
            text="Exit",
            bootstyle=DANGER,
            command=master.quit
        ).grid(row=5, column=0, pady=10, sticky=EW)

    def create_content_frame(self, master):
        """Create the dynamic content area."""
        self.content_frame = ttk.Frame(master, padding=20, bootstyle=LIGHT)
        self.content_frame.grid(row=1, column=1, sticky=NSEW)

        # Allow content frame to resize dynamically
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)

    def show_default_view(self):
        """Display a default welcome view."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        ttk.Label(
            self.content_frame,
            text="Welcome to Book Scanner!",
            font=("TkDefaultFont", 18)
        ).grid(row=0, column=0, pady=20, sticky=NSEW)


if __name__ == '__main__':
    # Create a styled application window
    app = ttk.Window("Book Scanner", "darkly")
    
    # Add the main application frame
    BookScannerGUI(app)
    
    # Start the main loop
    app.mainloop()
