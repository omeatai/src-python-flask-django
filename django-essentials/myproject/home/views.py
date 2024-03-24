from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


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
