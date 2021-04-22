from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Ingredients, SidesAndDrinks, DietaryRequirements, Category
from .forms import IngredientsForm


def all_ingredients(request):
    '''A view to show all the ingredients in the form'''
    ingredients = Ingredients.objects.all()
    # to get list and sorted list
    dietary_req = DietaryRequirements.objects.values_list(
        'name', flat=True).distinct()
    dietary_req = list(dietary_req)
    dietaryRequirements = None
    sort = None
    direction = None
    veggie_menu = None
    is_vegetarian = False

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

        if 'is_vegetarian' in request.GET:
            is_vegetarian = request.GET['is_vegetarian'] == 'True'
            if is_vegetarian:
                ingredients = ingredients.filter(is_vegetarian=True)


        if 'dietary_requirements' in request.GET:
            dietaryRequirements = request.GET['dietary_requirements'].split(
                ',')
            ingredients = ingredients.filter(
                dietary_requirements__name__in=dietaryRequirements)
            dietaryRequirements = DietaryRequirements.objects.filter(
                name__in=dietaryRequirements)

    context = {
        'ingredients': ingredients,
        'current_dietaryRequirements': dietaryRequirements,
        'dietary_list': dietary_req,
        'veggie_menu': veggie_menu,
        'is_vegetarian': is_vegetarian,
    }

    return render(request, 'menu/ingredients.html', context)


def all_drinks_all_sides(request):
    sort = None
    direction = None
    category = None
    sides_and_drinks = SidesAndDrinks.objects.all()
    template = 'menu/sidesanddrinks.html'

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            sides_and_drinks = sides_and_drinks.filter(category__name__in=categories)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if sort == 'price' and direction == 'asc':
                    sides_and_drinks = sides_and_drinks.order_by('price')
                else:
                    sides_and_drinks = sides_and_drinks.order_by('-price')

    context = {
        'sides_and_drinks' : sides_and_drinks,
    }

    return render(request, template, context)



@login_required
def add_ingredient(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = IngredientsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added your new ingredient!')
            return redirect(reverse('add_ingredient'))
        else:
            messages.error(request, 'Failed to add your new ingredient. Please ensure the form is valid.')
    else:
        form = IngredientsForm()
    template = 'menu/add_ingredient.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_ingredient(request, ingredient_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    ingredient = get_object_or_404(Ingredients, pk=ingredient_id)
    if request.method == 'POST':
        form = IngredientsForm(request.POST, request.FILES, instance=ingredient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated ingredient!')
            return redirect(reverse('ingredients'))
        else:
            messages.error(request, 'Failed to update ingredient. Please ensure the form is valid.')
    else:
        form = IngredientsForm(instance=ingredient)
        messages.info(request, f'You are editing {ingredient.name}')

    template = 'menu/edit_ingredient.html'
    context = {
        'form': form,
        'ingredient': ingredient,
    }

    return render(request, template, context)


@login_required
def delete_ingredient(request, ingredient_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    ingredient = get_object_or_404(Ingredients, pk=ingredient_id)
    ingredient.delete()
    messages.success(request, f'Deleted ingredient: {ingredient.name}')
    return redirect(reverse('ingredients'))