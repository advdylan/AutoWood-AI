import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from product.pdf_generator_scripts.pdf_generator import *
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame, Table, Spacer, Paragraph
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4

import os
import requests
import reportlab

stylesheet = getSampleStyleSheet()



def header_and_info(canvas, doc, project_data):
    # Setting up the header
    project_name = project_data["name"]
    project_id = project_data["id"]

    canvas.setFont("RobotoCondensed-Regular", 18)
    canvas.line(0, Y - 75, 595.27, Y - 75)  
    canvas.drawString(5, Y - 75/2 + 5, f"Wykaz elementów do zamówienia: {project_name}")
    canvas.drawString(5, Y - 75/2 - 18 - 6, f"ZD : {project_id}")

    # Setting up the company information below the header
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

    header_paragraph = Paragraph(company_info, custom_style, bulletText=None)

    # Create a frame for the company info
    frame_width = 140
    frame_height = 75
    x_position = X - frame_width
    y_position = Y - 75  # Adjust the position below the header

    header_frame = Frame(
        x_position, y_position, frame_width, frame_height,
        showBoundary=0, leftPadding=6, bottomPadding=6,
        rightPadding=6, topPadding=13
    )

    header_frame.addFromList([header_paragraph], canvas)


def table_header(table_name="Table"):
    custom_style = ParagraphStyle(
        'CustomStyle',
        parent=stylesheet['Normal'],
        fontName='RobotoCondensed-Regular',
        fontSize=14, 
        leading=14,
        alignment=TA_CENTER,
        spaceAfter=10,
        spaceBefore=10
    )

    table_name = table_name

    table_header = Paragraph(table_name,custom_style, bulletText=None)

    return table_header


def generate_report(output_dir, raport_name, id):

    project_data = get_data(id)   
    file_path = os.path.join(output_dir, raport_name)
  
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    doc = SimpleDocTemplate(file_path, pagesize=(X, Y))

    usable_width = X
    usable_height = Y - 75 - 35 #75 header, 35 footer
    frame = Frame(0, 35, usable_width, usable_height, id='normal')

    template = PageTemplate(
        id='test', 
        frames=frame, 
        onPage=lambda c, d: header_and_info(c, d, project_data),
       
    )
    doc.addPageTemplates([template])


    elements = []

    worktimes_table  = generate_worktimes_table(doc, project_data)
    elements_table = generate_elemental_table(doc,project_data)
    accesories_table = generate_accesories_table(doc, project_data)
    summary_table = generate_summary_table(project_data)

    """
    Setting page template below
    Tables with respected headers and data
    """
    elements.append(Spacer(1,5))
    worktimes_header = table_header("Koszty pracy")
    elements.append(worktimes_header)
    elements.append(worktimes_table)

    elements_header = table_header("Lista elementów")
    elements.append(elements_header)
    elements.append(elements_table)

    accesories_header = table_header("Akcesoria")
    elements.append(accesories_header)
    elements.append(accesories_table)

    summary_header = table_header("Podsumiwanie")
    elements.append(summary_header)
    elements.append(summary_table)


    doc.build(elements)
    


