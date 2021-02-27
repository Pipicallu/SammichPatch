from django.contrib import admin
from .models import Ingredients, Category, DietaryRequirements, SidesAndDrinks

admin.site.register(Ingredients)
admin.site.register(Category)
admin.site.register(DietaryRequirements)
admin.site.register(SidesAndDrinks)
