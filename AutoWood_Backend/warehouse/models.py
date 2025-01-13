from django.db import models
from product.models import Wood 

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=20, default="board", null=True)
    dimX = models.IntegerField(help_text="Dimension in milimeters")
    dimY = models.IntegerField(help_text="Dimension in milimeters")
    dimZ = models.IntegerField(help_text="Dimension in milimeters")
    wood_type = models.ForeignKey(Wood, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f"boardName:{self.name} {self.wood_type}, dimX:{self.dimX}, dimY:{self.dimY}, dimZ:{self.dimZ}"
