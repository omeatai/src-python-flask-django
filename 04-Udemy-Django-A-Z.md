
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

<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/db85e8c0-bde6-4dcf-8103-f7faf5b96511">

# #END</details>

<details>
<summary>2. Create new App - Home </summary>

# Create new App - Home

[https://github.com/omeatai/src-python-flask-django/commit/0959e138fcee4d7829ef38e9ca8ff24a5c443a23](https://github.com/omeatai/src-python-flask-django/commit/0959e138fcee4d7829ef38e9ca8ff24a5c443a23)

## Create App

```py
django-admin startapp home
```

### smartnotes.settings:

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
    'home',
]
```

# #END</details>

<details>
<summary>3. Create View </summary>

# Create View

[https://github.com/omeatai/src-python-flask-django/commit/c1680ccc9d7982ae87252859481cb3d64db13260](https://github.com/omeatai/src-python-flask-django/commit/c1680ccc9d7982ae87252859481cb3d64db13260)

### smartnotes.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
```

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    path('home', views.home),
]
```

### home.views:

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Hello World!</h1>")
```

<img width="1413" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ac80da1e-8b1a-4bc7-aa4f-528bd887843b">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/897bdc04-e787-467e-8194-5a5bcc99c229">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1292f08d-6ebc-4d3d-a0c0-460ed2869b57">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5c024f37-a954-4ae3-89a0-db735d3a7504">

# #END</details>


<details>
<summary>+Udemy - Django A-Z Build and Deploy Web Project </summary>

# #END</details>


