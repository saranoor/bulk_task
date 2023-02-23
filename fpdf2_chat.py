from fpdf import FPDF
from PIL import Image

class PDF(FPDF):

    def header(self):
        # Add image to header
        # self.image('company_logo.jpg', 0, 0, self.w, self.h)
        pass

    def add_text_box(self, x, y, w, h, text):
        # Add text box with transparent background
        alpha = 128 # Set alpha value for transparency (0 = fully transparent, 255 = fully opaque)
        img = Image.new('RGBA', (w, h), (255, 255, 255, alpha))
        self.image(img, x, y, w, h)

        # Add text to the text box
        self.set_font('Arial', '', 25) # Set the font
        text_width = self.get_string_width(text) # Get the width of the text
        x_pos = x + (w - text_width) / 2 # Center the text horizontally
        y_pos = y + (h - 5) / 2 # Center the text vertically (subtract 5 to adjust for cell padding)
        #self.text(x_pos, y_pos, text) # Output the text
        self.set_xy(x, y) # Set the position for the MultiCell
        self.multi_cell(w, 10, text, align='C') # Output the text, 10 is the line height

    def add_picture_box(self, x, y, w, h, text):
        # Add text box with transparent background
        alpha = 128 # Set alpha value for transparency (0 = fully transparent, 255 = fully opaque)
        img = Image.new('RGBA', (w, h), (255, 255, 255, alpha))
        self.image('bulk_image_format/imran_aftab', x, y, w, h)
        # Add text to the text box



# Create a new PDF object
pdf = PDF()
pdf.add_page()

# Add image to page
pdf.image('bulk_image_format/MicrosoftTeams-image.png', 0, 0, pdf.w, pdf.h)
pdf.set_font('Arial', '', 25)
name= "Muhammad Imran Aftab Khan"
designation="Co Founder and CEO"
employee_code="000"
blood="x"
phone_num="0300-00000000"
# Add text box on top of image
# pdf.add_text_box(50, 50, 50, 50, 'Hello, World!')
page_width = pdf.w  # returns the width of the page in points (72 points per inch)
page_height = pdf.h
print(page_height/2, page_width/2)
pdf.add_text_box(page_width/2-(page_width/3), 20, 100, 10,name)
#pdf.add_text_box(page_width/2-(page_width/4), 40, 60, 10,designation)
#pdf.add_picture_box(50, 50, 50, 50, 'Hello, World!')
pdf.text(70,232,employee_code)
pdf.text(55,245.5,blood)
pdf.text(55,260,phone_num)
# Output the PDF
pdf.output('output.pdf', 'F')


