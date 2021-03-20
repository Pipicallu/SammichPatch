from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Ingredients


def bag_contents(request):

    bag_items = []
    total = 0
    ingredient_count = 0
    bag = request.session.get('bag', {})

    for item, values in bag.items():
        for item_id, quantity in values.items():
            ingredient = get_object_or_404(Ingredients, pk=item_id)
            total += quantity * ingredient.price
            print(ingredient.price)
            ingredient_count += quantity
            bag_items.append({
                'item_name': item,
                'item_id': item_id,
                'quantity': quantity,
                'ingredient': ingredient,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_CHARGE
        free_delivery_gap = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_gap = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'ingredient_count': ingredient_count,
        'delivery': delivery,
        'free_delivery_gap': free_delivery_gap,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
