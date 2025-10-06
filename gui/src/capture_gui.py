import tkinter as tk
import ttkbootstrap as ttk
import subprocess
import tempfile
from tkinter import messagebox
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageEnhance

from utils.settings import config

class CaptureWindow:
    def __init__(self, parent):
        self.parent = parent
        self.l_settings = config['capture left']
        self.r_settings = config['capture right']
        
        self.image = None
        self.canvas = None
        self.tk_image = None
        self.current_image = None
        self.image_offset = (0, 0)
        self.image_scale = 1.0
        
        self.build_capture_settings()

    def build_capture_settings(self):
        settings = ["num_captures", "capture_interval", "iso", "aperture", "shutter_speed"]
        setting_names = ["Number of Captures", "Capture Interval", "ISO", "Aperture", "Shutter Speed"]

        # Main frame
        self.overall_frame = ttk.Frame(
            master=self.parent, 
            bootstyle="dark",
            padding=10)
        self.overall_frame.pack(fill=BOTH, expand=True)

        label_frame_style = ttk.Style()
        label_frame_style.configure(
            "light.TLabelframe.Label",
            font=("Helvetica", 20)
        )

        # Header frames
        self.l_header_frame = ttk.LabelFrame(
            master=self.overall_frame,
            bootstyle="light",
            text="Left Page Camera Settings"
        )
        self.l_header_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.r_header_frame = ttk.LabelFrame(
            master=self.overall_frame,
            bootstyle="light",
            text="Right Page Camera Settings"
        )
        self.r_header_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Dynamic frame for settings
        self.l_canvas = tk.Canvas(
            master=self.l_header_frame,
            bg="gray",
            highlightthickness=0,
            width=400,  # Fixed width
            height=200  # Fixed height
        )
        self.l_canvas.pack(fill=BOTH, expand=True)

        self.r_canvas = tk.Canvas(
            master=self.r_header_frame,
            bg="gray",
            highlightthickness=0,
            width=400,  # Fixed width
            height=200  # Fixed height
        )
        self.r_canvas.pack(fill=BOTH, expand=True)

        # Settings widget frames
        l_settings_frame = ttk.Frame(
            master=self.l_header_frame,
            bootstyle="light",
            )
        l_settings_frame.pack(fill=X)

        r_settings_frame = ttk.Frame(
            master=self.r_header_frame,
            bootstyle="light",
            )
        r_settings_frame.pack(fill=X)

        #Buttons sections
        l_button_label = ttk.Label(
            master=l_settings_frame,
            background="#190831",
            bootstyle="dark"
            )
        l_button_label.pack(fill=X)

        r_button_label = ttk.Label(
            master=r_settings_frame,
            background="#190831",
            bootstyle="dark"
            )
        r_button_label.pack(fill=X)

        my_style = ttk.Style()
        my_style.configure(
                "primary.TButton",
                font=("Helvetica", 18),
            )

        l_capture_button = ttk.Button(
            master=l_button_label,
            text="Capture Image for Preview",
            bootstyle="success",
            style="primary.TButton",
            padding=10,
            width=25,
            command=self.capture_l_preview_image,
        ).pack(side=TOP, expand=True, padx=30, pady=10)

        r_capture_button = ttk.Button(
            master=r_button_label,
            text="Capture Image for Preview",
            bootstyle="success",
            style="primary.TButton",
            padding=10,
            width=25,
            command=self.capture_r_preview_image,
        ).pack(side=TOP, expand=True, padx=30, pady=10)

        # Entry frames 
        l_entry_frame = ttk.Frame(
            master=l_settings_frame,
            padding=30,
            bootstyle="dark"
            )
        l_entry_frame.pack(fill=BOTH, expand=TRUE, ipady=5)

        r_entry_frame = ttk.Frame(
            master=r_settings_frame,
            padding=30,
            bootstyle="dark"
            )
        r_entry_frame.pack(fill=BOTH, expand=TRUE, ipady=5)

        def create_l_form_row(label_text, entry_var=None):
            # Container for each row
            row_frame = ttk.Frame(
                master=l_entry_frame,
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
            entry.pack()
            
            if entry_var is not None:
                entry.insert(0, str(entry_var))
                
            return entry
        
        def create_r_form_row(label_text, entry_var=None):
            # Container for each row
            row_frame = ttk.Frame(
                master=r_entry_frame,
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
            entry.pack()
            
            if entry_var is not None:
                entry.insert(0, str(entry_var))
                
            return entry
        
        for a, b in zip(settings, setting_names):
            config_setting = str(a)
            create_l_form_row(b, config["capture left"][config_setting])
            create_r_form_row(b, config["capture right"][config_setting])

    def capture_l_preview_image(self):
        try:
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                test_image_path = temp_file.name

            command = [
                r"c:\Program Files (x86)\digiCamControl\CameraControlCmd.exe",
                "/capture",
                "/filename", test_image_path,
            ]
            subprocess.run(command, check=True)

            self.l_image = Image.open(test_image_path)
            self.update_l_preview(self.l_image)
            
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to capture the test image. Check your camera connection.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def update_l_preview(self, l_image):
        # Get canvas dimensions
        canvas_width = self.l_canvas.winfo_width()
        canvas_height = self.l_canvas.winfo_height()
        
        if canvas_width == 1:  # Canvas not yet realized
            canvas_width = 200  # Default width
            canvas_height = 200  # Default height
        
        # Calculate scaling factor to fit image in canvas
        img_width, img_height = l_image.size
        scale_w = canvas_width / img_width
        scale_h = canvas_height / img_height
        scale = min(scale_w, scale_h)
        
        # Store current scale for coordinate conversion
        self.l_image_scale = scale
        
        # Calculate new dimensions
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        
        # Resize image
        l_resized_image = l_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Store current image for cropping reference
        self.current_image = l_resized_image
        
        # Update canvas
        self.tk_image = ImageTk.PhotoImage(l_resized_image)
        self.l_canvas.delete("all")  # Clear previous image
        
        # Center the image in canvas
        x_offset = (canvas_width - new_width) // 2
        y_offset = (canvas_height - new_height) // 2
        
        # Store offset for coordinate conversion
        self.image_offset = (x_offset, y_offset)
        
        # Create image on canvas
        self.l_canvas.create_image(x_offset, y_offset, anchor=tk.NW, image=self.tk_image)

    def capture_r_preview_image(self):
        try:
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                test_image_path = temp_file.name

            command = [
                r"c:\Program Files (x86)\digiCamControl\CameraControlCmd.exe",
                "/capture",
                "/filename", test_image_path,
            ]
            subprocess.run(command, check=True)

            self.r_image = Image.open(test_image_path)
            self.update_r_preview(self.r_image)
            
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to capture the test image. Check your camera connection.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def update_r_preview(self, r_image):
        # Get canvas dimensions
        canvas_width = self.r_canvas.winfo_width()
        canvas_height = self.r_canvas.winfo_height()
        
        if canvas_width == 1:  # Canvas not yet realized
            canvas_width = 200  # Default width
            canvas_height = 200  # Default height
        
        # Calculate scaling factor to fit image in canvas
        img_width, img_height = r_image.size
        scale_w = canvas_width / img_width
        scale_h = canvas_height / img_height
        scale = min(scale_w, scale_h)
        
        # Store current scale for coordinate conversion
        self.r_image_scale = scale
        
        # Calculate new dimensions
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        
        # Resize image
        r_resized_image = r_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Store current image for cropping reference
        self.current_image = r_resized_image
        
        # Update canvas
        self.tk_image = ImageTk.PhotoImage(r_resized_image)
        self.r_canvas.delete("all")  # Clear previous image
        
        # Center the image in canvas
        x_offset = (canvas_width - new_width) // 2
        y_offset = (canvas_height - new_height) // 2
        
        # Store offset for coordinate conversion
        self.image_offset = (x_offset, y_offset)
        
        # Create image on canvas
        self.r_canvas.create_image(x_offset, y_offset, anchor=tk.NW, image=self.tk_image)

def build_capture_settings(parent):
    return CaptureWindow(parent)