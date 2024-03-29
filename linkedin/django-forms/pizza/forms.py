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

    size = forms.ModelChoiceField(
        # queryset=Size.objects.all(), to_field_name='title', empty_label=None, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
        queryset=Size.objects.all(), to_field_name='title', empty_label=None, widget=forms.RadioSelect(attrs={'class': 'form-control'}))

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        # widgets = {
        #     'topping1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'topping2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'size': forms.Select(attrs={'class': 'form-control'}),
        # }

        # widgets = {
        #     'topping1': forms.Textarea(attrs={'class': 'form-control'}),
        #     'topping2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'size': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        # }
