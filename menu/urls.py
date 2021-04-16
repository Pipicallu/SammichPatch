from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ingredients, name='ingredients'),
    path('add/', views.add_ingredient, name='add_ingredient'),
    path('edit/<int:ingredient_id>/', views.edit_ingredient, name='edit_ingredient'),
    path('delete/<int:ingredient_id>/', views.delete_ingredient, name='delete_ingredient'),
]
