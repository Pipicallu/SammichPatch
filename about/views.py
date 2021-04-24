from django.shortcuts import render, redirect


def about(request):
    '''A view to return the index page'''
    return render(request, 'about/about.html')