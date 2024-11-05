import sys
import os
# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from product.pdf_generator_scripts.pdf_generator import get_data, header, header_info, footer, X, Y
from product.pdf_generator_scripts.elements_production import generate_elements_productionpdf
from product.pdf_generator_scripts.pricing_report import generate_report
from rest_framework import authentication, generics, mixins, permissions, status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.conf import settings

from django.db import transaction, IntegrityError, DatabaseError
from django.utils import timezone
from django.http import JsonResponse, HttpResponse, FileResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import decorator_from_middleware
from io import BytesIO

import json
import mimetypes
import datetime
from .models import *
from .serializers import *


class ProductListCreateAPIView(
    generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    

product_list_destroy_update_view = ProductRetrieveUpdateDestroyAPIView.as_view()


class WoodRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Wood.objects.all()
    serializer_class = WoodSerializer
    lookup_field = 'pk'


wood_retrieve_update_destroy_view = WoodRetrieveUpdateDestroyAPIView.as_view()


class ProjectListView(APIView):
    def get(self,request):
        category_serializer = CategorySerializer(Category.objects.all(), many=True)
        worktimetype_serializer = WorktimeTypeSerializer(Worktimetype.objects.all(), many=True)
        worktime_serializer = WorktimeSerializer(Worktimetype.objects.all(), many=True)
        accesorytype_serializer = AccessoryTypeSerializer(AccessoryType.objects.all().order_by('type'), many=True)
        #accesory_serializer = AccessorySerializer(Accessory.objects.all(), many=True)
        wood_serializer = WoodSerializer(Wood.objects.all(), many=True)
        collection_serializer = CollectionSerializer(Collection.objects.all(), many=True)
        paints_serializer = PaintsSerializer(Paints.objects.all(), many=True)

        return Response({
            'category': category_serializer.data,
            'worktimetype': worktimetype_serializer.data,
            #'workitme': worktime_serializer.data,
            'accesorytype': accesorytype_serializer.data,
            #'accesory': accesory_serializer.data,
            'wood': wood_serializer.data,
            'collection': collection_serializer.data,
            'paints': paints_serializer.data
        })
    
project_list_view = ProjectListView.as_view()

class NewProjectListCreateAPIView(
    generics.ListCreateAPIView
    ):
    queryset = NewProject.objects.all()
    serializer_class = NewProjectSerializer


new_project_list_create = NewProjectListCreateAPIView.as_view()




class NewProjectDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
    ):

    queryset = NewProject.objects.all()
    lookup_field = 'pk'
    serializer_class = NewProjectSerializer

    def update(self, request, *args, **kwargs):
        data = json.loads(request.body)
        wood = get_or_create_model_instance(Wood, data["wood"])
        collection = get_or_create_model_instance(Collection, data["collection"])    
        paint = get_or_create_model_instance(Paints, data["paints"])
        category_name = get_or_create_model_instance(Category, data["category"])

        elements_margin = data["elements_margin"]
        accesories_margin = data["accesories_margin"]
        additional_margin = data["additional_margin"]
        summary_with_margin = data["summary_with_margin"]
        summary_without_margin=data["summary_without_margin"]
        percent_elements_margin = data["percent_elements_margin"]
        percent_accesories_margin = data["percent_accesories_margin"]
        percent_additional_margin = data["percent_additional_margin"]

        new_project = get_object_or_404(NewProject, pk=data["id"])

        new_project.name = data["name"]
        new_project.category = category_name
        new_project.paints = paint
        new_project.wood = wood
        new_project.collection = collection
        new_project.percent_elements_margin = percent_elements_margin
        new_project.percent_accesories_margin = percent_accesories_margin
        new_project.percent_additional_margin = percent_additional_margin
        new_project.elements_margin = elements_margin
        new_project.accesories_margin = accesories_margin
        new_project.additional_margin = additional_margin
        new_project.summary_with_margin = summary_with_margin
        new_project.summary_without_margin = summary_without_margin
        new_project.elements_cost = data["elements_cost"]
        new_project.accesories_cost = data["accesories_cost"]
        new_project.worktime_cost = data["worktime_cost"]

        elements_data = data["elements"]

        new_project.new_elements.clear()
        
        for element_data in elements_data:
            #print(element_data["element"]["wood_type"])
            wood_type = get_or_create_model_instance(Wood, element_data["element"]["wood_type"]["name"])


            element = Element(
                name=element_data["element"]["name"],
                dimX=element_data["element"]["dimX"],
                dimY=element_data["element"]["dimY"],
                dimZ=element_data["element"]["dimZ"],
                wood_type = wood_type,              
            )
            element.set_price()
            element.save()

            #print(element_data["quantity"])
            new_project_element = NewProjectElement(
                project = new_project,
                element = element,
                quantity = element_data["quantity"]
                
            )

            print((new_project_element))

            new_project_element.save()
            new_project.new_elements.add(element)


        accesories_data = data["accessories"]
        new_project.accessories.clear()
        print(accesories_data)
        #print(data["type"]["name"])

        for accesory in accesories_data:
            accesorytype = get_or_create_model_instance(AccessoryType, accesory["type"]["name"])
            quantity = accesory["quantity"]

            acc = AccessoryDetail.objects.create(
                project = new_project,
                type = accesorytype,
                quantity = quantity
            )
            acc.save()

            print(acc)
            print(accesorytype)
            

            new_project.accessories.add(accesorytype)

        new_project.save()
        
        return JsonResponse({'message': 'Data updated'}, status=201)

    
