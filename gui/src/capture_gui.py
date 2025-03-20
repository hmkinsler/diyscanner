import tkinter as tk
import ttkbootstrap as ttk
import subprocess
import tempfile
from tkinter import messagebox
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

from utils.settings import config
from utils.browse import browse_directory

class CaptureWindow():
    def __init__(self, parent):
        self.parent=parent
        self.settings = config['capture']

        self.build_capture_settings()
        self.load_images()
        self.initialize_meters()

        self.image=None
        self.canvas = None
        self.tk_image = None
        self.current_image = None
        self.image_offset = (0, 0)
        self.image_scale = 1.0

    def load_images(self):
        try:
            image = ImageTk.PhotoImage(Image.open("assets/save_icon.png").resize((50, 50)))
            return image
        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image due to: {str(e)}")

    def initialize_meters(self):
        num_captures = self.settings['num_captures'] * 100
        self.num_captures_meter.configure(amountused=num_captures)
        
        capture_interval = (self.settings['capture_interval']) * 100
        self.capture_interval_meter.configure(amountused=capture_interval)
        
        iso = (self.settings['iso']) * 100
        self.iso_meter.configure(amountused=iso)

        aperture = (self.settings['aperture']) * 100
        self.aperture_meter.configure(amountused=aperture)

        shutter_speed = (self.settings['shutter_speed']) * 100
        self.shutter_speed_meter.configure(amountused=shutter_speed)

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

        # Header frame
        self.header_frame = ttk.LabelFrame(
            master=self.overall_frame,
            bootstyle="light",
            text="Preview Window"
        )
        self.header_frame.pack(fill=BOTH, expand=True)

        # Dynamic frame for settings
        self.canvas = tk.Canvas(
            master=self.header_frame,
            bg="gray",
            highlightthickness=0,
            width=800,  # Fixed width
            height=400  # Fixed height
        )
        self.canvas.pack(fill=BOTH, expand=True)

        # Settings widget frame
        settings_frame = ttk.LabelFrame(
            master=self.overall_frame,
            bootstyle="light",
            text="Capture Settings"
            )
        settings_frame.pack(fill=X)

        #Buttons section
        button_label = ttk.Label(
            master=settings_frame,
            background="#190831",
            bootstyle="dark"
            )
        button_label.pack(side=LEFT, fill=X)

        my_style = ttk.Style()
        my_style.configure(
                "primary.TButton",
                font=("Helvetica", 18),
            )

        capture_button = ttk.Button(
            master=button_label,
            text="Capture Image for Preview",
            bootstyle="success",
            style="primary.TButton",
            padding=10,
            width=25,
            command=self.capture_preview_image,
        ).pack(expand=True, padx=10, pady=10)

        # Meter frame
        meter_frame = ttk.Frame(
            master=settings_frame,
            bootstyle="dark"
        )
        meter_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Meter section one
        meter_label_one = ttk.Label(
            master=meter_frame,
            background="#190831",
            padding=10,
            bootstyle="dark"
        )
        meter_label_one.pack(side=TOP, fill=X, expand=True, ipady=10)

        self.num_captures_meter = ttk.Meter(
            master=meter_label_one,
            metersize=180,
            stripethickness=4,
            amountused=0,
            interactive=True,
            subtext="Number of Captures",
            bootstyle="success",
        )
        self.num_captures_meter.pack(side=LEFT, fill=X, expand= True, padx=10)

        self.capture_interval_meter = ttk.Meter(
            master=meter_label_one,
            metersize=180,
            stripethickness=4,
            amountused=0,
            interactive=True,
            subtext="Capture Interval",
            bootstyle="success",
        )
        self.capture_interval_meter.pack(side=LEFT, fill=X, expand=True, padx=10)

        self.iso_meter = ttk.Meter(
            master=meter_label_one,
            metersize=180,
            stripethickness=4,
            amountused=0,
            amounttotal=360,
            interactive=True,
            subtext="ISO",
            bootstyle="success",
        )
        self.iso_meter.pack(side=RIGHT, fill=X, expand=True, padx=10)

        # Meter label two
        meter_label_two = ttk.Label(
            master=meter_frame,
            background="#190831",
            padding=10,
            bootstyle="dark"
        )
        meter_label_two.pack(side=BOTTOM, fill=X, expand=True, ipady=10)

        self.aperture_meter = ttk.Meter(
            master=meter_label_two,
            metersize=180,
            stripethickness=4,
            amountused=0,
            interactive=True,
            subtext="Contrast",
            bootstyle="success",
        )
        self.aperture_meter.pack(side=LEFT, fill=X, expand=True, padx=10)
        
        self.shutter_speed_meter = ttk.Meter(
            master=meter_label_two,
            metersize=180,
            stripethickness=4,
            amountused=0,
            amounttotal=360,
            interactive=True,
            subtext="Shutter Speed",
            bootstyle="success",
        )
        self.shutter_speed_meter.pack(side=RIGHT, fill=X, expand=True, padx=10)

        self.num_captures_meter.amountusedvar.trace_add('write', self.apply_image_adjustments)
        self.capture_interval_meter.amountusedvar.trace_add('write', self.apply_image_adjustments)
        self.iso_meter.amountusedvar.trace_add('write', self.apply_image_adjustments)
        self.aperture_meter.amountusedvar.trace_add('write', self.apply_image_adjustments)
        self.shutter_speed_meter.amountusedvar.trace_add('write', self.apply_image_adjustments)

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
            self.image=None
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def apply_image_adjustments(self, *args):
        if self.image is None:
            return
        
        working_image=self.image.copy()

        num_captures_factor = self.num_captures_meter.amountusedvar.get() / 100.0
        self.settings['num_captures'] = num_captures_factor
        
        capture_interval_factor = self.capture_interval_meter.amountusedvar.get() / 100.0
        self.settings['capture_interval'] = capture_interval_factor

        iso_factor = self.iso_meter.amountusedvar.get() / 100.0
        self.settings['iso'] = iso_factor

        aperture_factor = self.aperture_meter.amountusedvar.get() / 100.0
        self.settings['aperture'] = aperture_factor

        shutter_speed_factor = self.shutter_speed_meter.amountusedvar.get() / 100.0
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