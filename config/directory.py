import os
from config.settings import CAPTURED_DIR, PROCESSED_DIR, OUTPUT_DIR

def setup_directories():
    """Ensures all required directories exist."""
    for directory in [CAPTURED_DIR, PROCESSED_DIR, OUTPUT_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory exists: {directory}")

if __name__ == "__main__":
    setup_directories()
