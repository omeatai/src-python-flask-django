from django import forms
from .models import Pizza

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


class PizzaForm(forms.Form):
    topping_1 = forms.CharField(label='Topping_1', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    topping_2 = forms.CharField(label='Topping_2', max_length=100, widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    topping_3 = forms.CharField(
        label='Topping_3', max_length=100, widget=forms.PasswordInput)
    topping_4 = forms.MultipleChoiceField(
        label='Topping_4', choices=TOPPING_CHOICES)
    topping_5 = forms.MultipleChoiceField(
        label='Topping_5', choices=TOPPING_CHOICES, widget=forms.CheckboxSelectMultiple)

    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=CHOICES)

# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['topping1', 'topping2', 'size']
#         labels = {
#             'topping1': 'Topping 1',
#             'topping2': 'Topping 2',
#             'size': 'Size',
#         }
