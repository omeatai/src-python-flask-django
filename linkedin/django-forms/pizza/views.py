from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, request.FILES)
        if filled_form.is_valid():
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'form': empty_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form})
