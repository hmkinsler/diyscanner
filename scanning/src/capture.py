import os
import subprocess
import time

def capture_images(config):
    capture_config = config["capture"]
    output_dir = capture_config["save_location"]
    file_naming = capture_config["file_naming"]
    num_captures = capture_config["num_captures"]
    interval = config["capture"]["capture_interval"]
    iso = config["capture"]["iso"]
    aperture = config["capture"]["aperture"]
    shutter_speed = config["capture"]["shutter_speed"]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, num_captures + 1):
        filename = file_naming.format(i)
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
        print(f"Image captured: {output_path}")

        if i < num_captures:
            time.sleep(interval)  # Wait before the next capture

