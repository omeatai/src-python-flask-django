
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
<summary>8. Creating Models for Form </summary>

# Creating Models for Form

[https://github.com/omeatai/src-python-flask-django/commit/f89abad1ceb7bee49234637369082b023fa5ebf8](https://github.com/omeatai/src-python-flask-django/commit/f89abad1ceb7bee49234637369082b023fa5ebf8)

## Make Migrations 

```py
python manage.py makemigrations
python manage.py migrate
```

## Create Super User

```py
python manage.py createsuperuser
```

## Run Development Server

```py
python manage.py runserver
```

### pizza.forms:

```py
from django import forms


CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=CHOICES)

```

### pizza.models:

```py
from django.db import models

# Create your models here.


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

```

### pizza.admin:

```py
from django.contrib import admin
from .models import Size, Pizza
# Register your models here.

admin.site.register(Size)
admin.site.register(Pizza)

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/02333abe-6f41-4ee2-98e8-5f670116a8c3">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a96685b8-a537-4d13-9086-8e155e36e076">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/df10d946-508c-42f7-87d1-cb9d34f0be74">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c2d5e5a5-e994-4c4f-ad81-533753fdc4d1">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0ce4832c-1485-409b-8f17-97ca24a61aa0">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7373b861-af9b-470c-9c7b-a34935550018">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8c8450d9-abd9-4b6a-b067-6b7a18d8efe5">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/92e1f04a-34e1-49db-8198-16b421312c28">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/864babcc-7712-4223-a852-e6508b215e90">

<img width="574" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/45d5e1ae-394e-48d4-b118-99fe34aa6540">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c4077616-46e0-4c94-bdc4-d43c65d0c5db">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7b90815a-73c2-47f5-abf7-41e7525a7e95">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6645dc42-e412-47f9-94ed-4326c01d3541">

# #END</details>

<details>
<summary>9. Using Model Forms </summary>

# Using Model Forms

[https://github.com/omeatai/src-python-flask-django/commit/db771cdf8a0227c81712ed81236793b2866aff0d](https://github.com/omeatai/src-python-flask-django/commit/db771cdf8a0227c81712ed81236793b2866aff0d)

### pizza.models:

```py
from django.db import models

# Create your models here.


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

```

### pizza.forms:

```py
from django import forms
from .models import Pizza

# CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

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

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e7b73289-e729-424e-86a8-089afc7850d1">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e8a819a6-7d5e-486d-aead-d06369416097">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/58b91581-64bd-4f81-bfbd-390921624929">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a6680012-2f05-4e7a-bdc6-63cda3dae49d">

# #END</details>

<details>
<summary>10. Using Basic Widgets </summary>

# Using Basic Widgets

[https://github.com/omeatai/src-python-flask-django/commit/eec165edc52314c140f3851a194e3fbea367a04b](https://github.com/omeatai/src-python-flask-django/commit/eec165edc52314c140f3851a194e3fbea367a04b)

### pizza.forms:

```py
from django import forms
from .models import Pizza

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


class PizzaForm(forms.Form):
    topping_1 = forms.CharField(label='Topping_1', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    topping_2 = forms.CharField(label='Topping_2', max_length=100, widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    topping_3 = forms.CharField(
        label='Topping_3', max_length=100, widget=forms.PasswordInput)
    topping_4 = forms.MultipleChoiceField(
        label='Topping_4', choices=TOPPING_CHOICES)
    topping_5 = forms.MultipleChoiceField(
        label='Topping_5', choices=TOPPING_CHOICES, widget=forms.CheckboxSelectMultiple)

    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=CHOICES)

# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['topping1', 'topping2', 'size']
#         labels = {
#             'topping1': 'Topping 1',
#             'topping2': 'Topping 2',
#             'size': 'Size',
#         }

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/023aeeb7-b388-488a-a8d7-70138f882e95">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/24c89464-963d-492e-8f96-1c0e241388fd">

# #END</details>

<details>
<summary>11. Using Widgets for Model Form </summary>

# Using Widgets for Model Form

[https://github.com/omeatai/src-python-flask-django/commit/9d3d91c02d14ecab171e51fb4410f5f81cefa426](https://github.com/omeatai/src-python-flask-django/commit/9d3d91c02d14ecab171e51fb4410f5f81cefa426)

### pizza.forms:

```py
from django import forms
from .models import Pizza, Size

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):

    size = forms.ModelChoiceField(
        # queryset=Size.objects.all(), to_field_name='title', empty_label=None, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
        queryset=Size.objects.all(), to_field_name='title', empty_label=None, widget=forms.RadioSelect(attrs={'class': 'form-control'}))

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        # widgets = {
        #     'topping1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'topping2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'size': forms.Select(attrs={'class': 'form-control'}),
        # }

        # widgets = {
        #     'topping1': forms.Textarea(attrs={'class': 'form-control'}),
        #     'topping2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'size': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        # }

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fea26596-9a4b-45d7-8435-212a3e1edd8c">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b82bf792-bb2f-47b2-89a9-72336bdd7460">

# #END</details>

<details>
<summary>12. Working with Files in Forms </summary>

# Working with Files in Forms

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
