import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from product.pdf_generator_scripts.pdf_generator import get_data
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


X = 2000
Y = 600

id = 61

output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/cut_optimizer/optimized_cuts/{id}"
optc_name = f"optc_{id}.png"
file_path = os.path.join(output_dir, optc_name)

def generate_board(output_dir, optc_name,X,Y):

    file_path = os.path.join(output_dir, optc_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    project_data = get_data(id)
    formats = convert_elements(project_data)

    i = 0
    j = 0
    start_position_x = 0
    start_position_y = 0
    
    #for format in formats:
        



    

    plt.axis([0,X,0,Y])
    plt.savefig(file_path, format='png')


def convert_elements(project_data):

    elements = project_data["elements"]

    formats = []

    for element in elements:
        length = element['element']['dimX']
        width = element['element']['dimY']
        thickness = element['element']['dimZ']
        quantity = element['quantity']

        row = [length,width,thickness,quantity]

        formats.append(row)

    return formats

   

    
def generate_rectangle(start_position_x, start_position_y, width, height):
  
    rect = patches.Rectangle(xy=(start_position_x,start_position_y), width=width, height=height)


generate_board(output_dir, optc_name, X, Y)




    