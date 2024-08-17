from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame

import reportlab
import os
import requests

X = 595.27 #standard width of A4 document format
Y = 841.89 #standard height of A4 document format


"""
Script above is about importing fonts to my program
"""
#DARK GARDEN EXAMPLE
folder = os.path.dirname(reportlab.__file__) + os.sep + 'fonts'
afmFile = os.path.join(folder, 'DarkGardenMK.afm')
pfbFile = os.path.join(folder, 'DarkGardenMK.pfb')

justFace = pdfmetrics.EmbeddedType1Face(afmFile, pfbFile)
faceName = 'DarkGardenMK' # pulled from AFM file
pdfmetrics.registerTypeFace(justFace)
justFont = pdfmetrics.Font('DarkGardenMK', faceName,'WinAnsiEncoding')
pdfmetrics.registerFont(justFont)

"""
End of font scripts
"""


def get_data(id):
    #getting the detail data of New Project from Django

    try:
        response = requests.get(f'http://127.0.0.1:8000/api/v1/newproject/{id}')
        project_data = response.json()
        return project_data
    
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def footer(c):
    #footer setup 

    c.line(0, 35, 595.27, 35) #footer size
    c.drawCentredString(60, 35/2, "| Auto - Wood |")

def header(c, project_data):
    #header setup

    project_name = project_data["name"]
    project_id = project_data["id"]
    c.setFont("Times-Bold", 18)
    c.line(0, Y - 75, 595.27, Y-75)  
    c.drawString(5, Y - 75/2 + 3, f"Wykaz elementów do zamowienia: {project_name}")
    c.drawString(5, Y - 75/2 - 18 - 6, f"ZD : {project_id}")

def header_info(c):
    #setting the information about company just under the header

    c.setFont("Times-Roman", 10)

    company_info = """Sekwoja
                      Gen. St. Dabka 22 
                      37-600 Lubaczow
                      sekwoja@sekwoja.pl
                      +48 16 632 93 30"""
    
    stylesheet = getSampleStyleSheet()
    normalStyle = stylesheet['Normal']

    header_paragraph = Paragraph(company_info,normalStyle, bulletText=None)

    frame_width = 140
    frame_height = 75
    x_position = X - frame_width
    y_position = Y - frame_height
    
    header_frame = Frame(x_position, y_position, frame_width, frame_height, showBoundary=0, leftPadding=6, bottomPadding=6,
            rightPadding=6, topPadding=15)
    header_frame.addFromList([header_paragraph], c)
    



def main():
    project_data = get_data(53)
    print(project_data)


    c = canvas.Canvas("hello.pdf")

    footer(c)
    header(c, project_data)
    header_info(c)
    c.showPage()
    c.save()

def test():

    print("x")

    c = canvas.Canvas("test_reportlab.pdf")
    c.setFont('DarkGardenMK', 32)
    c.drawString(10, 150, 'This should be in')
    c.drawString(10, 100, 'DarkGardenMK')
    c.showPage()
    c.save()

if __name__  == "__main__":
    main()

