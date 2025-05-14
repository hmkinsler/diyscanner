import tkinter as tk
import ttkbootstrap as ttk
import subprocess
import tempfile
import cv2
import numpy as np
from tkinter import messagebox
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageEnhance

from utils.settings import config
from scanning.src.processing import detect_page

class ProcessingWindow:
    def __init__(self, parent):
        self.parent = parent
        self.preview_label = None
        self.crop_rect_id = None
        self.start_x = self.start_y = None
        self.crop_coords = None
        self.image = None
        self.canvas = None
        self.tk_image = None
        self.current_image = None
        self.image_offset = (0, 0)
        self.image_scale = 1.0
        
        self.settings = config['processing']
        self.build_processing_preview()
        self.initialize_meters()

    def initialize_meters(self):
        # Convert rotation to degrees (0-360)
        rotation = self.settings['rotate'] % 360
        self.rotate_meter.configure(amountused=rotation)
        
        # Convert contrast to percentage (0-100)
        contrast = (self.settings['contrast'] - 1.0) * 100
        self.contrast_meter.configure(amountused=contrast)
        
        # Convert brightness to percentage (0-100)
        brightness = (self.settings['brightness'] - 1.0) * 100
        self.brightness_meter.configure(amountused=brightness)

    def build_processing_preview(self):
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

        # Bind canvas events
        self.canvas.bind("<ButtonPress-1>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.update_crop)
        self.canvas.bind("<ButtonRelease-1>", self.finish_crop)

        # Settings widget frame
        settings_frame = ttk.LabelFrame(
            master=self.overall_frame,
            bootstyle="light",
            text="Processing Settings"
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
        ).pack(side=TOP, expand=True, padx=30, pady=10)

        cropping_button = ttk.Button(
            master=button_label,
            text="Apply Cropping",
            bootstyle="success",
            style="primary.TButton",
            padding=10,
            width=25,
            command=self.apply_crop,
        ).pack(side=BOTTOM, expand=True, padx=30, pady=10)

        # Meter section
        meter_label = ttk.Label(
            master=settings_frame,
            background="#190831",
            padding=10,
            bootstyle="dark"
        )
        meter_label.pack(side=RIGHT, fill=X, expand=True, ipady=10)

        self.brightness_meter = ttk.Meter(
            master=meter_label,
            metersize=180,
            stripethickness=4,
            amountused=0,
            interactive=True,
            subtext="Brightness",
            bootstyle="success",
        )
        self.brightness_meter.pack(side=LEFT, fill=X, expand= True, padx=10)

        self.contrast_meter = ttk.Meter(
            master=meter_label,
            metersize=180,
            stripethickness=4,
            amountused=0,
            interactive=True,
            subtext="Contrast",
            bootstyle="success",
        )
        self.contrast_meter.pack(side=LEFT, fill=X, expand=True, padx=10)

        self.rotate_meter = ttk.Meter(
            master=meter_label,
            metersize=180,
            stripethickness=4,
            amountused=0,
            amounttotal=360,
            interactive=True,
            subtext="Rotate",
            bootstyle="success",
        )
        self.rotate_meter.pack(side=RIGHT, fill=X, expand=True, padx=10)

        self.brightness_meter.amountusedvar.trace_add('write', self.apply_image_adjustments)
        self.contrast_meter.amountusedvar.trace_add('write', self.apply_image_adjustments)
        self.rotate_meter.amountusedvar.trace_add('write', self.apply_image_adjustments)

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

        # Apply brightness
        brightness_factor = self.brightness_meter.amountusedvar.get() / 100.0
        if brightness_factor != 0:
            enhancer = ImageEnhance.Brightness(working_image)
            working_image = enhancer.enhance(1.0 + brightness_factor)
            # Update settings
            self.settings['brightness'] = 1.0 + brightness_factor
        
        # Apply contrast
        contrast_factor = self.contrast_meter.amountusedvar.get() / 100.0
        if contrast_factor != 0:
            enhancer = ImageEnhance.Contrast(working_image)
            working_image = enhancer.enhance(1.0 + contrast_factor)
            # Update settings
            self.settings['contrast'] = 1.0 + contrast_factor
        
        # Apply rotation
        rotation_angle = self.rotate_meter.amountusedvar.get()
        if rotation_angle != 0:
            working_image = working_image.rotate(rotation_angle, expand=True)
            # Update settings
            self.settings['rotate'] = rotation_angle

        # Update the preview
        self.update_preview(working_image)

    def update_preview(self, image):
        # Detect crop directly on the test image
        corners = detect_page(image)
        if corners:
            x, y, w, h = cv2.boundingRect(corners)
            crop = {"x": x, "y": y, "w": w, "h": h}

            # Apply cropping
            image = image.crop((crop["x"], crop["y"], crop["x"] + crop["w"], crop["y"] + crop["h"]))
        else:
            print("No crop detected for the test image.")

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

    def apply_crop(self):
        if not self.crop_coords or not self.current_image:
            messagebox.showwarning("No Crop Defined", "Please define a crop area first.")
            return

        # Get crop coordinates relative to canvas
        x1, y1, x2, y2 = self.crop_coords
        
        # Convert canvas coordinates to image coordinates
        x_offset, y_offset = self.image_offset
        scale = self.image_scale
        
        # Adjust coordinates for image position and scale
        img_x1 = max(0, int((x1 - x_offset) / scale))
        img_y1 = max(0, int((y1 - y_offset) / scale))
        img_x2 = min(self.image.width, int((x2 - x_offset) / scale))
        img_y2 = min(self.image.height, int((y2 - y_offset) / scale))
        
        # Apply crop to original image
        cropped_image = self.image.crop((img_x1, img_y1, img_x2, img_y2))
        0
        # Update the preview with cropped image
        self.image = cropped_image  # Update original image
        self.update_preview(cropped_image)
        
        # Clear crop rectangle
        if self.crop_rect_id:
            self.canvas.delete(self.crop_rect_id)
            self.crop_rect_id = None
            self.crop_coords = None
    
        # Update settings with new crop margins
        self.settings['crop_margins'] = (img_x1, img_y1, img_x2, img_y2)

    def start_crop(self, event):
        if not self.current_image:
            return
            
        # Get mouse position relative to canvas
        self.start_x = event.x
        self.start_y = event.y
        
        # Clear existing crop rectangle
        if self.crop_rect_id:
            self.canvas.delete(self.crop_rect_id)
            
        # Create new crop rectangle
        self.crop_rect_id = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y,
            outline="red",
            width=2
        )

    def update_crop(self, event):
        if not self.current_image or not self.crop_rect_id:
            return
            
        # Get canvas boundaries
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Constrain coordinates to canvas
        x = min(max(0, event.x), canvas_width)
        y = min(max(0, event.y), canvas_height)
        
        # Update rectangle
        self.canvas.coords(self.crop_rect_id, self.start_x, self.start_y, x, y)

    def finish_crop(self, event):
        if not self.current_image or not self.crop_rect_id:
            return
            
        # Get final coordinates
        coords = self.canvas.coords(self.crop_rect_id)
        
        # Convert to image coordinates
        x_offset, y_offset = self.image_offset
        x1, y1, x2, y2 = coords
        
        # Sort coordinates (in case of negative rectangle)
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        
        # Store crop coordinates
        self.crop_coords = (x1, y1, x2, y2)
        
        # Optional: Show feedback
        if self.crop_coords:
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            messagebox.showinfo("Crop Defined", 
                              f"Crop area defined: {width:.0f}x{height:.0f} pixels")

def build_processing_preview(parent):
    return ProcessingWindow(parent)
