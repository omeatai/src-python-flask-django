from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
