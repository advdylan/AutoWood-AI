from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import json
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
    

new_project_detail_view= NewProjectDetailAPIView.as_view()
   

@api_view(['POST'])
def save_data(request):
    if request.method == "POST": 
        data = json.loads(request.body)
        print(data)

        wood = get_or_create_model_instance(Wood, data["wood"])
        collection = get_or_create_model_instance(Collection, data["collection"])    
        paint = get_or_create_model_instance(Paints, data["paint"])
        category = get_or_create_model_instance(Category, data["category"])


        elements_margin = data["elements_margin"]
        accesories_margin = data["accesories_margin"]
        additional_margin = data["additional_margin"]
        summary_with_margin = data["summary_with_margin"]
        summary_without_margin = data["summary_without_margin"]
   
        new_project = NewProject.objects.create(
            name = data["name"],    
            category = category,
            paints = paint,
            collection = collection,
            wood = wood,
            elements_margin=data["elements_margin"],
            accesories_margin=data["accesories_margin"],
            additional_margin=data["additional_margin"],
            summary_with_margin=data["summary_with_margin"],
            summary_without_margin=data["summary_without_margin"]
        )
        print(new_project)
        

        elements_data = data["elements"]
        for element_data in elements_data:
            wood_type = get_or_create_model_instance(Wood, element_data["wood_type"])
            element = Element(
                name=element_data["name"],
                dimX=element_data["dimX"],
                dimY=element_data["dimY"],
                dimZ=element_data["dimZ"],
                wood_type = wood_type,
                quantity = element_data["quantity"]
            )
            print(element)
            element.set_price()
            element.save()
            new_project.elements.add(element)

        worktime_data = data["worktime"]
        for worktime in worktime_data:
            worktimetype = get_or_create_model_instance(Worktimetype, worktime["text"])
            print(type(worktimetype))

            duration = worktime["hours"]
            
            if duration == '':
                duration = 0

            worktime = ProjectWorktime.objects.create(       
                project = new_project,
                worktime = worktimetype,
                duration = duration,          
                
            )
            worktime.save()

        new_project.save()
            

        accesories_data = data["accesories"]

        for accesory in accesories_data:
            accesorytype = get_or_create_model_instance(AccessoryType, accesory["name"])
            quantity = accesory["quantity"]

            acc = AccessoryDetail.objects.create(
                project = new_project,
                type = accesorytype,
                quantity = quantity
            )
            acc.save()

        new_project.save()

        return JsonResponse({'message': 'Data saved'}, status=201)
        


def get_or_create_model_instance(model, name):
    instance, created = model.objects.get_or_create(name=name)
    return instance