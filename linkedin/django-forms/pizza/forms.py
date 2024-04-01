from django import forms
from .models import Pizza, Size

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):

    email = forms.EmailField()
    website = forms.URLField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        widgets = {
            'topping1': forms.TextInput(attrs={'class': 'form-control'}),
            'topping2': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.RadioSelect(attrs={'class': 'form-control'}),
        }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
