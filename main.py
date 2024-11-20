from src.capture import capture_images
from src.processing import process_images
from src.pdfgenerator import create_pdf
from config.settings import CAPTURED_DIR, PROCESSED_DIR, OUTPUT_DIR

def main():
    # Step 1: Capture images
    print("Starting image capture...")
    capture_images(CAPTURED_DIR, "page_{:03d}.jpg")  # Pass directory and filename pattern
    print(f"Images captured and saved to {CAPTURED_DIR}\n")

    # Step 2: Process images
    print("Starting image processing...")
    process_images(CAPTURED_DIR, PROCESSED_DIR)
    print(f"Images processed and saved to {PROCESSED_DIR}\n")

    # Step 3: Generate PDF
    print("Generating PDF...")
    create_pdf(PROCESSED_DIR, f"{OUTPUT_DIR}/scanned_book.pdf")
    print(f"PDF created and saved to {OUTPUT_DIR}/scanned_book.pdf\n")

if __name__ == "__main__":
    main()
