# This image loader utility is specifically intended for the modular GUI scripts, not including maingui.py
from PIL import Image, ImageTk
from tkinter import messagebox
import os

class ImageLoader:
    @staticmethod
    def load_image(parent, image_path, size=(100,100)):
        try:
            # Get the absolute path relative to the script location
            image_path = os.path.dirname((__file__))
            return ImageTk.PhotoImage(Image.open(image_path).resize(size))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image {image_path}: {str(e)}")
            return None