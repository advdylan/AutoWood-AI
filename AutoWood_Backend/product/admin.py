from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "paints", 
        "collection"
        )

admin.site.register(Product, ProductAdmin)

class WoodAdmin(admin.ModelAdmin):
    
    list_display = ("name", "density", "price")

admin.site.register(Wood,WoodAdmin)

class PaintAdmin(admin.ModelAdmin):
    list_display = ("name", "cost", "volume")

admin.site.register(Paints, PaintAdmin)

class WorktimetypeAdmin(admin.ModelAdmin):
    list_display = ("name", "cost")

admin.site.register(Worktimetype, WorktimetypeAdmin)

class WorktimeAdmin(admin.ModelAdmin):
    list_display = ("display_name", "duration", "workers")

    def display_name(self, obj):
        return ", ".join([worktimetype.name for worktimetype in obj.name.all()])
    
    display_name.short_description = "display_name"

admin.site.register(Worktime, WorktimeAdmin)

class AccessoryTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "weight", "price")

admin.site.register(AccessoryType, AccessoryTypeAdmin)

class AccessoryAdmin(admin.ModelAdmin):
    list_display = ['display_type', 'quantity']
    search_fields = ['type__name']  # You can search by the 'name' field of the 'type'
    list_filter = ['type__name']  # You can filter by the 'name' field of the 'type'

    def display_type(self, obj):
        return ", ".join([type.name for type in obj.type.all()])


admin.site.register(Accessory, AccessoryAdmin)


class ElementAdmin(admin.ModelAdmin):
    list_display = ("name", "dimX", "dimY", "dimZ", "wood_type", "price")

admin.site.register(Element, ElementAdmin)
    
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "partners")

admin.site.register(Collection, CollectionAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

admin.site.register(Category, CategoryAdmin)

class NewProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "category")

admin.site.register(NewProject,NewProjectAdmin)