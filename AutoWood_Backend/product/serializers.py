from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *

class ProductSerializer(serializers.ModelSerializer): 

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


class WoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wood
        fields = [
            'name',
            'density',
            'price'
        ]