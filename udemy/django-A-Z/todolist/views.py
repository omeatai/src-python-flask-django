from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList
# Create your views here.


def todolist(request):
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!"
    }
    # return HttpResponse("<h1>Welcome to the Task Page</h1>")
    return render(request, 'todolist.html', context)


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)
