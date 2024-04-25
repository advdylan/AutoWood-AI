from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paints
        fields = '__all__'


class WorktimeTypeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Worktimetype
        fields = '__all__'

class WorktimeSerializer(serializers.ModelSerializer):

    name = WorktimeTypeSerializer(read_only = True)
    class Meta:
        model = Worktime
        fields = '__all__'

class AccessoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoryType
        fields = '__all__'

class AccessorySerializer(serializers.ModelSerializer):

    type = AccessoryTypeSerializer(read_only = True)
    class Meta:
        model = Accessory
        fields = '__all__'

class WoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wood
        fields = [
            'name',
            'density',
            'price'
        ]

class ElementSerializer(serializers.ModelSerializer):

    wood_type = WoodSerializer(read_only=True)
    class Meta:
        model = Element
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer): 
    category = CategorySerializer(read_only=True)
    paints = PaintsSerializer(read_only=True)
    worktimes = WorktimeSerializer(many=True, read_only=True)
    accessories = AccessorySerializer(many=True, read_only=True)
    elements = ElementSerializer(many=True, read_only=True)
    collection = CollectionSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'paints',
            'worktimes',
            'accessories',
            'elements',
            'collection'
        ]

