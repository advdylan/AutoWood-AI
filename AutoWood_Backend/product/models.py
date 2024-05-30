from django.db import models
from decimal import Decimal, InvalidOperation



class Wood(models.Model):
    name = models.CharField(max_length=20)
    density = models.FloatField(help_text="Density in kg/m3")
    price = models.DecimalField(help_text="Price in zl/m3", max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Paints(models.Model):
    name = models.CharField(max_length=30)
    cost = models.FloatField(blank=True)
    volume = models.DecimalField(help_text="litr", blank=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Worktimetype(models.Model):
    name = models.CharField(max_length=30)
    cost = models.FloatField(help_text="Cost of one hour worktime")

    def __str__(self):
        return f"{self.name}"

class Worktime(models.Model):
    name = models.ManyToManyField(Worktimetype)
    duration = models.FloatField()
    workers = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return ", ".join([worktimetype.name for worktimetype in self.name.all()])



class AccessoryType(models.Model):

    choices = [
        ("Prowadnice", "Prowadnice"),
        ("Złącza", "Złącza"),
        ("Zawiasy", "Zawiasy")]

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    weight = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    price = models.DecimalField(blank=True, max_digits=8, decimal_places=2, null=True)
    type = models.CharField(max_length = 50, choices=choices, default="Prowadnice")

    def __str__(self):
        return f"{self.name}"
    
class Accessory(models.Model):
    type = models.ForeignKey(AccessoryType, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.type)

class Element(models.Model):
    name = models.CharField(max_length=200)
    dimX = models.IntegerField(help_text="Dimension in milimeters")
    dimY = models.IntegerField(help_text="Dimension in milimeters")
    dimZ = models.IntegerField(help_text="Dimension in milimeters")
    wood_type = models.ForeignKey(Wood, on_delete=models.CASCADE)
    price = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2)

    
    
    def set_price(self):
        try:
            
            volume = Decimal(self.dimX / 1000) * Decimal(self.dimY / 1000) * Decimal(self.dimZ / 1000)
            self.price = volume * self.wood_type.price
        
        except InvalidOperation as e:
            print(f"Invalid operation: {e}")

    def __str__(self):
        return f"{self.name}"

        
class Collection(models.Model):
    firms = (
        ("Visby", "Visby"),
        ("Seart", "Seart"),
        ("Desiq", "Desiq"),
    )
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    partners = models.CharField(max_length=200, blank=True, choices=firms)

    def __str__(self):
        if(self.partners):
            return f"{self.name} | {self.partners}"
        else:
            return f"{self.name}"
    
class Category(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return f'/{self.slug}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    paints = models.ForeignKey(Paints, on_delete=models.CASCADE)
    worktimes = models.ManyToManyField(Worktime, blank=True)
    accessories = models.ManyToManyField(Accessory, blank=True)
    elements = models.ManyToManyField(Element)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    class Meta: 
        ordering = ('category', 'name')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): 
        return f'/{self.category.name}/{self.name}'
    


    
    
class Balance(models.Model):
    balance = models.DecimalField(blank=True, max_digits=7, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    worktime = models.ForeignKey(Worktime, on_delete=models.CASCADE)

#class ProductElement(models.Model):
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #element = models.ForeignKey(Element, on_delete=models.CASCADE)
    #quantity = models.IntegerField()