from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('analysis/<str:name>/', views.anaylsis, name="analysis"),
    path('search_name/', views.search_name, name="search_name"),
]
