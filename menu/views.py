from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Ingredients, SidesAndDrinks, DietaryRequirements


def all_ingredients(request):
    '''A view to show all the ingredients in the form'''
    ingredients = Ingredients.objects.all()
    dietary_req = DietaryRequirements.objects.values_list('name', flat=True).distinct()
    dietary_req = list(dietary_req)
    
    
    print(dietary_req)
    dietaryRequirements = None

    if request.GET:
        if 'dietary_requirements' in request.GET:
            dietaryRequirements = request.GET['dietary_requirements'].split(',')
            ingredients = ingredients.filter(dietary_requirements__name__in=dietaryRequirements)
            dietaryRequirements = DietaryRequirements.objects.filter(name__in=dietaryRequirements)

    context = {
        'ingredients': ingredients,
        'current_dietaryRequirements': dietaryRequirements,
        'dietary_list': dietary_req,
    }

    return render(request, 'menu/ingredients.html', context)
