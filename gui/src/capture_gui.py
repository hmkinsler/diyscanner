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
        self.initialize_l_entries()
        self.initialize_r_entries()

    def initialize_l_entries(self):
        num_captures = self.l_settings['num_captures']
        capture_interval = (self.l_settings['capture_interval'])
        iso = (self.l_settings['iso'])
        aperture = (self.l_settings['aperture'])
        shutter_speed = (self.l_settings['shutter_speed'])

    def initialize_r_entries(self):
        num_captures = self.r_settings['num_captures']
        capture_interval = (self.r_settings['capture_interval'])
        iso = (self.r_settings['iso'])
        aperture = (self.r_settings['aperture'])
        shutter_speed = (self.r_settings['shutter_speed'])

    def build_capture_settings(self):
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
            command=self.capture_preview_image,
        ).pack(side=TOP, expand=True, padx=30, pady=10)

        r_capture_button = ttk.Button(
            master=r_button_label,
            text="Capture Image for Preview",
            bootstyle="success",
            style="primary.TButton",
            padding=10,
            width=25,
            command=self.capture_preview_image,
        ).pack(side=TOP, expand=True, padx=30, pady=10)

    def capture_preview_image(self):
        try:
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                test_image_path = temp_file.name

            command = [
                r"c:\Program Files (x86)\digiCamControl\CameraControlCmd.exe",
                "/capture",
                "/filename", test_image_path,
            ]
            subprocess.run(command, check=True)

            self.image = Image.open(test_image_path)
            self.update_preview(self.image)
            
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to capture the test image. Check your camera connection.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def apply_image_adjustments(self, *args):
        if self.image is None:
            return
        
        working_image=self.image.copy()

        num_captures_factor = self.num_captures_meter.amountusedvar.get()
        self.settings['num_captures'] = num_captures_factor
        
        capture_interval_factor = self.capture_interval_meter.amountusedvar.get()
        self.settings['capture_interval'] = capture_interval_factor

        iso_factor = self.iso_meter.amountusedvar.get()
        self.settings['iso'] = iso_factor

        aperture_factor = self.aperture_meter.amountusedvar.get()
        self.settings['aperture'] = aperture_factor

        shutter_speed_factor = self.shutter_speed_meter.amountusedvar.get()
        self.settings['shutter_speed'] = shutter_speed_factor

        # Update the preview
        self.update_preview(working_image)

    def update_preview(self, image):
        # Get canvas dimensions
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width == 1:  # Canvas not yet realized
            canvas_width = 800  # Default width
            canvas_height = 600  # Default height
        
        # Calculate scaling factor to fit image in canvas
        img_width, img_height = image.size
        scale_w = canvas_width / img_width
        scale_h = canvas_height / img_height
        scale = min(scale_w, scale_h)
        
        # Store current scale for coordinate conversion
        self.image_scale = scale
        
        # Calculate new dimensions
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        
        # Resize image
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Store current image for cropping reference
        self.current_image = resized_image
        
        # Update canvas
        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas.delete("all")  # Clear previous image
        
        # Center the image in canvas
        x_offset = (canvas_width - new_width) // 2
        y_offset = (canvas_height - new_height) // 2
        
        # Store offset for coordinate conversion
        self.image_offset = (x_offset, y_offset)
        
        # Create image on canvas
        self.canvas.create_image(x_offset, y_offset, anchor=tk.NW, image=self.tk_image)

def build_capture_settings(parent):
    return CaptureWindow(parent)
