import matplotlib.pyplot as plt
import numpy as np
import os

X = 2000
Y = 600

id = 27

output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/cut_optimizer/optimized_cuts/{27}"
optc_name = f"optc_{id}.pdf"
file_path = os.path.join(output_dir, optc_name)

def generate_board(output_dir, optc_name,X,Y):

    file_path = os.path.join(output_dir, optc_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


generate_board(output_dir, optc_name, X, Y)




    