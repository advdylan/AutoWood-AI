from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from production import views


urlpatterns = [
     path('stages/', views.production_stages_create_view, name='production-stages'),
     path('save-product', views.save_catalog_product, name="save-product")
  
]