import os
import subprocess
import time
from utils.settings import config

left_pg_cam = "D70"
right_pg_cam = "D3500"

def capture_left_page(config):
    capture_config = config["capture left"]
    output_dir = capture_config["save_location"]
    left_pg_naming = capture_config["left_pg_naming"]
    num_captures = capture_config["num_captures"]
    interval = config["capture left"]["capture_interval"]
    iso = config["capture left"]["iso"]
    aperture = config["capture left"]["aperture"]
    shutter_speed = config["capture left"]["shutter_speed"]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, num_captures + 1):
        filename = left_pg_naming.format(i)
        output_path = os.path.join(output_dir, filename)
        command = [
            "C:\\Program Files (x86)\\digiCamControl\\CameraControlCmd.exe",
            "/filename", output_path,
            "/capture"
        ]
        subprocess.run(command, check=True)
        print(f"Left page image captured: {output_path}")

        if i < num_captures:
            time.sleep(interval)  # Wait before the next capture

def capture_right_page(config):
    capture_config = config["capture right"]
    output_dir = capture_config["save_location"]
    right_pg_naming = capture_config["right_pg_naming"]
    num_captures = capture_config["num_captures"]
    interval = config["capture right"]["capture_interval"]
    iso = config["capture right"]["iso"]
    aperture = config["capture right"]["aperture"]
    shutter_speed = config["capture right"]["shutter_speed"]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, num_captures + 1):
        filename = right_pg_naming.format(i + 1)
        output_path = os.path.join(output_dir, filename)
        command = [
            "C:\\Program Files (x86)\\digiCamControl\\CameraControlCmd.exe",
            "/filename", output_path,
            "/capture"
        ]
        if iso:
            command.extend(["/iso", str(iso)])
        if aperture:
            command.extend(["/aperture", str(aperture)])
        if shutter_speed:
            command.extend(["/shutterspeed", str(shutter_speed)])

        subprocess.run(command, check=True)
        print(f"Right page image captured: {output_path}")

        if i < num_captures:
            time.sleep(interval)  # Wait before the next capture

capture_left_page(config)
capture_right_page(config)