from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    ingredient_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total + settings.STANDARD_DELIVERY_CHARGE
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
