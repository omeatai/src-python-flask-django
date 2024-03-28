

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

[https://github.com/omeatai/src-python-flask-django/commit/5aaa98696ea594578f7e3f1c555d12d09660e028](https://github.com/omeatai/src-python-flask-django/commit/5aaa98696ea594578f7e3f1c555d12d09660e028)

[https://www.postgresql.org/](https://www.postgresql.org/)

## Create Password for Postgres

```x
postgres=# \password postgres
Enter new password for user "postgres": 
Enter it again: 
postgres=# 
```

## Create Portfolio Database

```py
postgres=# CREATE DATABASE portfoliodb;
CREATE DATABASE
postgres=# 
```

## Install Psycopg2

```py
pip install psycopg2
```

## Install Django-environ

```py
pip install django-environ
```

- In the same directory as settings.py, create a file called ‘.env’
- Declare your environment variables in .env
- Make sure you don’t use quotations around strings.
- IMPORTANT: Add your .env file to .gitignore

```x
DATABASE_NAME=portfoliodb
DATABASE_USER=postgres
DATABASE_PASS=supersecretpassword
```

### portfolio.settings:

```py
import environ
env = environ.Env()
environ.Env.read_env()


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER': 'postgres',
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': 'localhost',  # 127.0.0.1
        'PORT': '5432',
    }
}
```

## Run Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## Run Local Server

```py
python manage.py runserver
```

<img width="219" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8496d476-8a7b-45c5-a341-90a38678b92b">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f9f8740a-553c-4c7b-a15f-3db5666610ff)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1fac7b3b-53ea-4502-8f20-4059048635a0)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/4ea617c9-716f-467d-bad9-aa8a0e041790)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ad3b1721-236b-443a-a965-8d66e25f6da9)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/624f2fb3-e3aa-40e1-88b4-5d19962d5835)

<img width="763" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/afbe7d2d-4a88-4086-bcf7-b85fef9180a4">
<img width="763" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ecbf236f-1aa8-485e-aced-918c2e01e41a">
<img width="682" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0c4e4d73-ef28-41cd-a513-ba24628a81c4">
<img width="671" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ff5df38d-cfcd-44fb-bf94-83126f6914be">
<img width="763" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/819787d6-f111-4cd0-9d46-75b4ba63c086">
<img width="862" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/776130c5-d56d-40e8-8a9b-6611d90afbcd">
<img width="1426" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/eaf5ffd0-c3b0-4e4c-b9ac-ce00a39cc110">
<img width="1426" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/26b48359-2810-4a22-a895-d0a7c3d3055a">

# #END</details>

<details>
<summary>6. Setup Django Admin Panel  </summary>

# Setup Django Admin Panel 

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
