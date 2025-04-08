from django.db import models
from product.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class CatalogProduct(models.Model):
    
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    paints = models.ForeignKey(Paints, on_delete=models.CASCADE)
    worktimes = models.ManyToManyField(Worktimetype,through='CatalogWorktime', blank=True)
    accessories = models.ManyToManyField(AccessoryType, through='CatalogAccessoryDetail', blank=True)
    new_elements = models.ManyToManyField(Element, through='CatalogElement',blank=True)
    wood = models.ForeignKey(Wood, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    document = models.ManyToManyField(Document, blank=True)
    image = models.ManyToManyField(Image,blank=True)
    worktime_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    elements_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    elements_margin = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    accesories_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    accesories_margin = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    additional_margin = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    summary_with_margin = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    summary_without_margin = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    percent_elements_margin = models.IntegerField(blank=True, null=True)
    percent_accesories_margin = models.IntegerField(blank=True, null=True)
    percent_additional_margin = models.IntegerField(blank=True, null=True)
    production_stages = models.ManyToManyField('ProductionStage', blank=True)




class Production(models.Model):
    production_stages = models.ManyToManyField('ProductionStage', through='OrderProductionStage', blank=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    date_ordered = models.DateField()
    
    date_of_delivery = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=150, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    
    # Generic relation to link to either NewProject or CatalogProduct
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    order = GenericForeignKey('content_type', 'object_id')

    
    def __str__(self):
        return f"Production for {self.order} (Status: {self.status})"
class ProductionStage(models.Model):    

    stage_name = models.CharField(max_length=100)
    shortcut = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.stage_name}"
class OrderProductionStage(models.Model):
    
    production = models.ForeignKey('Production', on_delete=models.CASCADE, related_name='production')
    production_stage = models.ForeignKey(ProductionStage, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.production_stage} - {'Done' if self.is_done else 'Pending'}"
    

        
    

class CatalogAccessoryDetail(models.Model):
    catalog_product = models.ForeignKey(CatalogProduct, on_delete=models.CASCADE, related_name="catalog_accessories")
    type = models.ForeignKey(AccessoryType, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class CatalogElement(models.Model):
    catalog_product = models.ForeignKey(CatalogProduct, on_delete=models.CASCADE, related_name="catalog_elements")
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.catalog_product.name} - {self.quantity}"
    
class CatalogWorktime(models.Model):
    catalog_product = models.ForeignKey(CatalogProduct, on_delete=models.CASCADE, related_name="catalog_worktime")
    worktime = models.ForeignKey(Worktimetype, on_delete=models.CASCADE)
    duration = models.FloatField(default=0)
    workers = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=10)

    def save(self, *args, **kwargs):
        self.cost = self.worktime.cost
        super().save(*args, **kwargs)