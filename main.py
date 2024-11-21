from src.capture import capture_images
from src.processing import process_images
from src.pdfgenerator import create_pdf_with_ocr
from config.config import config

def start_workflow():
    """Run the complete workflow: capture, process, and generate PDF."""
    print("Starting workflow...")

    # Step 1: Capture Images
    print("Capturing images...")
    capture_images(config)

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
