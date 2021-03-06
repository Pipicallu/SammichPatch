from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Ingredients, SidesAndDrinks, DietaryRequirements


def all_ingredients(request):
    '''A view to show all the ingredients in the form'''
    ingredients = Ingredients.objects.all()
    diets = DietaryRequirements.objects.all()
    print(diets)
    # to get list and sorted list
    dietary_req = DietaryRequirements.objects.values_list('name', flat=True).distinct()
    dietary_req = list(dietary_req)
    
    
    print(ingredients)
    dietaryRequirements = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if sort == 'price' and direction == 'asc':
                    ingredients = ingredients.order_by('price')
                else:
                    ingredients = ingredients.order_by('-price')



        if 'dietary_requirements' in request.GET:
            dietaryRequirements = request.GET['dietary_requirements'].split(',')
            ingredients = ingredients.filter(dietary_requirements__name__in=dietaryRequirements)
            dietaryRequirements = DietaryRequirements.objects.filter(name__in=dietaryRequirements)

    context = {
        'ingredients': ingredients,
        'current_dietaryRequirements': dietaryRequirements,
        'dietary_list': dietary_req,
        'diets': diets,
        
    }

    return render(request, 'menu/ingredients.html', context)
