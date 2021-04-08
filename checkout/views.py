from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag right now!')
        return redirect(reverse('ingredients'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IJ3TnLqFdJGIhsSYa4ZVKwVR2AkgZ9yKLsY5ewq2sm0vRH2jJPq8sbksfIpnxuhCETYUWVF14JJKu19rDbADxIa00pHVrHHxL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)