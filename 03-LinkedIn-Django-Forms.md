
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

[https://github.com/omeatai/src-python-flask-django/commit/c736d189596b7caa3597f762b1afbe344912c42b](https://github.com/omeatai/src-python-flask-django/commit/c736d189596b7caa3597f762b1afbe344912c42b)

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

    <form>
        <div>
            <label for="topping1">Topping 1: </label>
            <input type="text" id="topping1" name="topping1">
            <label for="topping2">Topping 2: </label>
            <input type="text" id="topping2" name="topping2">
            <label for="size">Size: </label>
            <select name="size" id="size">
                <option value="small">Small</option>
                <option value="medium">Medium</option>
                <option value="large">Large</option>
            </select>
        </div>
    </form>
</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a0e9d418-23bb-438c-b6cf-d6462fd2ac63)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/eea37d7a-f6a2-4954-84c3-5c9ab5530bc0">

# #END</details>

<details>
<summary>5. Submitting Forms </summary>

# Submitting Forms

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

    <form action="{% url 'order' %}" method="post">
        {% csrf_token %}
        <div>
            <label for="topping1">Topping 1: </label>
            <input type="text" id="topping1" name="topping1">
            <label for="topping2">Topping 2: </label>
            <input type="text" id="topping2" name="topping2">
            <label for="size">Size: </label>
            <select name="size" id="size">
                <option value="small">Small</option>
                <option value="medium">Medium</option>
                <option value="large">Large</option>
            </select>
            <input type="submit" value="Order Pizza">
        </div>
    </form>
</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b5bb0727-f8c9-4e0a-8634-430117c3ea55">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6a19534c-52c2-4c58-a57d-c3c4c5ebbc3f">

# #END</details>

<details>
<summary>6. Django Form Class </summary>

# Django Form Class

[https://github.com/omeatai/src-python-flask-django/commit/aac29045cc48a4a8130804c301196727c6076ccf](https://github.com/omeatai/src-python-flask-django/commit/aac29045cc48a4a8130804c301196727c6076ccf)

### pizza.forms:

```py
from django import forms


CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=CHOICES)

```

### pizza.views:

```py
from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    form = PizzaForm()
    return render(request, 'pizza/order.html', {'form': form})

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

    <form action="{% url 'order' %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Order Pizza">

        {% comment %} <div>
            <label for="topping1">Topping 1: </label>
            <input type="text" id="topping1" name="topping1">
            <label for="topping2">Topping 2: </label>
            <input type="text" id="topping2" name="topping2">
            <label for="size">Size: </label>
            <select name="size" id="size">
                <option value="small">Small</option>
                <option value="medium">Medium</option>
                <option value="large">Large</option>
            </select>
            <input type="submit" value="Order Pizza">
        </div> {% endcomment %}
    </form>
</body>

</html>

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8e3ec26a-ff38-406c-9876-71aa31cf2ceb">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a660edbe-8b71-49c4-a9e3-48ff05d1aa0d">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/963c5324-57b2-4428-8a6c-eb7055364908">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e972105a-a753-4b41-b065-5348fef9a26e">

# #END</details>

<details>
<summary>7. Using Submitted Data </summary>

# Using Submitted Data

[https://github.com/omeatai/src-python-flask-django/commit/fb0f8ea1b17786714e1a30a1e9fbb44c801276c7](https://github.com/omeatai/src-python-flask-django/commit/fb0f8ea1b17786714e1a30a1e9fbb44c801276c7)

### pizza.forms:

```py
from django import forms


CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=CHOICES)

```

### pizza.views:

```py
from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'form': empty_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form})

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

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <form action="{% url 'order' %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Order Pizza">

    </form>
</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/21c1e785-3929-4076-89b5-df14c7ef6fe5">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bcac377d-c2b0-41fe-b847-fe396890eafe">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4dcc8164-592a-47dd-aed9-de696bedf658">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/547c4336-44cf-4724-a8db-2aadc808bab5">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/88dd2d26-aaf0-4004-b0dc-d7afed925ad3">

# #END</details>

<details>
<summary>8. Adding Models to Form </summary>

# Adding Models to Form

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
