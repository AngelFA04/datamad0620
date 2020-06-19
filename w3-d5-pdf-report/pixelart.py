from templates.pixel import *
from fpdf import FPDF 

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 12)

for row in pixel_data:
    for pixel in row:
        pdf.set_fill_color(*colors.get(pixel))
        pdf.cell(10, 10, txt = '', border = 0, ln = 0, align = '', fill = True, link = '')
    pdf.ln()

pdf.output("output/pixelart.pdf")