from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})
