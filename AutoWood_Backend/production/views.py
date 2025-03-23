from django.shortcuts import render
from product.models import *
from .models import *
from product.serializers import *
from production.serializers import *
from rest_framework import authentication, generics, mixins, permissions, status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from product.views import get_or_create_model_instance, is_image
from django.http import JsonResponse, HttpResponse, FileResponse
from django.db import transaction, IntegrityError, DatabaseError
from django.utils import timezone

import datetime
import json

# Create your views here.


class CatalogProductListCreateAPIView(
    generics.ListCreateAPIView):
    queryset = CatalogProduct.objects.all()
    serializer_class = CatalogProductSerializer

catalog_product_list_create_view = CatalogProductListCreateAPIView.as_view()
class ProductionListCreateAPIView(
    generics.ListCreateAPIView):

    queryset = Production.objects.all()
    serializer_class = ProductionSerializer

production_list_create_view = ProductionListCreateAPIView.as_view()
class ProducttionStepsListCreateAPIView(
    generics.ListCreateAPIView):
    
    queryset = ProductionStage.objects.all()
    
    serializer_class = ProductionStagesSerializer
    

production_stages_create_view = ProducttionStepsListCreateAPIView.as_view()


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def save_catalog_product(request):

    
    name = request.POST.get('name')
    category = request.POST.get('category')
    wood = request.POST.get('wood')
    collection = request.POST.get('collection')
    paint = request.POST.get('paint')
    elements_margin = request.POST.get('elements_margin')
    accesories_margin = request.POST.get('accesories_margin')
    additional_margin = request.POST.get('additional_margin')
    summary_with_margin = request.POST.get('summary_with_margin')
    summary_without_margin = request.POST.get('summary_without_margin')

    elements_post = request.POST.get('elements')
    try:
        elements_data = json.loads(elements_post)
        print(elements_data)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format for elements'}, status=400)
    
    worktime_post = request.POST.get('worktime')
    try:
        worktime_data = json.loads(worktime_post)
        print(worktime_data)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format for worktime'}, status=400)
    
    accesories_post = request.POST.get('accesories')
    try:
        accesories_data = json.loads(accesories_post)
        print(accesories_data)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format for accesories'}, status=400)


    percent_elements_margin = request.POST.get('percent_elements_margin')
    percent_accesories_margin = request.POST.get('percent_accesories_margin')
    percent_additional_margin = request.POST.get('percent_additional_margin')
    elements_cost = request.POST.get('elements_cost')
    accesories_cost = request.POST.get('accesories_cost')
    worktime_cost =  request.POST.get('worktime_cost')


    """ customer_post = request.POST.get('customer')

    try:
        customer_data = json.loads(customer_post)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format for customer data'}, status=400)
     """

    uploaded_files = []
    for key in request.FILES:
        uploaded_files.append(request.FILES[key])

    now = timezone.now()
    #print(name,category,wood,collection,paint,elements_margin,accesories_margin,additional_margin,summary_with_margin,summary_without_margin)

 
    try:
        with transaction.atomic():
            # Get or create related models
            wood = get_or_create_model_instance(Wood, wood)
            collection = get_or_create_model_instance(Collection, collection)    
            paint = get_or_create_model_instance(Paints, paint)
            category = get_or_create_model_instance(Category, category)

            #error handling for empty value first


            # Create the NewProject instance
            catalog_product = CatalogProduct.objects.create(
                name=name,    
                category=category,
                paints=paint,
                collection=collection,
                wood=wood,
                elements_margin=elements_margin,
                accesories_margin=accesories_margin,
                additional_margin=additional_margin,
                summary_with_margin=summary_with_margin,
                summary_without_margin=summary_without_margin,
                percent_elements_margin=percent_elements_margin,
                percent_accesories_margin=percent_accesories_margin,
                percent_additional_margin=percent_additional_margin,
                elements_cost = elements_cost,
                accesories_cost = accesories_cost,
                worktime_cost = worktime_cost,

                
            )
            #Handle files and images
            for file in uploaded_files:
                if(is_image(file)):
                    #print(f"Image detected: {file}")
                    
                    

                    image = Image.objects.create(
                        name = file.name,
                        image = file,
                        catalog_product = catalog_product,
                        date = now,
                        file_type = file.name.split('.')[1],
                        size = round((file.size)/1000000, 2)
                        
                    )
                else:
                    
                    
                    
                    #print(f"Document detected: {file}")
                    document= Document.objects.create(
                        name = file.name,
                        document = file,
                        catalog_product = catalog_product,
                        date = now,
                        file_type = file.name.split('.')[1],
                        size = round((file.size)/1000000, 2)
                    )

            
            # Handle elements
            #elements_data = elements_data
            for element_data in elements_data:
                wood_type = get_or_create_model_instance(Wood, element_data["element"]["wood_type"]["name"])

                element = Element.objects.create(
                    name=element_data["element"]["name"],
                    dimX=element_data["element"]["dimX"],
                    dimY=element_data["element"]["dimY"],
                    dimZ=element_data["element"]["dimZ"],
                    wood_type=wood_type
                )
                element.set_price()
                element.save()

                CatalogElement.objects.create(
                    catalog_product=catalog_product,
                    element=element,
                    quantity=element_data["quantity"]
                )

                catalog_product.new_elements.add(element)
            
            # Handle worktime
            
            for worktime in worktime_data:
                worktimetype = get_or_create_model_instance(Worktimetype, worktime["text"])
                duration = worktime.get("hours", 0) or 0
                workers = worktime["workers"]

                CatalogWorktime.objects.create(
                    catalog_product=catalog_product,
                    worktime=worktimetype,
                    duration=duration,
                    workers=workers
                )
            
            # Handle accessories
            
            for accessory in accesories_data:
                accessory_type = get_or_create_model_instance(AccessoryType, accessory["type"]["name"])
                quantity = accessory["quantity"]

                CatalogAccessoryDetail.objects.create(
                    catalog_product = catalog_product,
                    type = accessory_type,
                    quantity = quantity
                )

                catalog_product.accessories.add(accessory_type)
            

            

            

            # Save the final project instance
            catalog_product.save()

        return JsonResponse({'message': 'Data saved', 'project_id': catalog_product.id}, status=201)

    except IntegrityError as e:
        # Log the error
        print(e)
        return JsonResponse({'error': str(e)}, status=500)



@api_view(["PATCH"])
def update_order(request):

    data = request.data.get("data", [])
    order_id = request.data.get("id")

    if not data:
        return JsonResponse({"error": "No data provided"}, status=400)

    first_item = data[0]

    if "stage" in first_item:
        # This means the request is updating stages
        print(f"Stage condition: ${first_item}")
    elif "notes" in first_item:  # Assuming notes have a "note" key
        print(f"Note condition: {first_item}")

 


    try:
        if order_id is not None:
            order = Production.objects.get(id=order_id)
         


    except Production.DoesNotExist:
        return JsonResponse({"Error": "Production Object does not exist"})

    return JsonResponse({"error:": "No order in the production list with this ID"}) 



    """ try: 
        order = Production.objects.get(id=order_id)
        print(order)
    except Production.DoesNotExist:
        return JsonResponse({"error:" "No order in the production list with this ID"}, status=status.HTTP_404_NOT_FOUND) """
    
    

