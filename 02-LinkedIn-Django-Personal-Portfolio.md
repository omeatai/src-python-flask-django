

## +LinkedIn - Building a Personal Portfolio with Django

<details>
<summary>1. Creating a New Django Project </summary>

# Creating a New Django Project

## Install venv

```py
python -m venv myproject-env
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
django-admin startproject portfolio .
```

## Start Local Server

```py
python manage.py runserver
```

# #END</details>

<details>
<summary>2. Creating Django App - Jobs </summary>

# Creating Django App - Jobs

[https://github.com/omeatai/src-python-flask-django/commit/227ea7c95e1918f8136d184a859f5690c367e5c5](https://github.com/omeatai/src-python-flask-django/commit/227ea7c95e1918f8136d184a859f5690c367e5c5)

## Create App

```py
django-admin startapp jobs
```

### portfolio.settings:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'jobs',
]
```

## Run Local Server

```py
python manage.py runserver
```

<img width="1420" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a8b0bbba-4445-4199-849d-9a8f8b046759">
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/fe28f420-5507-4ca2-bc5a-58eed67a590e)

# #END</details>

<details>
<summary>3. Setup URL, Views and Templates </summary>

# Setup URL, Views and Templates

[https://github.com/omeatai/src-python-flask-django/commit/1ce588a46d2e149c513207c96865ff7bf07c0ea7](https://github.com/omeatai/src-python-flask-django/commit/1ce588a46d2e149c513207c96865ff7bf07c0ea7)

### portfolio.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
]
```

### jobs.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
]

```

### jobs.views:

```py
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'jobs/home.html', {})

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HomePage</title>
</head>

<body>
    <h1>Hello World!</h1>
</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/970501cd-942b-4527-a718-b0cea40380d3)
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2a33a870-eff3-4c4c-b697-14801e23cf83">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/59e4d4d6-459f-480b-96aa-45ffb27ea8f8">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bb30e39c-efe7-40dc-be48-a5243416de54">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/96eaa040-50a5-4f2a-b3e4-40370b4e7aaf">

# #END</details>

<details>
<summary>4. Creating Models in Django </summary>

# Creating Models in Django

[https://github.com/omeatai/src-python-flask-django/commit/780144938397964962e4b786cfd724dc145045a8](https://github.com/omeatai/src-python-flask-django/commit/780144938397964962e4b786cfd724dc145045a8)

## Install Pillow

```py
pip install pillow
```

## Run Local Server

```py
python manage.py runserver
```

### jobs.models:

```py
from django.db import models
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # date = models.DateField()
    # description = models.TextField()
    # url = models.URLField()
    # company = models.CharField(max_length=100)
    # position = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)

```

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/659e18a7-99fc-44f0-bb89-5745f661bbf1">

# #END</details>

<details>
<summary>5. Setup PostgreSQL for Django </summary>

# Setup PostgreSQL for Django

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

<details>
<summary>+LinkedIn - Building a Personal Portfolio with Django </summary>

# #END</details>
