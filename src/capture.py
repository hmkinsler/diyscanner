#.venv\Scripts\Activate

# you can run the image capture in command prompt to test if need be
# "c:\Program Files (x86)\digiCamControl\CameraControlCmd" /capture /folder "C:\Users\hacks\Documents\diyscannerfiles\testing\captured_dir\test_image.jpg /capture"

import os
import subprocess

def capture_images(output_dir, filename_pattern="image_{:03d}.jpg"):
    """
    Captures images and saves them to the output directory using DigiCamControl.

    Args:
        output_dir (str): Directory to save captured images.
        filename_pattern (str): Pattern for image filenames (e.g., "page_{:03d}.jpg").
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Simulate capturing number of images
    for i in range(1, 5):
        filename = filename_pattern.format(i)
        output_path = os.path.join(output_dir, filename)

        # Use DigiCamControl to capture an image
        command = [
            "C:\\Program Files (x86)\\digiCamControl\\CameraControlCmd.exe",
            "/filename", output_path,
            "/capture"
        ]

        try:
            subprocess.run(command, check=True)
            print(f"Image captured successfully: {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error capturing image {output_path}: {e}")
