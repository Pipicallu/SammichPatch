from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class DietaryRequirements(models.Model):
    class Meta:
        verbose_name_plural = 'Dietary Requirements'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SidesAndDrinks(models.Model):
    class Meta:
        verbose_name_plural = 'Sides and Drinks'

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    dietary_requirements = models.ManyToManyField('DietaryRequirements')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    class Meta:
        verbose_name_plural = 'Ingredients'

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    dietary_requirements = models.ManyToManyField('DietaryRequirements')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name