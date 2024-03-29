
## +LinkedIn - Django Forms

<details>
<summary>1. Creating a New Django Project </summary>

# Creating a New Django Project

## Install venv

```py
python -m venv myproject-env

pip install virtualenv
virtualenv myproject-env
```

## Activate venv

```py
# myproject-env\Scripts\activate
source myproject-env/bin/activate
```

## Install Django

```py
python -m pip install Django

pip install Django
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
django-admin startproject anyisgarden .
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

# #END</details>

<details>
<summary>2. Create new App - Pizza </summary>

# Create new App - Pizza

[https://github.com/omeatai/src-python-flask-django/commit/df963c5ff37c50149f4ed82e4bca7451d4d0f71c](https://github.com/omeatai/src-python-flask-django/commit/df963c5ff37c50149f4ed82e4bca7451d4d0f71c)

```py
django-admin startapp pizza
```

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/83f17f2c-e00f-4154-a02e-3812f7ed11b6">

# #END</details>

<details>
<summary>3. Create Homepage and Order Page </summary>

# Create Homepage and Order Page

[https://github.com/omeatai/src-python-flask-django/commit/c5141aba40c0f8e13be4e8cf1bc081aeec1810e4](https://github.com/omeatai/src-python-flask-django/commit/c5141aba40c0f8e13be4e8cf1bc081aeec1810e4)

### anyisgarden.settings:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pizza',
]

```

### anyisgarden.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizza.urls')),
]

```

### pizza.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
]

```

### pizza.views:

```py
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    return render(request, 'pizza/order.html')

```

### src-python/linkedin/django-forms/pizza/templates/pizza/home.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anyi's garden</title>
</head>

<body>
    <h1>Anyi's Garden</h1>
    <a href="{% url 'order' %}">Order a pizza</a>
</body>

</html>
```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
</head>

<body>
    <h1>Order Pizza Form</h1>
</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/839178ea-5101-492f-a904-f57f2678c8c5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/138eca54-b81b-457b-b5b7-e0ba9d190809)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1c063cc4-0a77-492b-b172-5bc91d089b6b">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/41e065ce-2c52-4922-bef0-b51ed2b2e6f7">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/947ff739-77c8-4e6d-b20b-5aeff3081743">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e4df8a46-dadf-42af-b33a-a2cff102716b">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8a90fcba-2eab-4e35-b581-29e79a81c208">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/cd994088-56f5-4d8e-8c87-79490dfd0202">

# #END</details>

<details>
<summary>4. Create Form Fields </summary>

# Create Form Fields

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
<summary>+LinkedIn - Django Forms </summary>

# #END</details>
