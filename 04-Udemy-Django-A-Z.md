
## +Udemy - Django A-Z Build and Deploy Web Project

<details>
<summary>1. Creating a New Django Project </summary>

# Creating a New Django Project

## Install venv

```py
python -m venv myproject-env
```

## Activate venv

```py
# myproject-env\Scripts\activate
source myproject-env/bin/activate
```

## Install Django

```py
python -m pip install Django
pip install django
pip install django==5.0
```

## Get dependencies

```py
pip freeze
```

```x
asgiref==3.7.2
Django==5.0.3
sqlparse==0.4.4
```

## Save Dependencies to Requirements.txt

```py
pip freeze > requirements.txt
```

## Install requirements from Requirements.txt

```py
pip install -r requirements.txt
```

## Deactivate a virtual environment

```py
deactivate
```

## Create Django Project

```py
django-admin startproject taskmate .
```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## Start Local Server

```py
python manage.py runserver
```

```x
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 03, 2024 - 19:56:32
Django version 5.0.4, using settings 'taskmate.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/22df5e9a-3927-4360-bffc-40c6cfb95033)

<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e087d565-d986-4697-b1d6-3e1a239d5689">

# #END</details>

<details>
<summary>2. Create new App - TodoList </summary>

# Create new App - TodoList

[https://github.com/omeatai/src-python-flask-django/commit/fbf231bb53a548dc15c021d4041212fa10ffc13b](https://github.com/omeatai/src-python-flask-django/commit/fbf231bb53a548dc15c021d4041212fa10ffc13b)

## Create App

```py
python manage.py startapp todolist
django-admin startapp todolist
```

### taskmate.settings:

```x
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'todolist',
]
```

<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0df79c8a-1bcd-44c9-8941-cae421178859">


# #END</details>

<details>
<summary>3. Create Urls and Views </summary>

# Create Urls and Views


### taskmate.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist.urls')),
]
```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
]
```

### todolist.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def todolist(request):
    return HttpResponse("<h1>Welcome to the Task Page</h1>")
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/00dc48de-9654-4228-9306-b1e13ebdebef)
<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/428fa1e7-2306-4ed8-8d4d-92f0aff97760">
<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e0b80bad-7cdc-4a7c-b993-0d9fd4a5ccd2">
<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ca3b2339-c5b3-41b8-a5cd-6bf04e8e7dd6">

# #END</details>

<details>
<summary>4. Create Template </summary>

# Create Template

[https://github.com/omeatai/src-python-flask-django/commits/main/](https://github.com/omeatai/src-python-flask-django/commits/main/)

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
]

```

### todolist.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def todolist(request):
    # return HttpResponse("<h1>Welcome to the Task Page</h1>")
    return render(request, 'todolist.html', {})

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```py
<h1>Welcome to the New Task Page on Template!</h1>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/d396c262-ed1e-4f1c-bf43-fa520ea9c3af)

<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/cfbc6f64-928f-4080-ba25-8ebcc3d0a6de">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4dd585bd-dfd6-4303-8744-62592671234a">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/86cd6c65-0954-43fd-a751-6a9473475cf4">

# #END</details>

<details>
<summary>5. Using Bootstrap Template </summary>

# Using Bootstrap Template

[https://github.com/omeatai/src-python-flask-django/commit/5e9fe522da16c264556fb6d4e37d64bb80d1747b](https://github.com/omeatai/src-python-flask-django/commit/5e9fe522da16c264556fb6d4e37d64bb80d1747b)

## Bootstrap Main Template

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
```

## Navbar Template

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">

    <title>Todo List - Taskmate </title>
</head>

<body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Pricing</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" aria-disabled="true">Disabled</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <main class="container">
        <h1>Welcome to the New Task Page on Template!</h1>
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous">
    </script>
</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/446ff51f-5e68-4fab-9ee5-1b2cd918856d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/34ea1c8a-0430-4406-8548-f7a842f7633c)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e975baa4-d57f-4a83-9615-bfe89045f5eb)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/4f3ff341-162f-41c5-baa4-37f70e1ee5ae)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c34349cd-1660-490d-8a99-3960b0e1360b)

