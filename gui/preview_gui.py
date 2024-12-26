#this is meant to define the "preview image" window in the GUI, so that the user can view the images and make image adjustment settings before beginning to scan

import os
import subprocess
import tempfile
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import messagebox
from config.config import config
from PIL import Image, ImageTk, ImageOps, ImageEnhance


# Preview Functionality
def call_preview(content_frame):
    """
    Captures a test image, saves it temporarily, and previews it in the GUI.
    """
    try:
        # Step 1: Create a temporary directory to store the test image
        temp_dir = tempfile.gettempdir()
        test_image_path = os.path.join(temp_dir, "test_preview.jpg")
        
        # Step 2: Run the camera capture command (DigiCamControl)
        # Update this line with your actual DigiCamControl CommandLine call
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
            img = img.rotate

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
            photo = ImageTk.PhotoImage(img)

        # Add the image to the content_frame
        ttk.Label(content_frame, text="Preview Image").grid(pady=10)
        img_label = ttk.Label(content_frame, image=photo)
        img_label.image = photo  # Keep a reference to avoid garbage collection
        img_label.grid()

        ttk.Label(content_frame, text="Preview successful!").grid(pady=10)

    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to capture the test image. Check your camera connection.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
