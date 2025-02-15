from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *
from warehouse.models import *
from production.models import *
from product.serializers import NewProjectSerializer, WorktimeTypeSerializer, AccessoryTypeSerializer




class WorktimeSerializer(serializers.ModelSerializer):
    worktime = WorktimeTypeSerializer(read_only=True)  # Serialize the related Worktimetype model
    #worktime_id = serializers.PrimaryKeyRelatedField(queryset=Worktimetype.objects.all(), source='worktime', write_only=True)

    name = WorktimeTypeSerializer(read_only = True, many = True)
    class Meta:
        model = CatalogWorktime
        fields = '__all__'

class AccesoryTypeSerializer(serializers.ModelSerializer):
    accesory = AccessoryTypeSerializer(read_only=True)
    name = AccessoryTypeSerializer(read_only = True, many = True)

    class Meta:
        model = CatalogAccessoryDetail
        fields = '__all__'



class ProductionStagesSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = ProductionStage
        fields = '__all__'


class CatalogProductSerializer(serializers.ModelSerializer):

    worktimes = WorktimeSerializer(many=True, read_only=True, source='catalog_worktime')
    accessories = AccesoryTypeSerializer(many=True, read_only=True, source='catalog_accessories')
    

    class Meta:
        model = CatalogProduct
        fields = [
            'id',
            'name',
            'category',
            'worktimes',
            'accessories'
            'elements_margin',
            'accesories_margin',
            'additional_margin',
            'summary_with_margin',
            'summary_without_margin',
            'percent_elements_margin',
            'percent_accesories_margin',
            'percent_additional_margin',
            'elements_cost',
            'accesories_cost',
            'worktime_cost',
        ]

class GenericRelatedField(serializers.Field):

    def to_representation(self, value):
        if isinstance(value, CatalogProduct):
            return CatalogProductSerializer(value).data
        elif isinstance(value, NewProject):
            return NewProjectSerializer(value).data
        

    def to_internal_value(self, data):
        model = data.get("type")
        object_id = data.get("id")

        if not model or not object_id:
            raise serializers.ValidationError("type and id required")
        
        model_map = {
            "catalog_product": CatalogProduct,
            "new_project": NewProject
        }

        ModelClass = model_map.get(model.lower())

        if not ModelClass:
            raise serializers.ValidationError(f"Invalid type {model} Type 'catalog_product' or 'new_project'")


        try:
            return ModelClass.objects.get(id=object_id)
        except ModelClass.DoesNotExist:
            raise serializers.ValidationError(f"No {model} found with id {object_id}")

class ProductionSerializer(serializers.ModelSerializer):

    stages = ProductionStagesSerializer(many=True, read_only=True, source='production_stages')    
    order = GenericRelatedField

    class Meta:
        model = Production
        fields = [
            "stages",
         
        ]



class GenericRelatedField(serializers.Field):

    def to_representation(self, value):
        if isinstance(value, CatalogProduct):
            return CatalogProductSerializer(value).data
        elif isinstance(value, NewProject):
            return NewProjectSerializer(value).data
        

    def to_internal_value(self, data):
        model = data.get("type")
        object_id = data.get("id")

        if not model or not object_id:
            raise serializers.ValidationError("type and id required")
        
        model_map = {
            "catalog_product": CatalogProduct,
            "new_project": NewProject
        }

        ModelClass = model_map.get(model.lower())

        if not ModelClass:
            raise serializers.ValidationError(f"Invalid type {model} Type 'catalog_product' or 'new_project'")


        try:
            return ModelClass.objects.get(id=object_id)
        except ModelClass.DoesNotExist:
            raise serializers.ValidationError(f"No {model} found with id {object_id}")