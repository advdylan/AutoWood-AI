from django.shortcuts import render
from product.models import *
from .models import *
from product.serializers import *
from rest_framework import authentication, generics, mixins, permissions, status

import sys
import os
# Create your views here.

class BoardListListAPIView(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

board_list_view = BoardListListAPIView.as_view()
