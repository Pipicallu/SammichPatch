from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('extra/add/<item_id>/', views.add_side_to_bag, name='add_side_to_bag'),
    path('remove_ingredient/<item_id>/', views.remove_ingredient, name='remove_ingredient'),
    path('remove/<sandwich_id>/', views.remove_sandwich, name='remove_sandwich'),
]
