from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product import views

urlpatterns = [
    path('product/', views.product_list_create_view, name='product-list'),
    path('project/', views.project_list_view, name="project-list"),
    path('newproject/', views.new_project_list_create, name='new-project'),
    path('<int:pk>/update/', views.product_list_destroy_update_view, name="product-update" ),
    path('newproject/<int:pk>/', views.new_project_detail_view, name ='new-project-detail'),
    path('newproject/<int:pk>/', views.new_project_detail_view, name ='new-project-detail'),
    path('wood/<int:pk>/update', views.wood_retrieve_update_destroy_view, name="wood-update"),
    path('product/save', views.save_data, name="save-data"),
    path('newproject/elements-production/<int:pk>/', views.generate_elements_production, name="elements-production"),
    path('newproject/pricing-report/<int:pk>/', views.generate_pricing__report, name="pricing-report"),
    path('newproject/update-worktimetypes/', views.update_worktimetypes, name="update-worktimetypes")
]