<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7e064467-6a7e-46d9-9b8b-4a40e7aeea92">

# #END</details>

<details>
<summary>6. Base Templating with Jinja 2 </summary>

# Base Templating with Jinja 2

[https://github.com/omeatai/src-python-flask-django/commits/main/](https://github.com/omeatai/src-python-flask-django/commits/main/)

### taskmate.settings:

```py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [BASE_DIR / 'templates'],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### taskmate.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist.urls')),
]

```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]

```

### todolist.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def todolist(request):
    context = {
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

```

### src-python/udemy/django-A-Z/templates/todolist/base.html:

```html
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">

    <title>Todo List Manager - {% block title %}{% endblock title %} </title>
</head>

<body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Task Mate</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="{% url 'todolist' %}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
                        {% comment %} <a class="nav-link" href="/task">Todo List</a> {% endcomment %}
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'about' %}">About Us</a>
                        {% comment %} <a class="nav-link" href="/task/about">About Us</a> {% endcomment %}
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
                        {% comment %} <a class="nav-link" href="/task/contact">Contact Us</a> {% endcomment %}
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <main class="container">
        <h1>Taskmate</h1>
        {% block content %}
        {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous">
    </script>
</body>

</html>
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/about.html:

```html
{% extends "todolist/base.html" %}

{% block title %}
About Us
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/contact.html:

```html
{% extends "todolist/base.html" %}

{% block title %}
Contact Us
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/cf0018f9-f76d-4331-9a12-6e593e93388b)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/4c1a659a-e02e-4100-bd7d-e8642b1827b5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c3df0c22-7edc-4e21-912d-f3d99900780b)
<img width="1429" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/404412e4-8604-4713-8743-16acc5cb9ac5">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a17c5e5f-fcbc-4441-8ed1-f9f7072c28f4">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/95719a7d-890b-4a25-bbc3-2c6c89c8b1dc">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/15c80222-f800-406c-828f-c4c8bc2ce164">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/958b11f8-8a51-4bf7-9248-72d3a4c4a14a">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e5d94c38-773f-4bef-aeb3-68d5e0eed1cd">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/82861d69-ab2b-4767-9e65-fe2017da7056">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c2707449-f9fe-44c6-bd18-412d76ada279">

# #END</details>

<details>
<summary>7. Setup Static Folder </summary>

# Setup Static Folder

[https://github.com/omeatai/src-python-flask-django/commit/b727b0e70a83ddb22c3cc2845e28d8128f0a19b9](https://github.com/omeatai/src-python-flask-django/commit/b727b0e70a83ddb22c3cc2845e28d8128f0a19b9)

### taskmate.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### src-python/udemy/django-A-Z/templates/todolist/base.html:

```html
{% load static %}

<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">

    <title>Todo List Manager - {% block title %}{% endblock title %} </title>
</head>

