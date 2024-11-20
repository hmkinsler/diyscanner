from fpdf import FPDF  # Import the FPDF class
import os

def create_pdf(image_dir, output_pdf):
    """Creates a PDF from processed images."""
    pdf = FPDF()  # Instantiate the FPDF class
    for filename in sorted(os.listdir(image_dir)):
        if filename.lower().endswith(".jpg"):
            pdf.add_page()
            pdf.image(os.path.join(image_dir, filename), x=10, y=10, w=190)
    pdf.output(output_pdf)
    print(f"PDF created: {output_pdf}")
