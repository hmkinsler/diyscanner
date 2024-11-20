import os
from PIL import Image, ImageEnhance  # Correctly import from Pillow

def process_images(input_dir, output_dir):
    """Processes images by resizing and enhancing contrast."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpg"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            try:
                with Image.open(input_path) as img:
                    img = img.resize((1024, 768))  # Resize
                    enhancer = ImageEnhance.Contrast(img)
                    img = enhancer.enhance(1.5)  # Enhance contrast
                    img.save(output_path)
                    print(f"Processed and saved: {output_path}")
            except Exception as e:
                print(f"Error processing {input_path}: {e}")
