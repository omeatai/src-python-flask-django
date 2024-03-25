from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class UserSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user


class SignupView(CreateView):
    form_class = UserSignupForm  # UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    # model = User

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes-list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    http_method_names = ['get', 'post', 'options']

    def dispatch(self, request, *args, **kwargs):
        # return super().dispatch(request, *args, **kwargs)
        # Redirect to a specific URL after logout
        return redirect('/login')


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'John Doe', 'date': datetime.now()}


# def home(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {}
    login_url = '/admin'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# ### in views.py ###
# from django.contrib.auth import login as auth_login
# from .forms import RegisterForm
#
# def sign_up(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#     else:
#         form = RegisterForm()
#
#     return render(request, 'sign_up.html', {'form': form})
