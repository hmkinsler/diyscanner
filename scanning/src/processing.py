
import os
import numpy as np
import cv2
from PIL import Image, ImageEnhance

from utils.settings import config

def detect_page(input_path): 
    img = cv2.imread(input_path)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(img_gray, 75, 200)
    img_contours, _ = cv2.findContours(img_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if img_contours:
        page_contour = max(img_contours, key=cv2.contourArea)
        epsilon = 0.02 * cv2.arcLength(page_contour, True)
        corners = cv2.approxPolyDP(page_contour, epsilon, True)
        
        if len(corners) == 4:  # Ensure it's a quadrilateral
            return corners

    return None

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

            corners = detect_page(input_path)
            if corners is None:
                print(f"No page detected in {filename}. Skipping.")
                continue

            with Image.open(input_path) as img:
                img = img.resize(resize_dimensions)
                img = img.rotate(rotate_factor)
                img = ImageEnhance.Contrast(img).enhance(contrast_factor)
                img = ImageEnhance.Brightness(img).enhance(brightness_factor)
                img.save(output_path)
                print(f"Processed and saved: {output_path}")