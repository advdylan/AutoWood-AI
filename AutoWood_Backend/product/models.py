from django.db import models



class Wood(models.Model):
    name = models.CharField(max_length=20)
    density = models.FloatField(help_text="Density in kg/m3")
    price = models.DecimalField(help_text="Price in zl/m3", max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class WoodType(models.Model): 
    name = models.ForeignKey(Wood, on_delete=models.CASCADE)

class Paints(models.Model):
    name = models.CharField(max_length=30)
    cost = models.FloatField(blank=True)
    volume = models.DecimalField(help_text="litr", blank=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Worktimetype(models.Model):
    name = models.CharField(max_length=30)
    cost = models.FloatField(help_text="Cost of one hour worktime")
    workers = models.IntegerField()

    def __str__(self):
        return self.name

class Worktime(models.Model):
    name = models.ManyToManyField(Worktimetype)
    duration = models.FloatField()

    def __str__(self):
        return self.name

class AccessoryType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    weight = models.DecimalField(blank=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
class Accessory(models.Model):
    type = models.ForeignKey(AccessoryType, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class Element(models.Model):
    name = models.CharField(max_length=200)
    dimX = models.IntegerField(help_text="Dimension in milimeters")
    dimY = models.IntegerField(help_text="Dimension in milimeters")
    dimZ = models.IntegerField(help_text="Dimension in milimeters")
    count = models.IntegerField(default=0)
    wood_type = models.ForeignKey(WoodType, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
    def set_price(self):
        volume = (self.dimX / 1000) * (self.dimY / 1000) * (self.dimZ / 1000)
        self.price = volume * self.wood_type.name.price
        self.save()
        
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
            return f"{self.name} + {self.partners}"
        else:
            return f"{self.name}"
    
class Category(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
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