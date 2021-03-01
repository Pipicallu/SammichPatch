from django.contrib import admin
from .models import Ingredients, Category, DietaryRequirements, SidesAndDrinks


class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'is_vegetarian',
        'image',
    )

    ordering = ('category',)


class SidesAndDrinksAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'is_vegetarian',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class DietaryRequirementsAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DietaryRequirements, DietaryRequirementsAdmin)
admin.site.register(SidesAndDrinks, SidesAndDrinksAdmin)
