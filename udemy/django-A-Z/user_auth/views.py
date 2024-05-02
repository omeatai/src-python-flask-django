from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views import View
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, logout, login

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


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST["username"]
        # password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist')
        else:
            messages.error(
                request, "Sorry! Your credentials could not be validated. Please try again.")
            return redirect('login')
    else:
        return render(request, 'user_auth/login_manual.html')


def logout(request):
    if request.method == 'POST':
        messages.success(
            request, "Awesome! You have been logged out successfully!")
        return LogoutView.as_view(next_page='login')(request)
    else:
        return render(request, 'user_auth/logout.html')


# class UserLogoutView(LogoutView):
#     def get(self, request):
#         logout(request)
#         return redirect('login')
