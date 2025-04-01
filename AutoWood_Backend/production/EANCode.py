


production_data  = {
    "stages": [
        {
            "stage": {
                "id": 1,
                "stage_name": "Przód",
                "shortcut": "P"
            },
            "is_done": True
        },
        {
            "stage": {
                "id": 2,
                "stage_name": "Tył",
                "shortcut": "T"
            },
            "is_done": True
        },
        {
            "stage": {
                "id": 3,
                "stage_name": "Boki szuflad",
                "shortcut": "BS"
            },
            "is_done": True
        }
    ],
    "order": {
        "id": 138,
        "name": "Tyskie",
        "category": {
            "id": 2,
            "name": "Komody",
            "slug": "komody"
        },
        "customer": {
            "id": 11,
            "name": "",
            "phone_number": 0,
            "street": "",
            "code": "",
            "city": "",
            "email": ""
        },
        "paints": {
            "id": 1,
            "name": "Lakier naturalny wodny",
            "cost": 200,
            "volume": "200.00"
        },
        "worktimes": [
            {
                "id": 580,
                "worktime": {
                    "id": 1,
                    "name": "Lakiernia",
                    "cost": 55
                },
                "duration": 5,
                "workers": 5,
                "cost": "55.00",
                "project": 138
            },
            {
                "id": 581,
                "worktime": {
                    "id": 3,
                    "name": "Czyszczenie",
                    "cost": 33
                },
                "duration": 0,
                "workers": 0,
                "cost": "33.00",
                "project": 138
            },
            {
                "id": 582,
                "worktime": {
                    "id": 4,
                    "name": "Pakowanie",
                    "cost": 23
                },
                "duration": 0,
                "workers": 0,
                "cost": "23.00",
                "project": 138
            },
            {
                "id": 583,
                "worktime": {
                    "id": 5,
                    "name": "Produkcja",
                    "cost": 55
                },
                "duration": 0,
                "workers": 0,
                "cost": "55.00",
                "project": 138
            },
            {
                "id": 584,
                "worktime": {
                    "id": 11,
                    "name": "Kontrola",
                    "cost": 25
                },
                "duration": 0,
                "workers": 0,
                "cost": "25.00",
                "project": 138
            }
        ],
        "accessories": [
            {
                "id": 138,
                "type": {
                    "id": 2,
                    "type_choices": [
                        [
                            "Prowadnice",
                            "Prowadnice"
                        ],
                        [
                            "Złącza",
                            "Złącza"
                        ],
                        [
                            "Zawiasy",
                            "Zawiasy"
                        ]
                    ],
                    "name": "Prowadnica Hafele 30",
                    "description": "Zwykły szajs za średnie pieniądze",
                    "weight": "0.45",
                    "price": "2.00",
                    "type": "Prowadnice",
                    "is_active": True
                },
                "quantity": 3,
                "project": 138
            },
            {
                "id": 139,
                "type": {
                    "id": 6,
                    "type_choices": [
                        [
                            "Prowadnice",
                            "Prowadnice"
                        ],
                        [
                            "Złącza",
                            "Złącza"
                        ],
                        [
                            "Zawiasy",
                            "Zawiasy"
                        ]
                    ],
                    "name": "Mimośród",
                    "description": None,
                    "weight": None,
                    "price": "1.50",
                    "type": "Prowadnice",
                    "is_active": None
                },
                "quantity": 3,
                "project": 138
            }
        ],
        "elements": [
            {
                "id": 298,
                "element": {
                    "id": 347,
                    "wood_type": {
                        "name": "Buk",
                        "density": 750,
                        "price": "2700.00"
                    },
                    "name": "Przód",
                    "dimX": 2133,
                    "dimY": 500,
                    "dimZ": 25,
                    "price": "71.99"
                },
                "quantity": 5,
                "project": 138
            }
        ],
        "wood": {
            "name": "Buk",
            "density": 750,
            "price": "2700.00"
        },
        "collection": {
            "id": 1,
            "name": "Sandemo",
            "description": "Łóżka Sandemo to wyjątkowy badziew w naszej kolekcji mebli",
            "partners": "Visby"
        },
        "customer": {
            "id": 3,
            "name": "Jakub Kuźma",
            "phone_number": 502333222,
            "street": "Obrońćow Westerplatte",
            "code": "37-611",
            "city": "Cieszanów",
            "email": "dyl@gmail.com"
        },
        "elements_margin": "10.80",
        "accesories_margin": "0.21",
        "additional_margin": "174.54",
        "summary_with_margin": "1930.99",
        "summary_without_margin": "1745.44",
        "percent_elements_margin": 3,
        "percent_accesories_margin": 2,
        "percent_additional_margin": 10,
        "elements_cost": "359.94",
        "accesories_cost": "10.50",
        "worktime_cost": "1375.00",
        "image": [],
        "document": []
    },
    "status": "Done",
    "date_ordered": "2025-02-16",
    "date_of_delivery": "2025-03-14",
    "notes": "Pilne 3"
}

from pydantic import BaseModel, Field
from typing import Dict

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
    delivery: DeliveryInfo
    collection: str
    
    def get_prefix(self) -> str:
        prefix = self.collection[:3]
        return prefix.upper()

    def generate_base_code(self) -> str:
        pass

    def generate_id_prefix(self) -> str:
        id_str = str(self.id)  # Convert int to string
        if len(id_str) == 1:
            return f"00{id_str}"
        elif len(id_str) == 2:
            return f"0{id_str}"
        elif len(id_str) == 3:
            return id_str

    def __str__(self) -> str:
        return f"Name: {self.name}\nPrefix: {self.collection}"
        pass 


order_name = production_data["order"]["name"]
category = production_data["order"]["category"]["name"]
id = production_data["order"]["id"]
delivery = production_data["order"]["customer"]
collection = production_data["order"]["collection"]["partners"]

print(f"Category: {category}\nid: {id}\ndelivery: {delivery}\ncollection:: {collection}")

ean_code = EANCode(
    id = id,
    name = order_name,
    delivery = delivery,
    collection = collection
)


prefix_str = ean_code.get_prefix()
print(f"get_prefix: {prefix_str}")

prefix_int = ean_code.generate_id_prefix()
print(f"generate_id_prefix : {prefix_int}")














