from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse, HttpResponse, FileResponse


from rest_framework.decorators import api_view, parser_classes
import json 

# Create your views here.


@api_view(["POST"])
def optimize_cuts_without_project(request):

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    print(data)
    
    #file_path = f"generated_files/board_{board.id}.pdf"