from fpdf import FPDF


class PDF(FPDF):

    def header(self):
        # Add image to header
        # self.image('company_logo.jpg', 0, 0, self.w, self.h)
        pass
    def footer(self):
        # Add footer with page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def add_text_box(self, x, y, w, h, text):
        # Add text box with transparent background
        self.image('transparent.png', x, y, w, h)
        self.multi_cell(w, 10, text, 0, 'C')


# Create a new PDF object
pdf = PDF()
pdf.add_page()

# Add image to page
pdf.image('background_image.jpg', 0, 0, pdf.w, pdf.h)

# Add text box on top of image
pdf.add_text_box(50, 50, 100, 50, 'Hello, World!')

# Output the PDF
pdf.output('output.pdf', 'F')
