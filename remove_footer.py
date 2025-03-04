from PyPDF2 import PdfReader, PdfWriter, PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def create_overlay(page_width, page_height, footer_height):
    """
    Creates a PDF overlay with a white rectangle at the bottom to cover the footer.
    """
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))
    
    # Draw a white rectangle over the footer area
    can.setFillColorRGB(1, 1, 1)  # White color
    can.rect(0, 0, page_width, footer_height, fill=1, stroke=0)
    
    can.save()
    packet.seek(0)
    return PdfReader(packet)

def remove_footer(input_pdf_path, output_pdf_path, footer_height=50):
    """
    Removes the footer from each page of the input PDF and saves the result to output PDF.
    
    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path to save the output PDF file.
    :param footer_height: Height of the footer area to cover (in points).
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    for page_num, page in enumerate(reader.pages):
        page_width = page.mediabox.upper_right[0]
        page_height = page.mediabox.upper_right[1]
        
        # Create overlay
        overlay_pdf = create_overlay(page_width, page_height, footer_height)
        overlay_page = overlay_pdf.pages[0]
        
        # Merge the overlay with the original page
        page.merge_page(overlay_page)
        writer.add_page(page)
        
        print(f"Processed page {page_num + 1}/{len(reader.pages)}")
    
    # Write the output PDF
    with open(output_pdf_path, 'wb') as out_file:
        writer.write(out_file)
    
    print(f"Footer removed. Output saved to {output_pdf_path}")

if __name__ == "__main__":
    input_pdf = "input.pdf"       # Replace with your input PDF file path
    output_pdf = "output.pdf"     # Replace with desired output PDF file path
    footer_height = 12            # Adjust based on your footer size
    
    remove_footer(input_pdf, output_pdf, footer_height)
