from django.shortcuts import render, redirect
from menu.models import Ingredients
from django.http import HttpResponse


def shopping_bag(request):
    '''A view to return the index page'''
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
        bag[f'item_{str(itemNo)}'] = sandwich
        del request.session['bread_added']
        del request.session['filling_added']
        del request.session['cheese_added']
        del request.session['spread_added']
        del request.session['sandwich']

    return redirect(redirect_url)
