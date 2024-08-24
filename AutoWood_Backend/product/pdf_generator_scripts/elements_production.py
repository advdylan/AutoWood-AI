import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Now you can import as expected
from product.pdf_generator_scripts.pdf_generator import get_data, header, header_info, footer, elemental_table, X, Y
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

import os
import requests
import reportlab


def generate_elements_production():

    id = 54
    project_data = get_data(id)
    
    output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/pdf_generator_scripts/reports/{id}"
    raport_name = f"rozpiska_produkcja_{id}.pdf"
    file_path = os.path.join(output_dir, raport_name)

    if os.path.exists(file_path):
        #logika gdy dokument jest już gotowy
        print(f"Dokument o ID:{id} istnieje już w bazie danych")
    else:

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        c = canvas.Canvas(file_path)

        
        footer(c)
        header(c, project_data)
        elemental_table(c, project_data)
        header_info(c)
        
        c.showPage()
        c.save()

generate_elements_production()