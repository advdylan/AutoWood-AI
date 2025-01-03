import json 

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse, HttpResponse, FileResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status



from cut_optimizer.board_based_optimizer import generate_board, convert_elements_from_list

# Create your views here.


@api_view(["POST"])
def optimize_cuts_without_project(request):

    output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/cut_optimizer/optimized_cuts/"


    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    try:
        #formats = convert_elements_from_list(data)
        #print(data)
        formats = []
        #boards = [] - for future multiple board option
        for element in data:
            if element["type"] == "board":
                x = element["board"]["dimX"]
                y = element["board"]["dimY"]

            elif element["type"] == "element":
                

                dimX = int(element["element"]["dimX"])
                dimY = int(element["element"]["dimY"])
                quantity = int(element["quantity"])
                print(f"Q in element loop : {quantity}")

                if quantity > 0:
                    for _ in range(quantity):
                        formats.append([dimX,dimY])
                        

                #formats.append([dimX,dimY])

                #print(f"X:{dimX} Y:{dimY}")

        print(f"Formats: {formats}\nBoard: {x}/{y}")
      
        #print(f"open : {output_dir}/{raport_name}")


  
        formats_omitted, free_boards, occupied_boards = generate_board(x,y, output_dir, formats)

        free_boards_dicts = [board.to_dict() for board in free_boards]
        occupied_boards_dicts = [board.to_dict() for board in occupied_boards]

        #print(f"Formats_Omitted: {formats_omitted}\n FreeBoards: {free_boards}\nOccupiedBoards: {occupied_boards}")
  
            

        

        return JsonResponse({
            'formats_ommited': formats_omitted,
            'free_boards': free_boards_dicts,
            'occupied_boards': occupied_boards_dicts
        }, status=200)
    
    except FileNotFoundError as e:
        return JsonResponse({'error': 'Report file not found'}, status=status.HTTP_404_NOT_FOUND)
    except RuntimeError as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # function to 
    
#file_path = f"generated_files/board_{board.id}.pdf"vi