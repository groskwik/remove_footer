# PDF Footer Removal Script

This Python script removes footers from each page of a specified PDF document by overlaying a white rectangle over the footer area. It utilizes the [PyPDF2](https://pypi.org/project/PyPDF2/) library for reading and writing PDF files and the [ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf) library for creating the overlay.

## Features

- **Footer Removal**: Overlays a white rectangle over the footer area of each page in a PDF document.
- **Customizable Footer Height**: Allows specification of the footer height to accurately cover the footer content.

## Requirements

- **Python 3.x**
- **PyPDF2**: Library for PDF file manipulation.
- **ReportLab**: Library for generating PDF documents and graphics.

## Installation

1. **Install Python**: Ensure Python 3 is installed on your system. You can download it from the [official Python website](https://www.python.org/).

2. **Install Required Libraries**: Install the necessary libraries using `pip`:

   ```bash
   pip install PyPDF2 reportlab
   ```

## Usage

1. **Prepare the Script**: Save the provided script to a `.py` file.

2. **Specify Input and Output Paths**: Modify the `input_pdf` and `output_pdf` variables in the script to point to your input and desired output PDF file paths:

   ```python
   input_pdf = "input.pdf"       # Replace with your input PDF file path
   output_pdf = "output.pdf"     # Replace with desired output PDF file path
   ```

3. **Set Footer Height**: Adjust the `footer_height` variable to match the height of the footer in your PDF document (measured in points, where 1 inch = 72 points):

   ```python
   footer_height = 12  # Adjust based on your footer size
   ```

4. **Run the Script**: Execute the script using a terminal or command prompt:

   ```bash
   python script_name.py
   ```

5. **Output**: The script will process each page of the input PDF, overlay a white rectangle over the footer area, and save the modified pages to the output PDF file specified.

## Functions

- `create_overlay(page_width, page_height, footer_height)`: Creates a PDF overlay with a white rectangle at the bottom to cover the footer.

- `remove_footer(input_pdf_path, output_pdf_path, footer_height=50)`: Removes the footer from each page of the input PDF and saves the result to the output PDF.

## Notes

- **Footer Height**: Ensure that the `footer_height` value accurately reflects the height of the footer in your PDF to effectively cover the footer content.

- **Page Dimensions**: The script automatically detects the dimensions of each page to create an appropriately sized overlay.

- **Non-Destructive Editing**: The original PDF remains unaltered; the script creates a new PDF with the footers removed.

## License

This project is licensed under the MIT License.

## References

- [PyPDF2 Documentation](https://pypi.org/project/PyPDF2/)
- [ReportLab User Guide](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [Removing header/footer from PDF](https://www.reddit.com/r/learnpython/comments/1ao9hpj/removing_headerfooter_from_pdf/)
- [Removing PDF pages using Python and PyPDF2](https://pythoncircle.com/post/787/removing-pdf-pages-using-python-and-pypdf2/)

For further information on manipulating PDFs with Python, consider exploring the [PyPDF2 Library: How Can You Work With PDF Files in Python?](https://nanonets.com/blog/pypdf2-library-working-with-pdf-files-in-python/) article. 
