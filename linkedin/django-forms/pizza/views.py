from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'form': empty_form, 'note': note, "multiple_form": multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form, "multiple_form": multiple_form})


def orders(request):
    number_of_pizzas = 2
    filled_multi_form = MultiplePizzaForm(request.GET)

    if filled_multi_form.is_valid():
        number_of_pizzas = filled_multi_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data)
            note = "Multiple Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"
        return render(request, 'pizza/orders.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/orders.html', {'formset': formset})
