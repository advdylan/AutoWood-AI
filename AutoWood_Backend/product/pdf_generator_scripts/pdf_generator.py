from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.platypus import Paragraph, Frame, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont


import reportlab
import os
import requests

X = 595.27 #standard width of A4 document format
Y = 841.89 #standard height of A4 document format

pdfmetrics.registerFont(TTFont('RobotoCondensed-Regular', 'RobotoCondensed-Regular.ttf'))


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
    c.setFont("RobotoCondensed-Regular", 18)
    c.line(0, Y - 75, 595.27, Y-75)  
    c.drawString(5, Y - 75/2 + 5, f"Wykaz elementów do zamówienia: {project_name}")
    c.drawString(5, Y - 75/2 - 18 - 6, f"ZD : {project_id}")

def header_info(c):
    #setting the information about company just under the header

    stylesheet = getSampleStyleSheet()

    custom_style = ParagraphStyle(
        'CustomStyle',
        parent=stylesheet['Normal'],
        fontName='RobotoCondensed-Regular',
        fontSize=12, 
        leading=14,
        alignment=TA_LEFT
    )

    company_info = """Sekwoja
                      Gen. St. Dąbka 22 
                      37-600 Lubaczów
                      sekwoja@sekwoja.pl
                      +48 16 632 93 30"""
    
    
   

    header_paragraph = Paragraph(company_info,custom_style, bulletText=None)

    frame_width = 140
    frame_height = 75
    x_position = X - frame_width
    y_position = Y - frame_height
    
    header_frame = Frame(x_position, y_position, frame_width, frame_height, showBoundary=0, leftPadding=6, bottomPadding=6,
            rightPadding=6, topPadding=13)
    header_frame.addFromList([header_paragraph], c)
    

def elemental_table(c, project_data, offset=0):
    #elemental table setup for displaying the New Project elements
    

    elements_data = project_data["elements"]
    stylesheet = getSampleStyleSheet()
    
    headers = ['Nazwa', "Długość", 'Szerokość', 'Grubość', 'Ilość', 'Drewno']
    
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

    table_width = 0
    for column, x in enumerate(col_widths):      
        table_width += x

   
    table = Table(table_data, colWidths=col_widths)
    table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'RobotoCondensed-Regular'),  # Header font
    ('FONTNAME', (0, 1), (-1, -1), 'RobotoCondensed-Regular'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Cell background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Table grid
    ('FONTSIZE', (0, 0), (-1, 0), 12),  # Font size for the header
    ('FONTSIZE', (0, 1), (-1, -1), 10),  # Font size for the rest of the table
    ]))
    

    #calculating the width and height to set the table. Table width and position set accordingly
    row_height = 18
    rows_number = len(table_data)
    table_height = rows_number * row_height

    if offset == 0:
        y_position = Y - 115 - table_height
    else:
        y_position = Y - 125 - offset - table_height - 30

    table.wrapOn(c, X, Y)  # Ensure the table wraps correctly within the page
    table.drawOn(c, (X - table_width) / 2, y_position)  # Adjust x and y positions as necessary

    return table_height 

def worktimes_table(c, project_data):
    #elemental table setup for displaying the New Project elements

    worktimes_data = project_data["worktimes"]
    stylesheet = getSampleStyleSheet()
   
    headers = ['Dział','Ilość pracowników', 'Czas pracy', 'Koszty pracy', 'Suma']
    
    data = []

    for item in worktimes_data:
        #Getting information for header specified above : ['Dział','Ilość pracowników', 'Czas pracy', 'Koszty pracy' 'Suma']
        
        name = item['worktime']['name']
        workers = item['workers']
        duration = item['duration']
        cost = item['worktime']['cost']
        sum = f"{(int(workers)*int(duration)) * int(cost)} zł"

        row = [name, workers, duration, cost, sum]

        data.append(row)

    table_data = [headers] + data
    col_widths = [100, 100, 80, 80, 70]

    table_width = 0
    for column, x in enumerate(col_widths):      
        table_width += x



   
    table = Table(table_data, colWidths=col_widths)
    table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'RobotoCondensed-Regular'),  # Header font
    ('FONTNAME', (0, 1), (-1, -1), 'RobotoCondensed-Regular'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Cell background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Table grid
    ('FONTSIZE', (0, 0), (-1, 0), 12),  # Font size for the header
    ('FONTSIZE', (0, 1), (-1, -1), 10),  # Font size for the rest of the table
    ]))
    

    #calculating the width and height to set the table. Table width and position set accordingly
    row_height = 18
    rows_number = len(table_data)
    table_height = rows_number * row_height
    y_position = Y - 115 - table_height

    table.wrapOn(c, X, Y)  # Ensure the table wraps correctly within the page
    table.drawOn(c, (X - table_width) / 2, y_position)  # Adjust x and y positions as necessary

    return table_height 


def accesories_table(c, project_data, offset=0):
    #elemental table setup for displaying the New Project elements

    accesories_data = project_data["accessories"]
    stylesheet = getSampleStyleSheet()
   
    headers = ['Nazwa','Ilość', 'Koszt sztuki', 'Suma']
    
    data = []

    for item in accesories_data:
        #Getting information for header specified above : ['Dział','Ilość pracowników', 'Czas pracy', 'Koszty pracy' 'Suma']
        
        name = item['type']['name']
        cost = item['type']['price']
        quantity = item['quantity']
        sum = f"{float(cost) * int(quantity):.2f} zł"

        row = [name, quantity, cost, sum]

        data.append(row)

    table_data = [headers] + data
    col_widths = [160, 100, 80, 80]

        
    table_width = 0
    for column, x in enumerate(col_widths):      
        table_width += x

   
    table = Table(table_data, colWidths=col_widths)
    table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'RobotoCondensed-Regular'),  # Header font
    ('FONTNAME', (0, 1), (-1, -1), 'RobotoCondensed-Regular'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Cell background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Table grid
    ('FONTSIZE', (0, 0), (-1, 0), 12),  # Font size for the header
    ('FONTSIZE', (0, 1), (-1, -1), 10),  # Font size for the rest of the table
    ]))
    

    #calculating the width and height to set the table. Table width and position set accordingly
    row_height = 18
    rows_number = len(table_data)
    table_height = rows_number * row_height

    if offset == 0:
        y_position = Y - 115 - table_height
    else:
        y_position = Y - 125 - offset - table_height - 30 - 30

    table.wrapOn(c, X, Y)  # Ensure the table wraps correctly within the page
    table.drawOn(c, (X - table_width) / 2, y_position)  # Adjust x and y positions as necessary

    return table_height 

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

