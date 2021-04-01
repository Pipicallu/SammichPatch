from django.shortcuts import render, redirect, reverse
from menu.models import Ingredients
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

    if len(request.session.items()) == 6:
        itemNo = len(request.session['bag'])
        if f'item_{str(itemNo)}' not in request.session['bag']:
            bag[f'item_{str(itemNo)}'] = sandwich
        else:
            bag[f'item_{str(itemNo)}_replacement'] = sandwich
        messages.success(request, 'Sandwich successfully added to bag.')
        del request.session['bread_added']
        del request.session['filling_added']
        del request.session['cheese_added']
        del request.session['spread_added']
        del request.session['sandwich']

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
            del request.session['bread_added']
        if item.category.name == 'filling':
            del request.session['sandwich'][f'{item.id}']
            del request.session['filling_added']
        if item.category.name == 'cheese':
            del request.session['sandwich'][f'{item.id}']
            del request.session['cheese_added']
        if item.category.name == 'spread':
            del request.session['sandwich'][f'{item.id}']
            del request.session['spread_added']
        if item.category.name == 'salad':
            del request.session['sandwich'][f'{item.id}']

    return redirect(redirect_url) 


def remove_sandwich(request, sandwich_id):
    '''Removes sandwich from the bag'''
    try:
        bag = request.session.get('bag', {})
        request.session['bag'] = bag
        bag.pop(sandwich_id)
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)