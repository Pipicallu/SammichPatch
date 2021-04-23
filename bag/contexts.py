from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Ingredients, SidesAndDrinks


def bag_contents(request):
    bag_items = []
    total = 0
    previous_total = 0
    ingredient_count = 0
    bag = request.session.get('bag', {})

    for item, values in bag.items():
        for item_id, quantity in values.items():
            item_id_first_part = item.split("_")[0]
            if item_id_first_part == "item":
                ingredient = get_object_or_404(Ingredients, pk=item_id)
                total += quantity * ingredient.price
                ingredient_count += quantity
                bag_items.append({
                    'unit_id': item,
                    'item_id': item_id,
                    'type': 'sandwich',
                    'quantity': quantity,
                    'ingredient': ingredient,
                    'price': ingredient.price,
                })
            else:
                drink_side = get_object_or_404(SidesAndDrinks, pk=item_id)
                total += quantity * drink_side.price
                ingredient_count += quantity
                bag_items.append({
                    'unit_id': item,
                    'item_id': item_id,
                    'type': 'drink_side',
                    'quantity': quantity,
                    'drink_side': drink_side,
                    'price': drink_side.price,
                })
        bag_items.append({
          'unit_id': item,
          'unit_subtotal': total - previous_total,
        })
        previous_total = total

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
