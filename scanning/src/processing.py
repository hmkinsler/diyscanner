
import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance

from utils.settings import config

def detect_page(image_or_path):
    if isinstance(image_or_path, str):
        img = cv2.imread(image_or_path)
        original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply GaussianBlur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Perform edge detection
        edged = cv2.Canny(blurred, 50, 150)
        
        # Find contours
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter out the largest contour (assumed to be the book)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        largest_contour = contours[0]
        
        # Get bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        center_x = x + w // 2
        
        # Define the right page box
        right_page_box = (center_x, y, x + w, y + h)
        
        # Convert to PIL format and crop the right page
        pil_image = Image.fromarray(original)
        right_page = pil_image.crop(right_page_box)
        
        return right_page

def process_images(input_dir, output_dir):
    processing_config = config["processing"]
    resize_dimensions = processing_config["resize_dimensions"]
    rotate_factor = processing_config["rotate"]
    contrast_factor = processing_config["contrast"]
    brightness_factor = processing_config["brightness"]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.__contains__((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with Image.open(input_path) as img:
                img = img.resize(resize_dimensions)
                img = img.rotate(rotate_factor)
                img = ImageEnhance.Contrast(img).enhance(contrast_factor)
                img = ImageEnhance.Brightness(img).enhance(brightness_factor)
                img.save(output_path)
                print(f"Processed and saved: {output_path}")