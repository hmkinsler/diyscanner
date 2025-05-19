from src.capture import capture_left_page, capture_right_page
from src.processing import process_images
from scanning.src.pdf_generator import create_pdf_with_ocr

# Utilities
from utils.settings import config

def start_workflow():
    """Run the complete workflow: capture, process, and generate PDF."""
    print("Starting workflow...")

    # Step 1: Capture Images
    print("Capturing images...")
    capture_left_page(config)
    capture_right_page(config)

    # Step 2: Process Images
    print("Processing images...")
    process_images(
        config["capture"]["save_location"],
        config["processing"]["save_location"]
    )

    # Step 3: Generate PDF with OCR
    print("Generating PDF...")
    create_pdf_with_ocr(
        config["processing"]["save_location"],
        f"{config['pdf']['output_location']}/scanned_book.pdf"
    )

    print("Workflow completed successfully!")
