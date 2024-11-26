import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from product.pdf_generator_scripts.pdf_generator import get_data
from AutoWood_Backend.product.cut_optimizer.old_test.or_tools_mbo import pack_pieces_on_boards
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from ortools.linear_solver import pywraplp
import numpy as np


X = 3000
Y = 2000
SAW = 3.2

id = 60

output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/cut_optimizer/optimized_cuts/{id}"
optc_name = f"optc_{id}.png"
file_path = os.path.join(output_dir, optc_name)

def generate_board(output_dir, optc_name,X,Y):

    file_path = os.path.join(output_dir, optc_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    project_data = get_data(id)
    formats = convert_elements(project_data)

    fig, ax = plt.subplots()
    ax.set_xlim(0, X)
    ax.set_ylim(0, Y)
    

    i = 0
    j = 0
    start_position_x = 0
    start_position_y = 0

    define_starting_position(formats)

    
      

    for format in formats:
        #print(f"X: {format[i]}, Y: {format[i+1]}")

        generate_rectangle(start_position_x, start_position_y,format[i], format[i+1], ax)
       
    plt.savefig(file_path, format='png')


def convert_elements(project_data):

    elements = project_data["elements"]

    formats = []

    for element in elements:
        length = element['element']['dimX']
        width = element['element']['dimY']
        #thickness = element['element']['dimZ'] wyłączyłęś chwilowo grubośći
        quantity = element['quantity']
        starting_x = 0
        starting_y = 0

        row = [length, width, starting_x, starting_y]

        for _ in range(int(quantity)):
            formats.append(row)

    return formats

   
def generate_rectangle(start_position_x, start_position_y, width, height, ax):
  
    rect = patches.Rectangle(xy=(start_position_x,start_position_y), width=width, height=height, edgecolor='#bed4d4', facecolor='#d3e2dc', antialiased=True, linewidth=None)
    ax.add_patch(rect)


def calculate_rows(formats):
    i=0
    j=0
    lengths = []
    heights = []
    rows = []
    free_x = 0
    free_y = 0
    for format in formats:
        #print(f"Format numer {j}")       
        #print(f"X: {format[i]}, Y: {format[i+1]}")
        lengths.append(format[i])
        heights.append(format[i+1])
        j+=1

    lengths.sort()
    heights.sort(reverse=True)
    return lengths,heights
 
def create_virtual_row(height, X, Y):
    board = (X, height)
    return board

def control_board_capacity(format, board):
    
    capacity_left = (board[0] - format[0], board[1])
    positive = all(num >= 0 for num in capacity_left)
    if positive:
        #print("Wchodzi idelnie mój Panie")
        return capacity_left, True
    else:
        #print("Masz za dużego Panie")
        return capacity_left,False





def define_starting_position(formats):
    
    board = (X,Y)
    lengths, rows = calculate_rows(formats)
    print(f"Rows: {rows}")
    virtual_row = create_virtual_row(rows[0],X, Y)
    print(f"Virtual row:{virtual_row}")
    
    i=0
    for format in formats:
        print(f"X: {format[i]}, Y: {format[i+1]}")
        space_left = (0,0)
        if format[i+1] <= rows[0]:
                capacity_left, free_space = control_board_capacity(format, virtual_row)

                print(f"format po petli: {format}")
                print(f"capacity_left: {capacity_left}")

                
                virtual_row = capacity_left
                print(f"Virtual row: {virtual_row}")
                
                next_available_x = (format[i] + SAW)
                print(f"Next point: {next_available_x}")
                
                
                    
                i+=1






    

    
        

  
generate_board(output_dir, optc_name, X, Y)




    