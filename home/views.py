from django.shortcuts import render, redirect

def index(request):
    '''A view to return the index page'''
    return render(request, 'home/index.html')

