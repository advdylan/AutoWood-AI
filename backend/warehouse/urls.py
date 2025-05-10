from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from warehouse import views


urlpatterns = [
     path('boards/', views.board_list_view, name='product-list'),
  
]