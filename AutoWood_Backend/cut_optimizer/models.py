from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=255, default="Default Board")
    width = models.FloatField()  # X
    height = models.FloatField()  # Y
    saw_thickness = models.FloatField(default=3.2)  # SAW
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.width}x{self.height})"

# Create your models here.
