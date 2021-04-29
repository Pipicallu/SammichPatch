from django.shortcuts import render, redirect, reverse
from menu.models import Ingredients, SidesAndDrinks
from django.http import HttpResponse
from django.contrib import messages


def shopping_bag(request):
    '''A view to show the shopping bag'''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''add an sandwich to the bag'''
    if not request.POST:
        return HttpResponse(status=405)

    item = Ingredients.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    sandwich = request.session.get('sandwich', {})
    sandwich[item_id] = quantity
    request.session['sandwich'] = sandwich
    print(request.session['sandwich'])
    bag = request.session.get('bag', {})
    request.session['bag'] = bag

    if item.category.name == 'bread':
        request.session['bread_added'] = True
    if item.category.name == 'filling':
        request.session['filling_added'] = True
    if item.category.name == 'cheese':
        request.session['cheese_added'] = True
    if item.category.name == 'spread':
        request.session['spread_added'] = True
    if item.category.name == 'salad':
        messages.info(request, 'You can add as much salad as you like!')

    save_info = request.session.get('save_info')
    request.session['save_info'] = save_info
    bread_added = request.session.get('bread_added')
    request.session['bread_added'] = bread_added
    filling_added = request.session.get('filling_added')
    request.session['filling_added'] = filling_added
    cheese_added = request.session.get('cheese_added')
    request.session['cheese_added'] = cheese_added
    spread_added = request.session.get('spread_added')
    request.session['spread_added'] = spread_added

    if bread_added and filling_added and cheese_added and spread_added:
        itemNo = len(request.session['bag'])
        if f'item_{str(itemNo)}' not in request.session['bag']:
            bag[f'item_{str(itemNo)}'] = sandwich
        else:
            bag[f'item_{str(itemNo)}_replacement'] = sandwich
        messages.success(request, 'New sandwich successfully added to bag.')
        del request.session['bread_added']
        del request.session['filling_added']
        del request.session['cheese_added']
        del request.session['spread_added']
        del request.session['sandwich']

    return redirect(redirect_url)


def add_side_to_bag(request, item_id):
    if not request.POST:
        return HttpResponse(status=405)

    item = SidesAndDrinks.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    drink_side = request.session.get('drink_side', {})
    drink_side[item_id] = quantity
    request.session['drink_side'] = drink_side
    bag = request.session.get('bag', {})
    request.session['bag'] = bag

    if len(request.session.items()) >= 1:
        itemNo = len(request.session['bag'])
        if item.category.name == 'drink':
            if f'drink_{str(itemNo)}' not in request.session['bag']:
                bag[f'drink_{str(itemNo)}'] = drink_side
            else:
                bag[f'drink_{str(itemNo)}_replacement'] = drink_side
        elif item.category.name == 'side':
            if f'side_{str(itemNo)}' not in request.session['bag']:
                bag[f'side_{str(itemNo)}'] = drink_side
            else:
                bag[f'side_{str(itemNo)}_replacement'] = drink_side
        del request.session['drink_side']
        messages.success(request, 'New item added to bag.')

    return redirect(redirect_url)


def remove_ingredient(request, item_id):
    ''' remove item from a potential sandwich'''
    if not request.POST:
        return HttpResponse(status=405)
    item = Ingredients.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    sandwich = request.session.get('sandwich', {})
    sandwich = request.session['sandwich']

    if item_id in sandwich:
        if item.category.name == 'bread':
            del request.session['sandwich'][f'{item.id}']
            messages.info(
                request, f'{item.name} has been removed from your sandwich.')
            del request.session['bread_added']
        if item.category.name == 'filling':
            del request.session['sandwich'][f'{item.id}']
            messages.info(
                request, f'{item.name} has been removed from your sandwich.')
            del request.session['filling_added']
        if item.category.name == 'cheese':
            del request.session['sandwich'][f'{item.id}']
            messages.info(
                request, f'{item.name} has been removed from your sandwich.')
            del request.session['cheese_added']
        if item.category.name == 'spread':
            del request.session['sandwich'][f'{item.id}']
            messages.info(
                request, f'{item.name} has been removed from your sandwich.')
            del request.session['spread_added']
        if item.category.name == 'salad':
            del request.session['sandwich'][f'{item.id}']
            messages.info(
                request, f'{item.name} has been removed from sandwich.')

    return redirect(redirect_url)


def remove_sandwich(request, sandwich_id):
    '''Removes sandwich from the bag'''
    try:
        bag = request.session.get('bag', {})
        request.session['bag'] = bag
        messages.warning(request, 'You have deleted a item from your bag.')
        bag.pop(sandwich_id)
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'error removing item {e}')
        return HttpResponse(status=500)
