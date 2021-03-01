from django.shortcuts import render, redirect
from .models import Ingredients, SidesAndDrinks


def all_ingredients(request):
    '''A view to show all the ingredients in the form'''
    ingredients = Ingredients.objects.all()

    context = {
        'ingredients': ingredients,
    }

    return render(request, 'menu/ingredients.html', context)
