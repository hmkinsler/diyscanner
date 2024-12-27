# Run this script with python -m gui.maingui

# Libraries
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Functions from other scripts
from gui.capture_gui import build_capture_settings
from gui.processing_gui import build_processing_settings
from gui.pdf_gui import build_pdf_settings
from gui.preview_gui import call_preview

class BookScanningApp(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.load_images()
        self.create_sidebar()
        self.create_dynamic_frame()

    def load_images(self):
        try:
            # self.window_icon = ImageTk.PhotoImage(Image.open("images/wingow.png")) # I have not yet made this logo file
            self.logo_icon = ImageTk.PhotoImage(Image.open("gui/images/logo.png").resize((100,100)))
            self.capture_icon = ImageTk.PhotoImage(Image.open("gui/images/capture.png").resize((50,50)))
            self.processing_icon = ImageTk.PhotoImage(Image.open("gui/images/processing.png").resize((50,50)))
            self.pdf_icon = ImageTk.PhotoImage(Image.open("gui/images/pdf.png").resize((50,50)))
            self.preview_icon = ImageTk.PhotoImage(Image.open("gui/images/preview.png").resize((50,50)))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load images: {str(e)}")

    
    def create_sidebar(self):
        overall_frame = ttk.Frame(
            master=self,
            padding=10,
            bootstyle="primary"
        )
        overall_frame.pack(side=LEFT, fill=BOTH)
        
        sidebar_frame = ttk.Frame(
            master=overall_frame,
            padding=20,
            bootstyle="dark"
        )
        sidebar_frame.pack(side=LEFT, fill=BOTH)
        
        lbl = ttk.Label(
            master=sidebar_frame,
            text="Workflow Settings",
            font=("Helvetica", 25, "bold"),
            anchor=CENTER,
            bootstyle="dark inverse"
        )
        lbl.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5)

        buttons = [
            ("Image Capture Settings", build_capture_settings, self.capture_icon),
            ("Image Processing Settings", build_processing_settings, self.processing_icon),
            ("PDF Settings", build_pdf_settings, self.pdf_icon),
            ("Preview Image Capture", call_preview, self.preview_icon),
        ]

        my_style = ttk.Style()
        my_style.configure(
            "primary.Outline.TButton",
            font=("Helvetica", 18),
            foreground="#4bd2e6"
        )

        for label, command, icon in buttons:
            ttk.Button(
                sidebar_frame,
                text=f" {label}",
                image=icon,
                compound="left",
                bootstyle="dark",
                style="primary.Outline.TButton",
                width=23,
                command=lambda cmd=command: self.show_content_frame(cmd)
            ).pack(side=TOP, expand=YES, ipady=10)

    def create_dynamic_frame(self):
        self.dynamic_frame = ttk.Frame(
            master=self,
            padding=10,
            bootstyle="primary",
            width=500,
            height=200
        )
        self.dynamic_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE, ipadx=30, ipady=20)

        self.subframe = ttk.Frame(
            master=self.dynamic_frame,
            padding=10,
            bootstyle="dark"
        )
        self.subframe.pack(side=RIGHT, fill=BOTH, expand=TRUE, ipadx=30, ipady=20)

        welcome_header = ttk.Label(
            master=self.subframe,
            text=" Welcome to DIY Book Scanner!",
            font=("Helvetica", 31, "bold"),
            image=self.logo_icon,
            compound=LEFT,
            anchor=CENTER,
            bootstyle="dark inverse"
        ).pack(side=TOP, fill=BOTH, ipady=10)

        user_tip = ttk.Label(
            master=self.subframe,
            text="Select an option from the sidebar to begin configuring your scan settings.\n\n\nRemember to test your settings via 'Image Preview.'\n\n\nFor more information about this software project, you can reach out to the primary project researcher, Haley Kinsler, at hmkinsle@ncsu.edu",
            font=("Helvetica", 24),
            wraplength=700,
            justify="left",
            anchor=CENTER,
            bootstyle="dark inverse"
        ).pack(side=TOP, fill=BOTH, ipady=20)

    def show_content_frame(self, content_builder):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()
        
        try:
            # Build and display new content
            if callable(content_builder):
                content_builder(self.dynamic_frame)
                if content_builder and isinstance(content_builder, ttk.Frame):
                    return isinstance
        except Exception as e:
            self.show_error_message(f"Error loading content: {str(e)}")

    def show_error_message(self, message):
        error_frame = ttk.Frame(
            master=self.dynamic_frame,
            padding=10,
            bootstyle="danger"
            )
        error_frame.pack(fill=BOTH, expand=TRUE)

        error_message = ttk.Label(
            master=error_frame,
            text=message,
            bootstyle="danger"
        ).pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)
        
if __name__ == "__main__":

    app = ttk.Window(
        title="DIY Book Scanner", 
        themename="vapor", 
        resizable=(False, False),
        minsize=(1200,600),
        maxsize=(1200,600)
    )
    BookScanningApp(app)
    app.mainloop()
