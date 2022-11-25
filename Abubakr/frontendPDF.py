from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
my_path = '/Users/student/PycharmProjects/PDFFF/my_pdf.pdf'
c = canvas.Canvas(my_path)
c.drawString(360,770, '1 Savol ✖ ✔')
c.drawString(360,750, '2 Savol ✖')
c.drawString(360,730, '3 Savol ✖')
c.drawString(360,710, '4 Savol ✖')
c.drawString(360,690, '5 Savol ✖')
c.drawString(360,670, '6 Savol ✖')
c.drawString(360,650, '7 Savol ✖')
c.drawString(360,630, '8 Savol ✖')
c.drawString(360,610, '9 Savol ✖')
c.drawString(354,590, '10 Savol ✖')
c.drawString(354,570, '11 Savol ✖')
c.drawString(354,550, '12 Savol ✖')
c.drawString(354,530, '13 Savol ✖')
c.drawString(354,510, '14 Savol ✖')
c.drawString(354,490, '15 Savol ✖')
c.drawString(354,470, '16 Savol ✖')
c.drawString(354,450, '17 Savol ✖')
c.drawString(354,430, '18 Savol ✖')
c.drawString(354,410, '19 Savol ✖')
c.drawString(354,390, '20 Savol ✖')
c.drawString(354,370, '21 Savol ✖')
c.drawString(354,350, '22 Savol ✖')
c.drawString(354,330, '23 Savol ✖')
c.drawString(354,310, '24 Savol ✖')
c.drawString(354,290, '25 Savol ✖')
c.drawString(354,270, '26 Savol ✖')
c.drawString(354,250, '27 Savol ✖')
c.drawString(354,230, '28 Savol ✖')
c.drawString(354,210, '29 Savol ✖')
c.drawString(354,190, '30 Savol ✖')
###############################################
c.drawString(490,770, '1 Savol ✖ ✔')
c.drawString(490,750, '2 Savol ✖')
c.drawString(490,730, '3 Savol ✖')
c.drawString(490,710, '4 Savol ✖')
c.drawString(490,690, '5 Savol ✖')
c.drawString(490,670, '6 Savol ✖')
c.drawString(490,650, '7 Savol ✖')
c.drawString(490,630, '8 Savol ✖')
c.drawString(490,610, '9 Savol ✖')
c.drawString(484,590, '10 Savol ✖')
c.drawString(484,570, '11 Savol ✖')
c.drawString(484,550, '12 Savol ✖')
c.drawString(484,530, '13 Savol ✖')
c.drawString(484,510, '14 Savol ✖')
c.drawString(484,490, '15 Savol ✖')
c.drawString(484,470, '16 Savol ✖')
c.drawString(484,450, '17 Savol ✖')
c.drawString(484,430, '18 Savol ✖')
c.drawString(484,410, '19 Savol ✖')
c.drawString(484,390, '20 Savol ✖')
c.drawString(484,370, '21 Savol ✖')
c.drawString(484,350, '22 Savol ✖')
c.drawString(484,330, '23 Savol ✖')
c.drawString(484,310, '24 Savol ✖')
c.drawString(484,290, '25 Savol ✖')
c.drawString(484,270, '26 Savol ✖')
c.drawString(484,250, '27 Savol ✖')
c.drawString(484,230, '28 Savol ✖')
c.drawString(484,210, '29 Savol ✖')
c.drawString(484,190, '30 Savol ✖')
# c.drawImage('/Users/student/PycharmProjects/PDFFF/Image2.jpg', -8*inch, -8)
from reportlab.lib.units import inch



c.translate(inch, inch)
# define a large font
c.setFont("Helvetica", 14)
# choose some colors
c.setStrokeColorRGB(0.1, 0.8, 0.1)
c.setFillColorRGB(0, 0, 1)  # font colour
c.drawImage('/Users/student/PycharmProjects/PDFFF/Image.jpg', -0.5 * inch, 3 * inch,width=300, height=500,)  # change path
#####Result of  student ##########################
c.drawString(-30, 200, 'Titul:')
c.drawString(-30, 180, 'Ism:')
c.drawString(-30, 160, 'Umumiy bali:')

#### Draw line and copyright information at the bottom part ###
# c.line(-1.1, -0.7 * inch, 5 * inch, -0.7 * inch)

# c.setFillColorRGB(1, 0, 0)  # font colour
# c.drawString(0, -0.9 * inch, u"\u00A9" + " plus2net.com")
c.showPage()
c.save()
