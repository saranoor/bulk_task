from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.set_margin(0)
pdf.image('./bulk_image_format/MicrosoftTeams-image.png', h=pdf.eph, w=pdf.epw)
#pdf.image('./bulk_image_format/Employee_Cards-01.svg', h=30, w=30)
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')

pdf.output('tuto1.pdf', 'F')
