from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlparse, parse_qs
from django.contrib.auth.decorators import login_required

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def home(request):
    context = {
        "welcome_text": "Welcome to the Home Page!"
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.done = False
            instance.owner = request.user
            instance.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
            return redirect('todolist')
    else:
        # tasks = TaskList.objects.all()
        tasks = TaskList.objects.filter(owner=request.user)
        no_per_pages = 5
        paginator = Paginator(tasks, no_per_pages)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)

        context = {
            'tasks': tasks,
            "welcome_text": "Welcome to your Todo List!",
        }
        return render(request, 'todolist.html', context)


@login_required
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


def completed(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = True
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)


def pending(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = False
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)
    # return redirect('todolist')


@login_required
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


@login_required
def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)
