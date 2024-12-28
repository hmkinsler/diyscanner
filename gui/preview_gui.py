# This is meant to define the "preview image" window in the GUI, so that the user can view the images and make image adjustment settings before beginning to scan

# Libraries
import os
import subprocess
import tempfile
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps, ImageEnhance

# Utilities
from config.config import config

class PreviewWindow():
    def __init__(self, parent):
        self.parent=parent
        self.preview_label = None
        self.build_preview()

        # Preview Functionality
    def build_preview(self):
        # Main frame
        overall_frame = ttk.Frame(
                self.parent,
                bootstyle="dark",
                padding=20
                )
        overall_frame.pack(fill=BOTH, expand=True)

        # Header section  
        header_divider = ttk.Separator(
            master=overall_frame,
            bootstyle="light")
        header_divider.pack(fill=X, pady=20)

        self.preview_holder = ttk.Frame(
            master=overall_frame,
            bootstyle="dark"
        )
        self.preview_holder.pack(fill=BOTH, expand=True)

        self.preview_label = ttk.Label(
            master=self.preview_holder,
            anchor=CENTER,
            background="#2b2b2b",
            bootstyle="dark"
        )
        self.preview_label.pack(fill=BOTH, expand=True)

        # Frame for button to start preview process
        button_frame = ttk.Frame(
            master=overall_frame,
            bootstyle = "dark"
        )
        button_frame.pack(side=BOTTOM, fill=BOTH, ipadx=10, ipady=10)

        first_button_divider = ttk.Separator(
            master=button_frame,
            bootstyle="light")
        first_button_divider.pack(fill=X, pady=20)

        second_button_divider = ttk.Separator(
            master=button_frame,
            bootstyle="light")
        second_button_divider.pack(side=BOTTOM, fill=X, pady=20)

        footer_label = ttk.Label(
            master=button_frame,
            text="Preview Image:",
                font=("Helvetica", 31, "bold"),
                anchor=CENTER,
                bootstyle="dark inverse"
        ).pack(side=LEFT, fill=Y, expand=True, ipady=10)

        my_style = ttk.Style()
        my_style.configure(
                "success.Outline.TButton",
                font=("Helvetica", 18),
                foreground="#40ee84"
            )

        begin_preview_button = ttk.Button(
            master=button_frame,
            text="Capture Image for Preview",
            bootstyle="success",
            style="success.Outline.TButton",
            width=30,
            command=lambda: self.capture_preview_image()
        )
        begin_preview_button.pack(side=RIGHT, fill=Y, expand=True, ipady=10)

    def capture_preview_image(self):
        try:
            # Step 1: Create temporary file
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                test_image_path = temp_file.name
            
            # Step 2: Run the camera capture command (DigiCamControl)
            command = [
                r"c:\Program Files (x86)\digiCamControl\CameraControlCmd.exe",
                "/capture",
                "/filename", test_image_path
            ]
            subprocess.run(command, check=True)
        
            # Step 3: Apply processing settings
            with Image.open(test_image_path) as img:
                processing_settings = config["processing"]

                # Apply Resize
                resize_dims = processing_settings.get("resize_dimensions", (400, 300))
                img = img.resize(resize_dims, Image.Resampling.LANCZOS)

                # Apply rotate
                rotate_value = processing_settings.get("rotate", 270)
                img = img.rotate(rotate_value)

                # Apply Contrast
                contrast_value = processing_settings.get("contrast", 1.0)
                img = ImageEnhance.Contrast(img).enhance(contrast_value)

                # Apply Brightness
                brightness_value = processing_settings.get("brightness", 1.0)
                img = ImageEnhance.Brightness(img).enhance(brightness_value)

                # Apply Crop Margins
                crop_margins = processing_settings.get("crop_margins", (0, 0, 0, 0))
                left, top, right, bottom = crop_margins
                img_width, img_height = img.size
                img = img.crop((left, top, img_width - right, img_height - bottom))

                # Resize for Preview Display
                img = img.resize((400, 300), Image.Resampling.LANCZOS)

                # Convert to PhotoImage for display
                photo_image = ImageTk.PhotoImage(img)

                # Store photo reference to prevent garbage collection
                self.preview_label.image_names = photo_image

                # Update the label with the new image
                self.preview_label.configure(image=photo_image)
            
            # Clean temporary file
            os.unlink(test_image_path)

        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to capture the test image. Check your camera connection.")

        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def build_preview(parent):
    return PreviewWindow(parent)

