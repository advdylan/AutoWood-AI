import sys
import os
# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Now you can import as expected
from product.pdf_generator_scripts.pdf_generator import get_data, header, header_info, footer, X, Y
from product.pdf_generator_scripts.elements_production import generate_elements_productionpdf
from product.pdf_generator_scripts.pricing_report import generate_report
from io import BytesIO

id = 58
buffer = BytesIO()

output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/pdf_generator_scripts/reports/{id}"
raport_name = f"wycena_{id}.pdf"

generate_report(output_dir, raport_name, id)