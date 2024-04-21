from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "paints", 
        "display_worktimes",
        "display_accessories",
        "display_elements",
        "collection"
        )

    def display_worktimes(self, obj):
        return ", ".join([worktime.name for worktime in obj.worktimes.all()])

    def display_accessories(self, obj):
        return ", ".join([accessory.type.name for accessory in obj.accessories.all()])

    def display_elements(self, obj):
        return ", ".join([element.name for element in obj.elements.all()])

    display_worktimes.short_description = 'Worktimes'
    display_accessories.short_description = 'Accessories'
    display_elements.short_description = 'Elements'

admin.site.register(Product, ProductAdmin)

class WoodTypeAdmin(admin.ModelAdmin):
    list_display = ("name_id",)

admin.site.register(WoodType, WoodTypeAdmin)

class WoodAdmin(admin.ModelAdmin):
    
    list_display = ("name", "density", "price")

admin.site.register(Wood,WoodAdmin)