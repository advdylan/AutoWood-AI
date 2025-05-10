from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cut_optimizer import views


urlpatterns = [
    path('cut-optimizer/', views.optimize_cuts_without_project, name='cut-optimizer'),
    path('new-project-elements/<int:pk>/', views.elements_get_view, name='new-project-elements')
]