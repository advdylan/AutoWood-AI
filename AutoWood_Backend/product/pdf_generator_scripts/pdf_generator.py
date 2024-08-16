from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

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
    c.drawCentredString(X/2, 35/2, "| Auto - Wood |")

def header(c, project_name):
    #header setup

    c.setFont("Times-Bold", 18)
    c.line(0, Y - 35, 595.27, Y-35)  
    c.drawCentredString(X/2, Y-(35/2)-5, f"Wycena zamówienia: {project_name}")


def main():
    project_data = get_data(53)
    project_name = project_data["name"]


    c = canvas.Canvas("hello.pdf")

    footer(c)
    header(c, project_name)
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

