from django.shortcuts import render, redirect

def shopping_bag(request):
    '''A view to return the index page'''
    return render(request, 'bag/bag.html')