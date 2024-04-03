
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

```py
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

