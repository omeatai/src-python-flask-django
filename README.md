# Python-Flask-Django - src

## +LinkedIn - Django Essential Training

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
django-admin startproject smartnotes .
```

## Start Local Server

```py
python manage.py runserver
```

```x
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 20, 2024 - 04:58:12
Django version 5.0.3, using settings 'smartnotes.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d1188761-5eb8-44f3-849e-b6b69662cd44">
<img width="1416" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c414f6de-58e0-490e-a6d6-e0cbaae242b1">

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
<summary>4. Creating your first Django template </summary>

# Creating your first Django template

[https://github.com/omeatai/src-python-flask-django/commit/6f788cf2b56c91f44b960178d8576c35bbebd11a](https://github.com/omeatai/src-python-flask-django/commit/6f788cf2b56c91f44b960178d8576c35bbebd11a)

### smartnotes.settings:

```py
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_TZ = True
```

### home.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})
```

### home/templates/home/welcome.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartNotes</title>
</head>

<body>
    <h1>Welcome to SmartNotes Home Page - {{name}}.</h1>
    <h2>Today is {{date}}</h2>
</body>

</html>
```

<img width="1413" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/360b36a5-c3e9-4767-81b6-50a6969bbe2c">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b117ad99-4daa-4910-9b8d-7581139d5bac">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7f247c75-ff40-4fa4-9f30-266cf411a8f3">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7a366f68-7d08-423b-a7c9-c400262a04af">

# #END</details>

<details>
<summary>5. Migrate Changes </summary>

# Migrate Changes

```py
python manage.py makemigrations
```

```py
python manage.py migrate
```

<img width="449" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7b035ec1-9768-47cb-82b2-99171cccee67">

# #END</details>

<details>
<summary>6. Create Super User</summary>

# Create Super User

```py
python manage.py createsuperuser
```

# Run Dev Server

```py
python manage.py runserver
```

<img width="448" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/07bc212b-b444-4f42-804e-6212abf24964">
<img width="1330" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/eb04a65d-2c5e-4040-830c-1e1618cd1767">
<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f883b789-fdf6-46d6-b729-f730c87c7ed6">
<img width="1319" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/97ccec8d-6dcf-4929-b8e0-a8a189fbf2be">

# #END</details>

<details>
<summary>7. Basic User Authentication</summary>

# Basic User Authentication

[https://github.com/omeatai/src-python-flask-django/commit/d5e5549f294eff2e8802a0cbfb499be02c648d31](https://github.com/omeatai/src-python-flask-django/commit/d5e5549f294eff2e8802a0cbfb499be02c648d31)

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    path('home', views.home),
    path('authorized', views.authorized),
]
```

### home.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


@login_required
def authorized(request):
    return render(request, 'home/authorized.html', {})
```

### home/authorized.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restricted Area</title>
</head>

<body>
    <h1>You are in a restricted area!</h1>
</body>

</html>
```

<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4e2e5a7b-8123-4e02-bc14-c92f6b71066b">
<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/60489590-edb1-4fbe-9d9a-7fac08eadf1d">
<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/739ecf40-3968-476a-8119-141a4335c8d9">
<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9f3c23f0-cc96-4e2e-9066-5eedc5ad5c95">

# #END</details>

<details>
<summary>8. Basic User Authentication 2 - Force Redirect on failed Login</summary>

# Basic User Authentication 2 - Force Redirect on failed Login

[https://github.com/omeatai/src-python-flask-django/commit/ee29ba256602e97df09bcec992f4c0efda93286b](https://github.com/omeatai/src-python-flask-django/commit/ee29ba256602e97df09bcec992f4c0efda93286b)

### home.views:

```py
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
```

<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/000601ab-8f95-4b1f-a720-34ccf24eb623">

# #END</details>

<details>
<summary>9. Create Notes Model</summary>

# Create Notes Model

[https://github.com/omeatai/src-python-flask-django/commit/09253493e7a3e2e425681639f18e15110a5d6092](https://github.com/omeatai/src-python-flask-django/commit/09253493e7a3e2e425681639f18e15110a5d6092)

## Create new app - notes

```py
django-admin startapp notes
```

### smartnotes.settings:

```py
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
    'notes',
]
```

### notes.models:

```py
from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

## Run migrations

```py
python manage.py makemigrations
python manage.py migrate
```

# #END</details>

<details>
<summary>10. Using Admin for data creation and manipulation</summary>

# Using Admin for data creation and manipulation

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
