from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import OrderItem, OrderSideItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update order total on orderitem update/create
    """

    instance.order.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    update order total on orderitem update/create
    """

    instance.order.update_total()


@receiver(post_save, sender=OrderSideItem)
def update_side_on_save(sender, instance, created, **kwargs):
    """
    update order total on orderSideitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderSideItem)
def update_side_on_delete(sender, instance, **kwargs):
    """
    update order total on orderSideitem update/create
    """

    instance.order.update_total()
