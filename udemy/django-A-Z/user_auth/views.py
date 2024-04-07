from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CustomRegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = CustomRegistrationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})
