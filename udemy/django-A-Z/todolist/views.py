from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        # note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
    }
    return render(request, 'todolist.html', context)


def edit_task(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST or None,
                        instance=TaskList.objects.get(pk=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your new Task has been updated successfully!")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    messages.success(request, "Task has been deleted successfully!")
    return redirect('todolist')


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
