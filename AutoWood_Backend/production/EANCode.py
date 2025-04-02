import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from django.conf import settings

from pydantic import BaseModel, Field
from typing import Dict
import barcode
from barcode.writer import ImageWriter
import random

class DeliveryInfo(BaseModel):
    id: int
    name: str
    phone_number: int
    street: str
    code: str
    city: str
    email: str

class EANCode(BaseModel):

    id: int
    name: str
    collection: str
  
    
    def get_id_prefix(self) -> str:

        id_str = str(self.id)  # Convert int to string
        if len(id_str) == 1:
            return f"00{id_str}"
        elif len(id_str) == 2:
            return f"0{id_str}"
        elif len(id_str) == 3:
            return id_str
        

    def generate_base_code(self) -> str:

        id_prefix = self.get_id_prefix()
        ean_code = f"{id_prefix}"

        for _ in range(9):
            random_number = str(random.randint(0,9))
            ean_code += random_number

        return ean_code


    def __str__(self) -> str:
        return f"Name: {self.name}\nPrefix: {self.collection}"
        pass 



def generate_barcode(production_data):

    id = production_data.order.id
    order_name = production_data.order.name
    collection = production_data.order.collection.partners


    #print(f"Ordername: {order_name}\nCategory: {category}\nid: {id}\n\ncollection:: {collection}")

    ean_code = EANCode(
        id = id,
        name = order_name,
        collection = collection
    )


    ean = ean_code.generate_base_code()
    print(ean)

    ean13 = barcode.get_barcode_class("ean13")
    ean_instance = ean13(ean[:12])
    file_name = f"ean_{ean_code.id}{ean_code.name}"
    save_dir = os.path.join(settings.BASE_DIR, f'product/pdf_generator_scripts/reports/{id}')

    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, file_name)
    print(f"Save path : {save_path}")

    ean_instance.save(save_path)
    return file_name,save_path 













