from django.shortcuts import render
from product.models import *
from .models import *
from product.serializers import *
from rest_framework import authentication, generics, mixins, permissions, status

# Create your views here.

class ProducttionStepsListCreateAPIView(
    generics.ListCreateAPIView):
    
    queryset = ProductionStage.objects.all()
    serializer_class = ProductionStagesSerializer
    

production_stages_create_view = ProducttionStepsListCreateAPIView.as_view()
