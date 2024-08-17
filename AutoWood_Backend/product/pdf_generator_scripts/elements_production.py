from pdf_generator import get_data, header, header_info, footer, X, Y
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

import os
import requests
import reportlab


def main():

    id = 54
    project_data = get_data(id)
    
    output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/pdf_generator_scripts/reports/{id}"
    raport_name = f"raport_{id}.pdf"
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
        header_info(c)
        
        c.showPage()
        c.save()

main()