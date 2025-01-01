import os
import subprocess

def capture_images(config):
    capture_config = config["capture"]
    output_dir = capture_config["save_location"]
    file_naming = capture_config["file_naming"]
    num_captures = capture_config["num_captures"]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, num_captures + 1):
        filename = file_naming(i)
        output_path = os.path.join(output_dir, filename)
        command = [
            "C:\\Program Files (x86)\\digiCamControl\\CameraControlCmd.exe",
            "/filename", output_path,
            "/capture"
        ]
        subprocess.run(command, check=True)
        print(f"Image captured: {output_path}")

