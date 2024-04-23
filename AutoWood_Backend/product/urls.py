from django.urls import path

from product import views

urlpatterns = [
    path('', views.product_list_create_view, name='product-list'),
    path('<int:pk>/update/', views.product_list_destroy_update_view, name="product-update" ),
    path('wood/<int:pk>/update', views.wood_retrieve_update_destroy_view, name="wood-update")
]