
from pydantic import BaseModel


class ProductionID(BaseModel): 
    production_id: int
    order_id: int


    def get_id_prefix(self) -> str:

        id_str = str(self.order_id)  # Convert int to string
        if len(id_str) == 1:
            return f"00{id_str}"
        elif len(id_str) == 2:
            return f"0{id_str}"
        elif len(id_str) == 3:
            return id_str