<body>
    <nav class="navbar navbar-expand-lg bg-body-dark navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'todolist' %}"><img src="{% static 'todolist/images/logo-1.png' %}"
                    alt="Taskmate Logo"></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="{% url 'todolist' %}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
                        {% comment %} <a class="nav-link" href="/task">Todo List</a> {% endcomment %}
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'about' %}">About Us</a>
                        {% comment %} <a class="nav-link" href="/task/about">About Us</a> {% endcomment %}
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
                        {% comment %} <a class="nav-link" href="/task/contact">Contact Us</a> {% endcomment %}
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <main class="container">
        <h1>Taskmate</h1>
        {% block content %}
        {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous">
    </script>
</body>

</html>
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```py
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a2277918-c10d-4288-9da7-5b432584721b)

<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9df594d4-54de-4364-82f0-3a284055392f">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3bc02c76-03e0-4a8f-9378-a031239ecf0b">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b220e88c-809f-41f0-8ae3-09afe5965650">

# #END</details>

<details>
<summary>8. Create Super User for Admin Panel </summary>

# Create Super User for Admin Panel

## Create Super User

```py
python manage.py createsuperuser
```

## Run Local Server

```py
python manage.py runserver
```

<img width="510" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/77949caa-8709-4791-a7e5-2afdec7fba00">
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b0543452-5fe3-4bcb-82fa-383316494102)
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6f3861bb-a0fb-4586-81ce-ef572f8a5222">

# #END</details>

<details>
<summary>9. Setup Django Model and Migration </summary>

# Setup Django Model and Migration

[https://github.com/omeatai/src-python-flask-django/commit/d3985ea132dfa34bb55905b46db68e27b9d763b3](https://github.com/omeatai/src-python-flask-django/commit/d3985ea132dfa34bb55905b46db68e27b9d763b3)

### todolist.models:

```py
from django.db import models

# Create your models here.


class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

### todolist.admin:

```py
from django.contrib import admin
from .models import TaskList

# Register your models here.
admin.site.register(TaskList)

```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## Run Local Server

```py
python manage.py runserver
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f69b55f9-7c06-45d9-b90f-95705d619746)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/efc83b7a-c85c-46fd-9381-3d673105a4ee)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/cc5ba05b-068b-4920-8670-f7abc38f04ad)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1ec8e6a8-e448-4bc6-a8f9-2d296a99fbd5)

<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6c89310a-d2c6-4e4b-9ebb-a82cf387cab9">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/addfbe9c-e4ae-4dd3-af38-f60ee9b8d031">

# #END</details>

<details>
<summary>10. Fetch Data from Database </summary>

# Fetch Data from Database

[https://github.com/omeatai/src-python-flask-django/commit/36b1e3ea6eecc65fecc913682d0829684a876ebd](https://github.com/omeatai/src-python-flask-django/commit/36b1e3ea6eecc65fecc913682d0829684a876ebd)

[https://getbootstrap.com/docs/5.3/content/tables/](https://getbootstrap.com/docs/5.3/content/tables/)

## Bootstrap Table Format:

```html
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
```

### todolist.views:

```py
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

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>

{% comment %} <table class="table table-dark table-striped"> {% endcomment %}
    <table class="table table-light table-striped table-hover table-bordered">
        <thead>
            <tr class="table-dark">
                <th scope="col">Task</th>
                <th scope="col">Done</th>
                <th scope="col">Edit</th>
                <th scope="col">Delete</th>
            </tr>
        </thead>
        <tbody>
            {% for todo in tasks %}
            {% if todo.done %}
            <tr class="table-success">
                <th scope="row">{{ todo.task }}</th>
                <td>YES</td>
                <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
                <td><a href="" type="button" class="btn btn-danger btn-sm">Delete</a></td>
            </tr>
            {% else %}
            <tr>
                <th scope="row">{{ todo.task }}</th>
                <td>NO</td>
                <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
                <td><a href="" type="button" class="btn btn-danger btn-sm">Delete</a></td>
            </tr>
            {% endif %}
            {% endfor %}
        </tbody>
    </table>

    {% for todo in tasks %}
    <div class="todo">
        <h3>{{ todo.task }} - {{ todo.done }}</h3>
    </div>


    {% endfor %}

    {% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/02124501-e51e-44a8-9433-e90626c05762)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1eec6917-7f8f-4ef9-8c26-b6f16b130988)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a04a4aed-1075-4144-b7e2-db3cb0cc7cbb)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/db8b9ea7-1016-44a0-8550-646e391acd3c)

<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9c32960b-e69b-4f62-8313-e599cb6771b5">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5049d062-2360-44a7-a134-414b3d9c14b5">

# #END</details>

<details>
<summary>11. Using Forms to add data </summary>

# Using Forms to add data

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```


# #END</details>

<details>
<summary>+Udemy - Django A-Z Build and Deploy Web Project </summary>

# #END</details>


