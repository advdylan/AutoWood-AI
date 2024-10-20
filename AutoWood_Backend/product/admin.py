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


class AccessoryTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "weight", "price")

admin.site.register(AccessoryType, AccessoryTypeAdmin)

"""
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ['display_type', 'quantity']
    search_fields = ['type__name']  # You can search by the 'name' field of the 'type'
    list_filter = ['type__name']  # You can filter by the 'name' field of the 'type'

    def display_type(self, obj):
        return ", ".join([type.name for type in obj.type.all()])


admin.site.register(Accessory, AccessoryAdmin)
"""


class ElementAdmin(admin.ModelAdmin):
    list_display = ("name", "dimX", "dimY", "dimZ", "wood_type", "price",)

admin.site.register(Element, ElementAdmin)
    
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "partners")

admin.site.register(Collection, CollectionAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

admin.site.register(Category, CategoryAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "street", "code","city","email")

admin.site.register(Customer, CustomerAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ("name",'project', "image", "date")

admin.site.register(Image, ImageAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name",'project', "document", "date")

admin.site.register(Document, DocumentAdmin)

class ProjectWorktimeInline(admin.TabularInline):
    model = ProjectWorktime
    extra = 1

class AccessoryDetailInline(admin.TabularInline):
    model = AccessoryDetail
    extra = 1

class ElementsDetailInline(admin.TabularInline):
    model = NewProjectElement
    extra = 1
class NewProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectWorktimeInline, AccessoryDetailInline, ElementsDetailInline]
    list_display = ('id',
                    'name',
                    'category',
                    'collection',
                    'summary_with_margin',
                    'summary_without_margin', 
                    'percent_elements_margin',
                    'percent_accesories_margin',
                    'percent_additional_margin'
                    )
    search_fields = ('name',)

admin.site.register(NewProject,NewProjectAdmin)

class ProjectWorktimeAdmin(admin.ModelAdmin):
    list_display = ("project","worktime")

admin.site.register(ProjectWorktime,ProjectWorktimeAdmin)