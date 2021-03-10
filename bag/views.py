from django.shortcuts import render, redirect


def shopping_bag(request):
    '''A view to return the index page'''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''add an ingredient to the bag'''
    ingredient_to_add = int(request.POST.get('ingredient_to_add'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = ingredient_to_add
    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)