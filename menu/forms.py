from django import forms
from .widgets import CustomClearableFileInput
from .models import Ingredients, Category, SidesAndDrinks


class IngredientsForm(forms.ModelForm):

    class Meta:
        model = Ingredients
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all().exclude(name__in=['drink', 'side'])
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'standard-border rounded-0'


class SidesAndDrinksForm(forms.ModelForm):

    class Meta:
        model = SidesAndDrinks
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.filter(name__in=["drink", "side"])
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'standard-border rounded-0'
