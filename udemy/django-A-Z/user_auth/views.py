from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def register(request):
    return HttpResponse("<h1>User registration Page is working!</h1>")
    # return render(request, 'register.html', {})
