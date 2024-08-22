from pdf_generator import get_data, header, header_info, footer, elemental_table, worktimes_table,accesories_table, X, Y
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

import os
import requests
import reportlab


def main():

    id = 46
    project_data = get_data(id)
    
    output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/pdf_generator_scripts/reports/{id}"
    raport_name = f"wycena_{id}.pdf"
    file_path = os.path.join(output_dir, raport_name)

    if os.path.exists(file_path):
        #logika gdy dokument jest już gotowy
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        c = canvas.Canvas(file_path)

        
        footer(c)
        header(c, project_data)  
        header_info(c)
        workers_table_height = worktimes_table(c, project_data)
        elemental_table_height = elemental_table(c,project_data, offset=workers_table_height)
        accesories_table(c,project_data,offset=(workers_table_height + elemental_table_height))

        


        
        c.showPage()
        c.save()
    else:

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        c = canvas.Canvas(file_path)

        
        footer(c)
        header(c, project_data)  
        header_info(c)
        table_height = worktimes_table(c, project_data)
        


        
        c.showPage()
        c.save()

main()