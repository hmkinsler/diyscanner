
import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance

from utils.settings import config

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