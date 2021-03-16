from menu.models import Ingredients


class Sandwich:
    def __init__(self):

        def set_bread(self, item):
            item = Ingredients.objects.get(pk=item_id)
            if item.category.name == 'bread':
                self.bread = item


        def set_filling(self, item):
            item = Ingredients.objects.get(pk=item_id)
            if item.category.name == 'filling':
                self.filling = item


        def set_cheese(self, item):
            item = Ingredients.objects.get(pk=item_id)
            if item.category.name == 'cheese':
                self.cheese = item

        def set_spread(self, spread):
            item = Ingredients.objects.get(pk=item_id)
            if item.category.name == 'spread':
                self.spread = item