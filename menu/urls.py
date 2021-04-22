from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ingredients, name='ingredients'),
    path('extra/', views.all_drinks_all_sides, name="drinks_and_sides"),
    path('add/', views.add_ingredient, name='add_ingredient'),
    path('add/extra/', views.add_side_drink, name='add_side_drink'),
    path('edit/<int:ingredient_id>/', views.edit_ingredient, name='edit_ingredient'),
    path('edit_side/<int:side_drink_id>/', views.edit_side_drink, name='edit_side_drink'),
    path('delete/<int:ingredient_id>/', views.delete_ingredient, name='delete_ingredient'),
    path('delete_side/<int:side_drink_id>/', views.delete_side_drink, name='delete_side_drink'),
]
