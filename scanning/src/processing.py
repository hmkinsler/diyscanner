
import os
from PIL import Image, ImageEnhance

from utils.settings import config

def process_images(input_dir, output_dir):
    processing_config = config["processing"]
    resize_dimensions = processing_config["resize_dimensions"]
    rotate_factor = processing_config["rotate"]
    contrast_factor = processing_config["contrast"]
    brightness_factor = processing_config["brightness"]
    crop_margins = processing_config["crop_margins"]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpg"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with Image.open(input_path) as img:
                # Resize
                img = img.resize(resize_dimensions)
                # Rotate
                img = img.rotate(rotate_factor)
                # Adjust Contrast
                img = ImageEnhance.Contrast(img).enhance(contrast_factor)
                # Adjust Brightness
                img = ImageEnhance.Brightness(img).enhance(brightness_factor)
                # Crop
                width, height = img.size
                left, top, right, bottom = crop_margins
                img = img.crop((left, top, width - right, height - bottom))
                # Save
                img.save(output_path)
                print(f"Processed and saved: {output_path}")
