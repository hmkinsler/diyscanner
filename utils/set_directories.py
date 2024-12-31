import os
from utils.my_paths import capture_save_location, processing_save_location, pdf_output_location

def setup_directories():
    """Ensures all required directories exist."""
    for directory in [capture_save_location, processing_save_location, pdf_output_location]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory exists: {directory}")

if __name__ == "__main__":
    setup_directories()
