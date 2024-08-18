from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.platypus import Paragraph, Frame, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont


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
    c.drawString(5, Y - 75/2 + 5, f"Wykaz elementów do zamowienia: {project_name}")
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
            rightPadding=6, topPadding=13)
    header_frame.addFromList([header_paragraph], c)
    

def elemental_table(c, project_data):
    #elemental table setup for displaying the New Project elements
    

    elements_data = project_data["elements"]
    

    stylesheet = getSampleStyleSheet()
    normalStyle = stylesheet['Normal']

    

    #table_paragraph = Paragraph("table", normalStyle, bulletText=None)

    headers = ['Nazwa', "Długosc", 'Szerokosc', 'Grubosc', 'Ilosc', 'Drewno']
    
    data = []

    for item in elements_data:
        #Getting information for header specified above : ['Nazwa', "Długość", 'Szerokość', 'Grubość', 'Ilość', 'Drewno']
        
        name = item['element']['name']
        wood_type = item['element']['wood_type']['name']
        length = item['element']['dimX']
        width = item['element']['dimY']
        thickness = item['element']['dimZ']
        quantity = item['quantity']

        row = [name,length,width,thickness,quantity,wood_type]

        data.append(row)

    table_data = [headers] + data
    col_widths = [100, 80, 80, 80, 70, 70]

    #calculating the width of all of the given columns. Table width and position set accordingly

    table_width = 0
    for column, x in enumerate(col_widths):      
        table_width += x

    print(table_width)
    table = Table(table_data, colWidths=col_widths)
    table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),  # Header font
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Cell background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Table grid
    ('FONTSIZE', (0, 0), (-1, 0), 12),  # Font size for the header
    ('FONTSIZE', (0, 1), (-1, -1), 10),  # Font size for the rest of the table
    ]))
    frame_width = X-100
    frame_height = 600
    x_position = X/2
    y_position = Y - 90

    table.wrapOn(c, (X/table_width), Y-90)  # Ensure the table wraps correctly within the page
    table.drawOn(c, (X - table_width)/2, Y - 180)  # Adjust x and y positions as necessary

    

    
    

def main():

    project_data = get_data(37)
    
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

