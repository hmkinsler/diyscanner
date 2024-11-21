from fpdf import FPDF
from PIL import Image
import pytesseract
import os

def create_pdf_with_ocr(image_dir, output_pdf):
    """
    Generate a PDF from processed images and add OCR text layers.

    Args:
        image_dir (str): Directory containing processed images.
        output_pdf (str): Path to the output PDF.
    """
    pdf = FPDF()
    temp_text_file = "temp_ocr.txt"  # Temporary file for OCR text

    for filename in sorted(os.listdir(image_dir)):
        if filename.lower().endswith(".jpg"):
            image_path = os.path.join(image_dir, filename)
            
            # Add image to the PDF
            pdf.add_page()
            pdf.image(image_path, x=10, y=10, w=190)
            
            # Perform OCR on the image
            print(f"Performing OCR on {filename}...")
            text = pytesseract.image_to_string(Image.open(image_path))
            
            # Save OCR text to the PDF
            with open(temp_text_file, "w") as f:
                f.write(text)
            pdf.set_xy(10, 250)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text)
            
    # Save the PDF
    pdf.output(output_pdf)
    print(f"PDF with OCR created: {output_pdf}")

    # Clean up temporary files
    if os.path.exists(temp_text_file):
        os.remove(temp_text_file)
