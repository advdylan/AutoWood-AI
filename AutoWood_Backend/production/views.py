from django.shortcuts import render
from product.models import *
from .models import *
from product.serializers import *
from rest_framework import authentication, generics, mixins, permissions, status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from product.views import get_or_create_model_instance
from django.http import JsonResponse, HttpResponse, FileResponse

import json

# Create your views here.

class ProducttionStepsListCreateAPIView(
    generics.ListCreateAPIView):
    
    queryset = ProductionStage.objects.all()
    serializer_class = ProductionStagesSerializer
    

production_stages_create_view = ProducttionStepsListCreateAPIView.as_view()


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def save_catalog_product(request):

    data = request.data.dict()
    print(data)
    name  = data.get("name")
    print(name)


    return JsonResponse({'message': 'Data saved', 'data': (data)}, status=201)


