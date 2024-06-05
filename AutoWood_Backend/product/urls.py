from django.urls import path

from product import views

urlpatterns = [
    path('product/', views.product_list_create_view, name='product-list'),
    path('project/', views.project_list_view, name="project-list"),
    path('newproject/', views.new_project_retrieve_update_destroy_view, name='new-project'),
    path('<int:pk>/update/', views.product_list_destroy_update_view, name="product-update" ),
    path('wood/<int:pk>/update', views.wood_retrieve_update_destroy_view, name="wood-update"),
    path('product/save', views.save_data, name="save-data")
]