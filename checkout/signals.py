from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update order total on orderitem update/create
    """
    print('updated!!!!')
    instance.order.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    update order total on orderitem update/create
    """
    print('delete signal received')
    instance.order.update_total()