new_project_detail_view= NewProjectDetailAPIView.as_view()
   

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def save_data(request):


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
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format for elements'}, status=400)
    
    worktime_post = request.POST.get('worktime')
    try:
        worktime_data = json.loads(worktime_post)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format for worktime'}, status=400)
    
    accesories_post = request.POST.get('accesories')
    try:
        accesories_data = json.loads(accesories_post)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format for accesories'}, status=400)


    percent_elements_margin = request.POST.get('percent_elements_margin')
    percent_accesories_margin = request.POST.get('percent_accesories_margin')
    percent_additional_margin = request.POST.get('percent_additional_margin')
    elements_cost = request.POST.get('elements_cost')
    accesories_cost = request.POST.get('accesories_cost')
    worktime_cost =  request.POST.get('worktime_cost')


    customer_post = request.POST.get('customer')

    try:
        customer_data = json.loads(customer_post)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format for customer data'}, status=400)
    

    uploaded_files = []
    for key in request.FILES:
        uploaded_files.append(request.FILES[key])

    now = timezone.now()


    try:
        with transaction.atomic():
            # Get or create related models
            wood = get_or_create_model_instance(Wood, wood)
            collection = get_or_create_model_instance(Collection, collection)    
            paint = get_or_create_model_instance(Paints, paint)
            category = get_or_create_model_instance(Category, category)

            
            customer, created = Customer.objects.get_or_create(
                name=customer_data["name"],
                phone_number=int(customer_data["phone_number"]),
                street=customer_data["street"],
                code=customer_data["code"],
                city=customer_data["city"],
                email=customer_data["email"]
            )

            # Create the NewProject instance
            new_project = NewProject.objects.create(
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
                customer = customer,
                
            )
            #Handle files and images
            for file in uploaded_files:
                if(is_image(file)):
                    #print(f"Image detected: {file}")
                    
                    

                    image = Image.objects.create(
                        name = file.name,
                        image = file,
                        project = new_project,
                        date = now,
                        file_type = file.name.split('.')[1],
                        size = round((file.size)/1000000, 2)
                        
                    )
                else:
                    
                    
                    
                    #print(f"Document detected: {file}")
                    document= Document.objects.create(
                        name = file.name,
                        document = file,
                        project = new_project,
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

                NewProjectElement.objects.create(
                    project=new_project,
                    element=element,
                    quantity=element_data["quantity"]
                )

                new_project.new_elements.add(element)
            
            # Handle worktime
            
            for worktime in worktime_data:
                worktimetype = get_or_create_model_instance(Worktimetype, worktime["text"])
                duration = worktime.get("hours", 0) or 0
                workers = worktime["workers"]

                ProjectWorktime.objects.create(
                    project=new_project,
                    worktime=worktimetype,
                    duration=duration,
                    workers=workers
                )
            
            # Handle accessories
            
            for accessory in accesories_data:
                accessory_type = get_or_create_model_instance(AccessoryType, accessory["type"]["name"])
                quantity = accessory["quantity"]

                AccessoryDetail.objects.create(
                    project = new_project,
                    type = accessory_type,
                    quantity = quantity
                )

                new_project.accessories.add(accessory_type)
            

            

            

            # Save the final project instance
            new_project.save()

        return JsonResponse({'message': 'Data saved', 'project_id': new_project.id}, status=201)

    except IntegrityError as e:
        # Log the error
        print(e)
        return JsonResponse({'error': str(e)}, status=500)
        

@api_view(['GET'])
def generate_elements_production(request, pk):

    id = pk
    buffer = BytesIO()

    output_dir = os.path.join(settings.BASE_DIR, f'AutoWood_Backend/product/pdf_generator_scripts/reports/{id}')

    print("Output Directory Path:", output_dir)

    #output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/pdf_generator_scripts/reports/{id}" #for local deploy
    raport_name = f"rozpiska_produkcja_{id}.pdf"

    try:
        generate_elements_productionpdf(output_dir, raport_name, id)

        with open(f"{output_dir}/{raport_name}", "rb") as file:
            buffer.write(file.read())

        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename=raport_name)
        response['Content-Type'] = 'application/pdf'
        response['Access-Control-Allow-Origin'] = '*'  # Allow cross-origin requests
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Accept'
        return response
    
    except FileNotFoundError as e:
        return JsonResponse({'error': 'Report file not found'}, status=status.HTTP_404_NOT_FOUND)
    except RuntimeError as e:
        return JsonResponse({'error': str(e), 'outpit_dir' : output_dir}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        print("Error occurred:", str(e))
        return JsonResponse({'error': str(e), 'outpit_dir' : output_dir}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    

@api_view(['GET'])
def generate_pricing__report(request, pk):

    id = pk
    buffer = BytesIO()

    output_dir = os.path.join(settings.BASE_DIR, f'AutoWood_Backend/product/pdf_generator_scripts/reports/{id}')
    #output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/pdf_generator_scripts/reports/{id}" #for local deploy
    raport_name = f"wycena_{id}.pdf"

    try:
        generate_report(output_dir, raport_name, id)

        with open(f"{output_dir}/{raport_name}", "rb") as file:
            buffer.write(file.read())

        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename=raport_name)
    
    except FileNotFoundError as e:
        return JsonResponse({'error': 'Report file not found'}, status=status.HTTP_404_NOT_FOUND)
    except RuntimeError as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def update_worktimetypes(request):
  
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    worktimetypes = data["worktimetype"]
    wood = data["wood"]
    paints = data["paints"]
    try:
        with transaction.atomic():
            for object in worktimetypes:
                              
                new_worktimetype, created = Worktimetype.objects.update_or_create(
                    name=object["name"],
                    defaults={'cost': object["cost"]}
                )

            for object in wood:
            
                new_wood, created = Wood.objects.update_or_create(
                    name=object["name"],
                    defaults={'price': object["price"],
                              'density': object["density"]}
                )

            for object in paints:
                new_paint, created = Paints.objects.update_or_create(
                    name = object["name"],
                    defaults={'cost' : object["cost"],
                              'volume' :object["volume"]}
                )
              
            return JsonResponse({'message': 'DataSaved'}, status=200)
        
    except DatabaseError as e:
        return JsonResponse({'error': str(e)}, status=500)
        
@api_view(['POST'])
def update_accesorytype(request):

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    try:
        with transaction.atomic():
            for object in data:
                new_acc, created = AccessoryType.objects.update_or_create(
                    name = object["name"],
                    defaults={'description': object['description'],
                              'weight': object["weight"],
                              'price' : object["price"],
                              'type': object["type"]}

                )
            return JsonResponse({'message': 'Accesories succesfully updated'}, status=200)
    except DatabaseError as e:
        return JsonResponse({'error': str(e)}, status=500)
  
    return JsonResponse({'message': 'Accesories succesfully updated'}, status=200)


                
def get_or_create_model_instance(model, name):
    instance, created = model.objects.get_or_create(name=name)
    return instance

def is_image(file):
    mime_type, _ = mimetypes.guess_type(file.name)
    
    if mime_type and mime_type.startswith('image'):
        return True
    return False