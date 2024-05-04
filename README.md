#SRC-PYTHON-FLASK-DJANGO

<details>
<summary>+LinkedIn - Django Essential Training </summary>

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
<summary>10. Setup Admin for data creation and manipulation</summary>

# Setup Admin for data creation and manipulation

[https://github.com/omeatai/src-python-flask-django/commit/fe4590e92ae3f0ac735f5950c8660cf79aed015b](https://github.com/omeatai/src-python-flask-django/commit/fe4590e92ae3f0ac735f5950c8660cf79aed015b)

### notes.admin:

```py
from django.contrib import admin
from . import models
# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated',)
    verbose_name = "Note"
    verbose_name_plural = "Notes"

    # def get_model_name(self):
    #     return "Notes"


admin.site.register(models.Notes, NotesAdmin)
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

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
```

## Run migrations

```py
python manage.py makemigrations
python manage.py migrate
```

<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/44e70011-13a8-4329-98e8-de55d982840e">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d2b2e809-b98c-4bf9-97bc-a539bb352808">
<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/354f952d-e64f-4956-ada8-c9c1461ed99c">
<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6c302e29-1e1d-4400-a752-c38955302f1f">
<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e187c091-b598-40e3-82f4-10f61cbe8d95">

# #END</details>

<details>
<summary>11. Using Django shell for creating and querying data</summary>

# Using Django shell for creating and querying data

## Run Shell:

```py
python manage.py shell
```

## Get Instance of Model Object

```py
from notes.models import Notes
mynote = Notes.objects.get(pk=1)

mynote.title
# 'Make food'

mynote.content
# 'This is how to make the food'
```

## Get all Object Instances

```py
 Notes.objects.all()
# <QuerySet [<Notes: Make food>]>
```

## Create New Object Instance

```py
new_note = Notes.objects.create(title="The second note", content="This is the second note.")

Notes.objects.all()
# <QuerySet [<Notes: Make food>, <Notes: The second note>]>
```

## Filter and Exclude contents

```py
Notes.objects.filter(title__startswith="The")
# <QuerySet [<Notes: The second note>]>

Notes.objects.filter(content__icontains="food")
#  <QuerySet [<Notes: Make food>]>

Notes.objects.exclude(content__icontains="food")
# <QuerySet [<Notes: The second note>]>

Notes.objects.filter(content__icontains="food").exclude(content__icontains="second")
# <QuerySet [<Notes: Make food>]>
```

# #END</details>

<details>
<summary>12. Creating Dynamic Templates - Display all Notes </summary>

# Creating Dynamic Templates - Display all Notes

[https://github.com/omeatai/src-python-flask-django/commit/a135c2a03da27f098e6d5e3a508ffa2746745e96](https://github.com/omeatai/src-python-flask-django/commit/a135c2a03da27f098e6d5e3a508ffa2746745e96)

### notes.models:

```py
from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
```

### smartnotes.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('smart/', include('notes.urls')),
]
```

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.list),
]
```

### notes.views:

```py
from django.shortcuts import render
from .models import Notes

# Create your views here.


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})
```

### notes/notes_list.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notes</title>
</head>

<body>
    <h1>Note List</h1>
    <h2>These are the notes:</h2>
    <ul>
        {% for note in notes %}
        <li>{{note.title}}</li>
        {% endfor %}
    </ul>
</body>

</html>
```

<img width="1409" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a93749d6-a319-421f-b211-3288eecc3786">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ebcd35d1-e9b4-4dd9-88de-028296c7ef34">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0ccaf7cd-59bb-47b9-bf10-1dd7123819dd">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1b70d099-f746-4499-a1bb-99f82baaa8ab">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2422a6ee-56fd-4479-baca-80f33bb664e4">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/330aee64-8204-45ba-975c-d34e33a16019">

# #END</details>

<details>
<summary>13. Creating Dynamic Templates - Display content of a single note w 404 Page </summary>

# Creating Dynamic Templates - Display content of a single note w 404 Page

[https://github.com/omeatai/src-python-flask-django/commit/6a213c7aa46ec24c6017a44bad60269918eaf2a0](https://github.com/omeatai/src-python-flask-django/commit/6a213c7aa46ec24c6017a44bad60269918eaf2a0)

### smartnotes.settings:

```py
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # True

ALLOWED_HOSTS = ['*']


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

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>', views.detail),
]
```

### notes.views:

```py
from django.shortcuts import render
from django.http import Http404

from .models import Notes

# Create your views here.


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/notes_detail.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Note Detail</title>
</head>

<body>
    <h1>{{note.title | title}}</h1>
    <h3>{{note.content}}</h3>
</body>

</html>
```

### notes/templates/404.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Page</title>
</head>

<body>
    <h1>404 - Ooops!</h1>
    <h2>I cannot find the file you requested!</h2>
</body>

</html>
```

<img width="1409" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/10aa4c56-be8b-4bc6-ba6b-fe52dcf11389">
<img width="1409" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/01259842-9e6f-4a09-9091-10b36c1e636d">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/43c1eb4e-fbfd-4ffb-930f-37db29b0e50d">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e6dabf44-5720-492e-9272-6f2e7f8bae55">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f637fb96-364d-4acd-9c64-3aed91a93080">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ff107b00-75b3-4da7-891a-28b40ad0b797">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0a26901f-dad5-4686-9fd6-cc9b18970de1">

# #END</details>

<details>
<summary>14. Django Class Based Views - TemplateView </summary>

# Django Class Based Views - TemplateView

[https://github.com/omeatai/src-python-flask-django/commit/1e10260f38b8bf5b6804d6f45b9f4bf61b1c2edf](https://github.com/omeatai/src-python-flask-django/commit/1e10260f38b8bf5b6804d6f45b9f4bf61b1c2edf)

### home.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'John Doe', 'date': datetime.now()}


# def home(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {}
    login_url = '/admin'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
```

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    # path('home', views.home),
    path('home', views.HomeView.as_view()),
    # path('authorized', views.authorized),
    path('authorized', views.AuthorizedView.as_view()),
]
```

<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/27480e31-f225-49ee-aba2-b9a149a9323d">
<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fb460d21-b9a7-4799-961f-56bc751d5121">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1b2b17f3-5d1c-48bd-9364-25374c1ce361">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2c4dbd20-39b2-4adb-bc28-ffcac9089466">

# #END</details>

<details>
<summary>15. Django Class Based Views - ListView </summary>

# Django Class Based Views - ListView

[https://github.com/omeatai/src-python-flask-django/commit/3f935498be33171d56e127482e771f199787ab6c](https://github.com/omeatai/src-python-flask-django/commit/3f935498be33171d56e127482e771f199787ab6c)

### notes.views:

```py
from typing import Any
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView

from .models import Notes

# Create your views here.


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.detail),
]
```

### notes/templates/notes/notes_list.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notes</title>
</head>

<body>
    <h1>Note List</h1>
    <h2>These are the notes:</h2>
    <ul>
        {% for note in notes %}
        <li>{{note.title}}</li>
        {% endfor %}
    </ul>
</body>

</html>
```

<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8023729d-604c-4b71-9dfa-89fa4501c7cc">
<img width="1208" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/47e33038-8d50-413c-a88e-1eca9978a27d">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c369c75a-203c-46f5-9844-00796ae8904a">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0b3720e2-b860-4c42-b7bc-2eccb67e8fb8">

# #END</details>

<details>
<summary>16. Django Class Based Views - DetailView </summary>

# Django Class Based Views - DetailView

[https://github.com/omeatai/src-python-flask-django/commit/3dbc4628a9a8892e9098e455c03cb8c63e4253f5](https://github.com/omeatai/src-python-flask-django/commit/3dbc4628a9a8892e9098e455c03cb8c63e4253f5)

### smartnotes.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('smart/', include('notes.urls')),
]
```

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
]
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Notes

# Create your views here.


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/templates/notes/notes_list.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notes</title>
</head>

<body>
    <h1>Note List</h1>
    <h2>These are the notes:</h2>
    <ul>
        {% for note in notes %}
        <li>{{note.title}}</li>
        {% endfor %}
    </ul>
</body>

</html>
```

<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1be41d27-ca7b-421b-95f5-18d52c56fde7">
<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/72c45b25-dd04-409d-87a4-b5cf9c34d48d">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e5f7626e-d377-45eb-9ad2-ca78c7de2074">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/07094330-2eb9-4153-9b6e-a8796c2468ac">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/74a02860-d5d8-44cf-9dab-7e9ee5412633">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fdbf20ef-4a65-4623-a7cb-ba067f2a68ce">

# #END</details>

<details>
<summary>17. Static Files in Django - CSS in Template </summary>

# Static Files in Django - CSS in Template

[https://github.com/omeatai/src-python-flask-django/commit/c9a69902fd55e8eff47d658603800dab25cb0ab8](https://github.com/omeatai/src-python-flask-django/commit/c9a69902fd55e8eff47d658603800dab25cb0ab8)

### smartnotes.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

### static/notes/css/style.css:

```css
.note-li {
    color: blue;
    font-size: 18px;
    font-weight: 800;
}
```

### notes/templates/notes/notes_list.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}">
    <title>Notes</title>
</head>

<body>
    <h1>Note List</h1>
    <h2>These are the notes:</h2>
    <ul>
        {% for note in notes %}
        <li class="note-li">{{note.title}}</li>
        {% endfor %}
    </ul>
</body>

</html>
```

<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b43b561f-4547-41f3-afe7-de0ffe54d353">
<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9326acdd-5ae5-4bc8-b01d-3a87961fdec2">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/139b36d2-137b-4366-b175-103d50f6489c">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c2a15c08-1cb5-48f9-87a5-47d3bbea48f8">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/65ed74a3-2119-45ba-8bca-905b770b895c">

# #END</details>

<details>
<summary>18. Base HTML for Templates </summary>

# Base HTML for Templates

[https://github.com/omeatai/src-python-flask-django/commit/9e009fac7c4d43b7c5cae36dd13301e35079146e](https://github.com/omeatai/src-python-flask-django/commit/9e009fac7c4d43b7c5cae36dd13301e35079146e)

### smartnotes.settings:

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

### static/notes/css/style.css:

```css
.note-li {
    color: purple;
    font-size: 18px;
    font-weight: 800;
}

h2 {
    color: cadetblue;
}
```

### templates/notes/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}">
    <title>Notes</title>
</head>

<body>
    {% block content %}
    {% endblock content %}
</body>

</html>
```

### templates/notes/notes_list.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<h1>Note List</h1>
<h2>These are the notes:</h2>
<ul>
    {% for note in notes %}
    <li class="note-li">{{note.title}}</li>
    {% endfor %}
</ul>
{% endblock content %}
```

<img width="1430" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/047a9f2c-1e33-4827-8cab-c825ab3dd210">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/79af28af-7378-431b-abaa-b208e67194b5">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c2ef70e3-dd93-4455-83c5-f9d285bdb87b">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4423d5ed-de11-41c9-98f7-58d85515e682">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0ac816c0-cb25-49c5-843a-276784f40f71">

# #END</details>

<details>
<summary>19. Styling with Bootstrap and Linking Pages </summary>

# Styling with Bootstrap and Linking Pages

[https://github.com/omeatai/src-python-flask-django/commit/61b4a649138fba4700ea7ecac34d5babea955e80](https://github.com/omeatai/src-python-flask-django/commit/61b4a649138fba4700ea7ecac34d5babea955e80)

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
]
```

### templates/home/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>SmartNotes</title>
</head>

<body>
    <div class="my-5 text-center container">
        {% block content %}
        {% endblock content %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>
</body>

</html>
```

### home/templates/home/welcome.html:

```html
{% extends 'home/base.html' %}

{% block content %}
<h1>Welcome to SmartNotes Home Page - {{name}}.</h1>
<h2>Today is {{date}}</h2>
<a href="{% url 'notes-list' %}" class="btn btn-primary">Check out these SmartNotes</a>
{% endblock content %}
```

### templates/notes/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}">
    <title>Notes</title>
</head>

<body>
    <div class="my-5 text-center container">
        {% block content %}
        {% endblock content %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>
</body>

</html>
```

### notes/templates/notes/notes_list.html:

```html
{% extends 'notes/base.html' %}

{% block content %}
<h1>Note List</h1>
<h2 class="mb-5">These are the notes:</h2>

<div class="row row-cols3 g-2">
    {% for note in notes %}
    <div class="col">
        <div class="p-3 border">
            <a href="{% url 'notes-detail-list' pk=note.id %}" class="text-dark text-decoration-none">
                <h3>{{note.title | title}}</h3>
            </a>
            <p>{{note.content | truncatechars:30}}</p>
        </div>
    </div>
    {% endfor %}
</div>

{% endblock content %}
```

### notes/templates/notes/notes_detail.html:

```html
{% extends 'notes/base.html' %}

{% block content %}
<div class="border round">
    <h1 class="my-5">{{note.title | title}}</h1>
    <p>{{note.content}}</p>
</div>

{% endblock content %}
```

<img width="1453" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a9a658c5-2846-4604-92b0-a1f2b73c5e5d">
<img width="1453" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/340f8b96-1493-42ae-b0a3-5fe1a8c7cedb">
<img width="1453" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/25d5c2c3-fa4f-4976-89e3-de46118d1aea">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/63f9b354-057c-4c3a-b3a2-d9e526685efd">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f12343af-535e-4817-9ea2-b8aaa055e3fd">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3528ba4f-38f1-40d9-9e52-5c85a9a73c2a">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f8acfc54-55cc-471c-a24a-45841e71760f">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/91d083ca-a9b7-4696-ac40-507d024ec472">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e3e639e1-3b09-413c-8493-50c61914e06c">

# #END</details>

<details>
<summary>20. Django Class Based Views - CreateView </summary>

# Django Class Based Views - CreateView

[https://github.com/omeatai/src-python-flask-django/commit/2f833971f6a3e9d78c730e912bcb08105d79e8c9](https://github.com/omeatai/src-python-flask-django/commit/2f833971f6a3e9d78c730e912bcb08105d79e8c9)

### smartnotes.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('smart/', include('notes.urls')),
]
```

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
    path('notes/create', views.NotesCreateView.as_view(), name='notes-create'),
]
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import Notes

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/templates/notes/notes_create.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<form action="{% url 'notes-create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>

{% endblock content %}
```

<img width="1411" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1b131ba3-80fe-4ccd-9b3f-fc6fb1684f05">
<img width="1411" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/269ca0b6-300e-42de-abd4-94a63760f233">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0b81c59f-d6a6-46d0-8b6c-d91b224c1909">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/937c3f1a-7146-49d5-a646-822e7a71e42a">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e34fd8f9-3302-454b-ab2f-a4c8df055f8f">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ac2fdb6a-b470-4fc5-93e4-cfaf999cd9f9">

# #END</details>

<details>
<summary>21. Using Model Forms </summary>

# Using Model Forms

[https://github.com/omeatai/src-python-flask-django/commit/5afb11cc82683921b2d35eeb2928fe655b2a59c1](https://github.com/omeatai/src-python-flask-django/commit/5afb11cc82683921b2d35eeb2928fe655b2a59c1)

### notes.forms:

```py
from django import forms

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        labels = {
            'title': 'Title',
            'content': 'Content',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError(
                "Title must be at least 5 characters long.")
        if "Django" not in title:
            raise forms.ValidationError(
                "Title must contain the word 'Django'. We only accept notes about Django.")
        return title
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/templates/notes/notes_create.html:

```html
{% extends 'notes/base.html' %}

{% block content %}
<form action="{% url 'notes-create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>

{% if form.errors %}
<div class="alert alert-danger my-5">
    <div><strong>Oops!</strong> Something went wrong.</div>
    {{ form.errors.title.as_text }}
    <div>
        {% for field in form %}
        {% for error in field.errors %}
        <p>{{ error }}</p>
        {% endfor %}
        {% endfor %}
    </div>
</div>
{% endif %}

{% endblock content %}
```

### templates/notes/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}">
    <title>Notes</title>
</head>

<body>
    <div class="my-5 text-center container">
        {% block content %}
        {% endblock content %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>
</body>

</html>
```

### static/notes/css/style.css:

```css
.note-li {
    color: purple;
    font-size: 18px;
    font-weight: 800;
}

h2 {
    color: cadetblue;
}

ul.errorlist {
    display: none;
    color: red;
}
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a19e43ff-810f-4c52-bce2-f63665e9d520">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/128c4e30-94e7-4154-bf9e-0c68c227dc41">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9d71c552-9a5f-4159-bda8-951b60657f6a">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b7d2b308-70b8-490a-8ee5-a7a61a022abc">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3d358e29-53a3-45ca-aead-7e89a8a6dbb3">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d60a4b5e-d4a5-4ff3-a87e-d7c49e4316a3">

# #END</details>

<details>
<summary>22. Django Class Based Views - UpdateView </summary>

# Django Class Based Views - UpdateView

[https://github.com/omeatai/src-python-flask-django/commit/86fd903694ab1879f984b8c104499ca3980903bf](https://github.com/omeatai/src-python-flask-django/commit/86fd903694ab1879f984b8c104499ca3980903bf)

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
    path('notes/create', views.NotesCreateView.as_view(), name='notes-create'),
    path('notes/<int:pk>/edit',
         views.NotesUpdateView.as_view(), name='notes-update'),
]
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_update.html'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/templates/notes/notes_detail.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<div class="border round">
    <h1 class="my-5">{{note.title | title}}</h1>
    <p>{{note.content}}</p>
</div>

<a href="{% url 'notes-list' %}" class="btn btn-secondary my-5">Back</a>
<a href="{% url 'notes-update' pk=note.id %}" class="btn btn-secondary my-5">Edit</a>

{% endblock content %}
```

### notes/templates/notes/notes_update.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<form method="POST" class="my-5">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>

{% if form.errors %}
<div class="alert alert-danger my-5">
    <div><strong>Oops!</strong> Something went wrong.</div>
    {{ form.errors.title.as_text }}
    <div>
        {% for field in form %}
        {% for error in field.errors %}
        <p>{{ error }}</p>
        {% endfor %}
        {% endfor %}
    </div>
</div>
{% endif %}

<a href="{% url 'notes-list' %}" class="btn btn-secondary">Cancel</a>

{% endblock content %}
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8f757657-d69e-4d8c-8e5e-95e1c885246e">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ea7ea682-5762-43b2-9bd4-1c63a639abf7">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d05d8190-65c0-4ebf-a481-c424005a3ab4">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d3179dc8-05e7-43e6-8d9b-51669c6e9c5b">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a34446f2-c19a-41e8-a214-a786bc2cdf89">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a113079c-ae1f-4f0f-9ae8-2055abe7b575">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b1df57b1-b143-49c0-ba5a-7d07b55c7765">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a53b4b3e-6dae-492b-9aa0-bf3834631ec4">

# #END</details>

<details>
<summary>23. Django Class Based Views - DeleteView </summary>

# Django Class Based Views - DeleteView

[https://github.com/omeatai/src-python-flask-django/commit/ce92ed9ce5332eb39a9b48c0ff0ee6d0364b1cbc](https://github.com/omeatai/src-python-flask-django/commit/ce92ed9ce5332eb39a9b48c0ff0ee6d0364b1cbc)

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
    path('notes/create', views.NotesCreateView.as_view(), name='notes-create'),
    path('notes/<int:pk>/edit',
         views.NotesUpdateView.as_view(), name='notes-update'),
    path('notes/<int:pk>/delete',
         views.NotesDeleteView.as_view(), name='notes-delete'),
]
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_update.html'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})

```

### notes/templates/notes/notes_delete.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<form method="POST" class="my-5">
    {% csrf_token %}
    {{ form.as_p }}
    <p>Are you sure you want to delete "{{notes.title}}"?</p>
    <p>This action can't be undone.</p>
    <button type="submit" class="btn btn-danger">Confirm</button>
</form>

{% if form.errors %}
<div class="alert alert-danger my-5">
    <div><strong>Oops!</strong> Something went wrong.</div>
    {{ form.errors.title.as_text }}
    <div>
        {% for field in form %}
        {% for error in field.errors %}
        <p>{{ error }}</p>
        {% endfor %}
        {% endfor %}
    </div>
</div>
{% endif %}

<a href="{% url 'notes-list' %}" class="btn btn-secondary">Cancel</a>

{% endblock content %}
```

### notes/templates/notes/notes_detail.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<div class="border round">
    <h1 class="my-5">{{note.title | title}}</h1>
    <p>{{note.content}}</p>
</div>

<a href="{% url 'notes-list' %}" class="btn btn-secondary my-5">Back</a>
<a href="{% url 'notes-update' pk=note.id %}" class="btn btn-secondary my-5">Edit</a>
<a href="{% url 'notes-delete' pk=note.id %}" class="btn btn-danger my-5">Delete</a>

{% endblock content %}
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/11968d06-a6a0-4a13-b9f9-523704622728">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/eb5a165c-012d-4279-b796-17ab6135c727">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4ef12d30-fc42-43b9-aced-7c5115290249">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2c0dd2f5-d6f4-401a-90f1-7ecb8fb15d00">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/92e3e804-c948-4903-9b0d-56ef2c3a22c5">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ebc9e374-d39b-4ff6-a131-bbbcf6e258e7">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d2b82cbb-c3ad-4562-8b85-9e4ad48a9108">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2d9a1e2f-b050-46d1-b785-657a0b3cfcad">

# #END</details>

<details>
<summary>24. Django Model - ForeignKey Relationships </summary>

# Django Model - ForeignKey Relationships

[https://github.com/omeatai/src-python-flask-django/commit/2f06d43716aeec0be8dfd79e9e70f503c95f9cb3](https://github.com/omeatai/src-python-flask-django/commit/2f06d43716aeec0be8dfd79e9e70f503c95f9cb3)

### notes.models:

```py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
```

## Run Migration:

```py
python manage.py makemigrations
python manage.py migrate
```

```x
➜  myproject git:(main) ✗ python manage.py makemigrations
It is impossible to add a non-nullable field 'user' to notes without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> 1
Migrations for 'notes':
  notes/migrations/0003_notes_user.py
    - Add field user to notes
➜  myproject git:(main) ✗ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, notes, sessions
Running migrations:
  Applying notes.0003_notes_user... OK
➜  myproject git:(main) ✗ 
```

## Run Django Shell

```py
python manage.py shell
```

```x
➜  myproject git:(main) ✗ python manage.py shell
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.20.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from django.contrib.auth.models import User

In [2]: user = User.objects.get(pk=1)

In [3]: user
Out[3]: <User: admin>

In [4]: user.notes.count()
Out[4]: 1

In [5]: user.notes.all()
Out[5]: <QuerySet [<Notes: Make food>]>

In [6]: 

```

<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/89948b35-4faf-4e0c-b5ce-ff1404490ab7">


# #END</details>

<details>
<summary>25. Displaying Logged User Data with LoginRequiredMixin </summary>

# Displaying Logged User Data with LoginRequiredMixin

[https://github.com/omeatai/src-python-flask-django/commit/f14e0baa6a7c6e609002003120b5fc74ed461452](https://github.com/omeatai/src-python-flask-django/commit/f14e0baa6a7c6e609002003120b5fc74ed461452)

[https://ccbv.co.uk/](https://ccbv.co.uk/)

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_update.html'
    form_class = NotesForm


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10
    login_url = '/admin'

    def get_queryset(self):
        # return Notes.objects.filter(user=self.request.user).order_by('-created')
        return self.request.user.notes.all().order_by('-created')


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes.models:

```py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5f0c9a42-25ec-4d2f-8dbe-6968a85cb2f4">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a2f8a5d4-6dd1-409e-99ef-1b543d9e1621">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b7080570-2ea6-40f1-b54d-420e87fbe425">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4313ab0d-b0d4-4c40-8952-446c4bda0714">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bce92f56-1d35-4d3d-9941-d9d63e0322b9">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1a38113d-ace7-4186-be6c-d1e78953d14d">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1b628141-0818-44e6-b721-c57963b1239e">

# #END</details>

<details>
<summary>26. Login and Logout Functionality </summary>

# Login and Logout Functionality

[https://github.com/omeatai/src-python-flask-django/commit/c9570d056b9827de59c53f69197a19baabf48d50](https://github.com/omeatai/src-python-flask-django/commit/c9570d056b9827de59c53f69197a19baabf48d50)

### smartnotes.settings:

```py
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/smart/notes'
LOGIN_URL = '/login'
```

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    # path('home', views.home),
    path('', views.HomeView.as_view(), name='home'),
    # path('authorized', views.authorized),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
]
```

### home.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    http_method_names = ['get', 'post', 'options']

    def dispatch(self, request, *args, **kwargs):
        # return super().dispatch(request, *args, **kwargs)
        # Redirect to a specific URL after logout
        return redirect('/login')


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'John Doe', 'date': datetime.now()}


# def home(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {}
    login_url = '/admin'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
```

### src-python/django-essentials/myproject/home/templates/home/login.html:

```html
{% extends 'home/base.html' %}

{% block content %}
<h1>Login</h1>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type='submit' class="btn btn-secondary" />
</form>
{% endblock content %}
```

### src-python/django-essentials/myproject/home/templates/home/logout.html:

```html
{% extends 'home/base.html' %}

{% block content %}
<h1>Logout</h1>
<h2>Hope to see you soon :) </h2>
<p>You have successfully logged out.</p>
{% endblock content %}
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/80339acd-97c4-4b62-ba7a-c3b8913c698b">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3606efeb-5dc5-4aa0-b3ce-0474a32eeee1">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4bfc1e9b-4f3a-43a6-a348-b0dd8cad4f02">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f155eb3c-094c-4f9c-b516-39306b1ad39b">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5ff1d47c-9d01-413d-beb4-8f6b5c4ea402">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ce7fa2a6-aac4-4633-af32-c0dedd5e408f">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f768f703-993e-4519-9b07-ec003630d695">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/170cbc76-bb7f-475e-8f07-853ce2fa5aa6">

# #END</details>

<details>
<summary>27. Signup/Register Functionality </summary>

# Signup/Register Functionality

[https://github.com/omeatai/src-python-flask-django/commit/691b2d3a6dbc30a423f7be44f4bea53ef099b2ef](https://github.com/omeatai/src-python-flask-django/commit/691b2d3a6dbc30a423f7be44f4bea53ef099b2ef)

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    # path('home', views.home),
    path('', views.HomeView.as_view(), name='home'),
    # path('authorized', views.authorized),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
```

### home.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class UserSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user


class SignupView(CreateView):
    form_class = UserSignupForm  # UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    # model = User

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes-list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    http_method_names = ['get', 'post', 'options']

    def dispatch(self, request, *args, **kwargs):
        # return super().dispatch(request, *args, **kwargs)
        # Redirect to a specific URL after logout
        return redirect('/login')


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'John Doe', 'date': datetime.now()}


# def home(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {}
    login_url = '/admin'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# ### in views.py ###
# from django.contrib.auth import login as auth_login
# from .forms import RegisterForm
#
# def sign_up(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#     else:
#         form = RegisterForm()
#
#     return render(request, 'sign_up.html', {'form': form})
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_update.html'
    form_class = NotesForm


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10
    login_url = '/login'

    def get_queryset(self):
        # return Notes.objects.filter(user=self.request.user).order_by('-created')
        return self.request.user.notes.all().order_by('-created')


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### src-python/django-essentials/myproject/home/templates/home/register.html:

```py
{% extends 'home/base.html' %}

{% block content %}
<h1>Register</h1>

<form method="POST" style="text-align: left; margin: 0 auto; width: 600px">
    {% csrf_token %}
    {{ form.non_field_errors }}
    {% for field in form %}
    <div class="my-3">
        {% comment %} <label for="{{ form.field.id_for_label }}">Your {{field.label_tag}}</label> {% endcomment %}
        {{ field.label_tag }}
        {{ field }}
        {{ field.errors }}
    </div>
    {% endfor %}
    <input type='submit' class="btn btn-secondary" name="submit" />
</form>

<hr />

<form method="POST" style="text-align: left; margin: 0 auto; width: 600px">
    {% csrf_token %}
    {{ form.non_field_errors }}
    {{ form.as_p }}
    <input type='submit' class="btn btn-secondary" name="submit" />
</form>

{% endblock content %}
```

<img width="1367" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b318e50a-1ec6-4d74-9906-4c87cdb366cf">
<img width="1367" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0a8e48a8-5621-489b-8612-2c2208702998">
<img width="1367" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0705c63c-0aa1-465d-b7cf-e139ee16e720">
<img width="1171" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ef5c18af-283c-4850-979e-c6aa6251a747">
<img width="1171" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b9e26ef9-c351-4a64-87cc-36ed5161f809">
<img width="1171" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/504f4ad6-ff04-4e2d-b778-c5f23425b6d5">
<img width="1171" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/23df12a4-5734-4058-8a11-7cb53f4b4c44">

# #END</details>

<details>
<summary>28. Creating Nav Menu </summary>

# Creating Nav Menu

[https://github.com/omeatai/src-python-flask-django/commit/02788d37cbaf2ec7804ba1e66fb9c39ca166903f](https://github.com/omeatai/src-python-flask-django/commit/02788d37cbaf2ec7804ba1e66fb9c39ca166903f)

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    # path('home', views.home),
    path('', views.HomeView.as_view(), name='home'),
    # path('authorized', views.authorized),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
```

### home.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    http_method_names = ['get', 'post', 'options']

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        logout(request)
        # Redirect to a specific URL after logout
        return redirect('/login')


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)


class UserSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user


class SignupView(CreateView):
    form_class = UserSignupForm  # UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    # model = User

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes-list')
        return super().get(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'John Doe', 'date': datetime.now()}
    login_url = '/login'


# def home(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {}
    login_url = '/login'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# ### in views.py ###
# from django.contrib.auth import login as auth_login
# from .forms import RegisterForm
#
# def sign_up(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#     else:
#         form = RegisterForm()
#
#     return render(request, 'sign_up.html', {'form': form})

```

### src-python/django-essentials/myproject/templates/home/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>SmartNotes</title>
</head>

<body>
    <nav class="navbar navbar-dark bg-dark">
        <div class="ms-auto">
            <div class="navbar-nav ms-auto flex-row my-2">

                {% if user.is_authenticated %}
                <a class="btn btn-outline-light me-1" href="{% url 'home' %}">Home</a>
                <a class="btn btn-outline-light me-1" href="{% url 'notes-list' %}">Notes</a>
                <a class="btn btn-outline-light me-1" href="{% url 'notes-create' %}">Create Note</a>
                <a class="btn btn-outline-light me-1" href="{% url 'logout' %}">Logout</a>

                {% else %}

                <a class="btn btn-outline-light me-1" href="{% url 'login' %}">Login</a>
                <a class="btn btn-outline-light me-1" href="{% url 'signup' %}">Register</a>

                {% endif %}

            </div>
        </div>
    </nav>
    <div class="my-5 text-center container">
        {% block content %}
        {% endblock content %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>
</body>

</html>
```

### src-python/django-essentials/myproject/templates/notes/base.html:

```py
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}">
    <title>Notes</title>
</head>

<body>

    <nav class="navbar navbar-dark bg-dark">
        <div class="ms-auto">
            <div class="navbar-nav ms-auto flex-row my-2">

                {% if user.is_authenticated %}
                <a class="btn btn-outline-light me-1" href="{% url 'home' %}">Home</a>
                <a class="btn btn-outline-light me-1" href="{% url 'notes-list' %}">Notes</a>
                <a class="btn btn-outline-light me-1" href="{% url 'notes-create' %}">Create Note</a>
                <a class="btn btn-outline-light me-1" href="{% url 'logout' %}">Logout</a>

                {% else %}

                <a class="btn btn-outline-light me-1" href="{% url 'login' %}">Login</a>
                <a class="btn btn-outline-light me-1" href="{% url 'signup' %}">Register</a>

                {% endif %}

            </div>
        </div>
    </nav>
    <div class="my-5 text-center container">
        {% block content %}
        {% endblock content %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>
</body>

</html>
```

<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b4c676ce-9151-47a0-8b77-48f1c9c44eb3">
<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/675aa88b-b303-4145-afd8-145d42718841">
<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0e50370e-0462-4ca2-84e2-8bbaed473bbd">
<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5d6afec2-d8c6-4f7e-86c2-fe862e0046ff">
<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4ae490ee-34fe-4700-a096-f70509858fe3">

# #END</details>


# #END</details>




<details>
<summary>+LinkedIn - Building a Personal Portfolio with Django </summary>
    
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

[https://github.com/omeatai/src-python-flask-django/commit/f453a68d89b1d7c15c30a0b643a6a951daeed426](https://github.com/omeatai/src-python-flask-django/commit/f453a68d89b1d7c15c30a0b643a6a951daeed426)

## Create Django Superuser

```py
python manage.py createsuperuser
```

### jobs.admin:

```py
from django.contrib import admin
from .models import Job

# Register your models here.
admin.site.register(Job)

```

<img width="1420" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8fb2e7d4-8286-4c98-898c-28ca77657600">

### http://127.0.0.1:8000/admin:

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/11c7e95e-81bd-464a-a64f-1fa552505d75)

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f08f528c-a223-40d9-86bb-972822a792fd">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0a39b127-762a-44e6-b6b4-b87125f1b672">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/913b54ae-1451-4141-b26d-64f749744be1">

# #END</details>

<details>
<summary>7. Create Jobs in Admin Panel  </summary>

# Create Jobs in Admin Panel 

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/14c47c31-3ff2-4291-98cc-b1710bfa2fb7">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b2104630-2119-4ea8-aa59-f40c8b96e0d6">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/26bcbd51-d1b1-419d-bfa2-5f1f815c3eae">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b89e3927-91d1-4ed4-9067-5abc0a89b47e">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e98c9874-92a5-4554-909e-36a1e18d69ed">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a3ad9af0-961d-4f84-8536-ca38ce711f76">

# #END</details>

<details>
<summary>8. Pulling Objects from Database  </summary>

# Pulling Objects from Database

[https://github.com/omeatai/src-python-flask-django/commit/500292e12ff3a34d76c09906963794c007e6987f](https://github.com/omeatai/src-python-flask-django/commit/500292e12ff3a34d76c09906963794c007e6987f)

### jobs.views:

```py
from django.shortcuts import render
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HomePage</title>
</head>

<body>
    <h1>All my Jobs</h1>
    {% for job in jobs %}
    <h2>{{ job.title }}</h2>
    <p>{{ job.summary }}</p>
    <img src='/images/1.webp' alt='{{ job.title }}' />
    {% endfor %}
</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ebf8c8de-6df9-4d65-bd75-e6fb86dfee69">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/be86c166-c5eb-414b-b684-5f76cedc83e8">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7b9adf65-1756-4326-bb5f-4ad5456e29b9">

# #END</details>

<details>
<summary>9. Bootstrap Layout and Template </summary>

# Bootstrap Layout and Template

[https://github.com/omeatai/src-python-flask-django/commit/ea34e8361eb8fcc0bce828ecb85bc80626af85e0](https://github.com/omeatai/src-python-flask-django/commit/ea34e8361eb8fcc0bce828ecb85bc80626af85e0)

[https://getbootstrap.com/](https://getbootstrap.com/)
[https://getbootstrap.com/docs/5.3/examples/album/](https://getbootstrap.com/docs/5.3/examples/album/)

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

### jobs.views:

```py
from django.shortcuts import render
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.122.0">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <!-- Favicons -->
    <link rel="apple-touch-icon" href="/docs/5.3/assets/img/favicons/apple-touch-icon.png" sizes="180x180">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
    <link rel="manifest" href="/docs/5.3/assets/img/favicons/manifest.json">
    <link rel="mask-icon" href="/docs/5.3/assets/img/favicons/safari-pinned-tab.svg" color="#712cf9">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon.ico">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    </div>
                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">
                            <svg class="bd-placeholder-img card-img-top" width="100%" height="225"
                                xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                                preserveAspectRatio="xMidYMid slice" focusable="false">
                                <title>{{ job.title }}</title>
                                <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef"
                                    dy=".3em">{{ job.title }}</text>
                            </svg>
                            <div class="card-body">
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                        <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>

</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/92c7b2f9-8bd5-4b19-a1be-4df99bbe6d6e">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/83029a5f-39fb-474d-8e5f-f9dbd9fef106)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/60bb6b74-5edf-4af6-bf21-f4bb419eb45f)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b08f30c9-4d92-4bc2-8c36-6ee3a4887014)

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/88573e62-ac0b-445d-b7f2-a088ef498a45">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/93eda305-2d48-4c6f-b04a-c50ed160e03e)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/63ef7e7f-96d3-482b-85c2-884f601d06c8)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fd7570c6-d16f-4de1-b85e-286b87b821be">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b3f13f6b-5571-4af2-926b-f308b6d23bbb">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b7e89d03-3817-40c4-9e90-a6a6172c7e42">

# #END</details>

<details>
<summary>10. Adding Static Images to Django </summary>

# Adding Static Images to Django

[https://github.com/omeatai/src-python-flask-django/commit/58911b297ac32d5da5a9921c81ac4acb2cd90bd5](https://github.com/omeatai/src-python-flask-django/commit/58911b297ac32d5da5a9921c81ac4acb2cd90bd5)

## Run Collectstatic (To add all static folders into a single main folder)

```py
python manage.py collectstatic
```

### portfolio.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### portfolio.urls:

```py
"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.122.0">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <!-- Favicons -->
    <link rel="apple-touch-icon" href="/docs/5.3/assets/img/favicons/apple-touch-icon.png" sizes="180x180">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
    <link rel="manifest" href="/docs/5.3/assets/img/favicons/manifest.json">
    <link rel="mask-icon" href="/docs/5.3/assets/img/favicons/safari-pinned-tab.svg" color="#712cf9">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon.ico">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                    <img src="{% static 'picofme.png' %}" width="300" alt="my profile pic" />
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">
                            <img src="{% static job.image %}" alt='{{job.title}}'
                                class="bd-placeholder-img card-img-top p-2 bg-black" width="100%" height="225" />
                            {% comment %} <svg class="bd-placeholder-img card-img-top" width="100%" height="225"
                                xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                                preserveAspectRatio="xMidYMid slice" focusable="false">
                                <title>{{ job.title }}</title>
                                <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef"
                                    dy=".3em">{{ job.title }}</text>
                            </svg> {% endcomment %}
                            <div class="card-body">
                                <h4>{{ job.title }}</h4>
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                        <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a0f520c5-a879-4ba2-979c-7626dafa8666)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7d0588a4-d71b-4dee-8a36-46766e05b0da)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4a5ba522-ba48-4f40-8260-6b8bfa9ec0db">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e51c9fec-d7e7-454a-b3a4-2c43608946ea">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/185ec6e9-c5f4-4450-b90f-8b96a6de83b6">

# #END</details>

<details>
<summary>11. Using Bootstrap Static Assets </summary>

# Using Bootstrap Static Assets

[https://github.com/omeatai/src-python-flask-django/commit/485bd4e3992354075db72461810cc21900f74677](https://github.com/omeatai/src-python-flask-django/commit/485bd4e3992354075db72461810cc21900f74677)

## Run Collectstatic (To add Bootstrap and Jquery static files into the main Static folder)

```py
python manage.py collectstatic
```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    {% comment %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    {% endcomment %}
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                    <img src="{% static 'picofme.png' %}" width="300" alt="my profile pic" />
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">
                            <img src="{% static job.image %}" alt='{{job.title}}'
                                class="bd-placeholder-img card-img-top p-2 bg-black" width="100%" height="225" />
                            {% comment %} <svg class="bd-placeholder-img card-img-top" width="100%" height="225"
                                xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                                preserveAspectRatio="xMidYMid slice" focusable="false">
                                <title>{{ job.title }}</title>
                                <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef"
                                    dy=".3em">{{ job.title }}</text>
                            </svg> {% endcomment %}
                            <div class="card-body">
                                <h4>{{ job.title }}</h4>
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                        <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    {% comment %} <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script> {% endcomment %}

</body>

</html>
```

#### Bootstrap Assets
[https://getbootstrap.com/docs/5.3/getting-started/download/](https://getbootstrap.com/docs/5.3/getting-started/download/)

#### JQuery Assets
[https://jquery.com/download/](https://jquery.com/download/)

#### Popper Assets
[https://github.com/vusion/popper.js/](https://github.com/vusion/popper.js/)

#### Popper.js now Floating-ui CDN
[https://github.com/floating-ui/floating-ui#installation](https://github.com/floating-ui/floating-ui#installation)
[https://floating-ui.com/docs/getting-started#cdn](https://floating-ui.com/docs/getting-started#cdn)

```html
<script src="https://cdn.jsdelivr.net/npm/@floating-ui/core@1.6.0"></script>
<script src="https://cdn.jsdelivr.net/npm/@floating-ui/dom@1.6.3"></script>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/86e47226-c7c0-474f-bfe5-dbf0500cfb4b)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/65b9c8d5-aeb7-4037-be7d-62e239d150e0)

<img width="1450" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/da652915-3973-472e-aecb-440d58559528">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/6ad250cc-6c94-4330-9cfc-5379d5cc4221)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/acfe694b-16bb-45f8-81c6-66e3f8afc627)

<img width="932" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8f849af8-f756-429b-8f8b-695887ffe3a7">

# #END</details>

<details>
<summary>12. Setup Media Folder for Media Files </summary>

# Setup Media Folder for Media Files

[https://github.com/omeatai/src-python-flask-django/commit/77db2bc76db3f37538be9094a42d1e1f546e51df](https://github.com/omeatai/src-python-flask-django/commit/77db2bc76db3f37538be9094a42d1e1f546e51df)

### portfolio.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### portfolio.urls:

```py
"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    {% comment %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    {% endcomment %}
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                    <img src="{% static 'picofme.png' %}" width="300" alt="my profile pic" />
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">
                            {% comment %} <img src="{% static job.image %}" alt='{{job.title}}'
                                class="bd-placeholder-img card-img-top p-2 bg-black" width="100%" height="225" />
                            {% endcomment %}
                            <img src="{{ job.image.url }}" alt='{{job.title}}'
                                class="bd-placeholder-img card-img-top p-2 bg-black" width="100%" height="225" />
                            {% comment %} <svg class="bd-placeholder-img card-img-top" width="100%" height="225"
                                xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                                preserveAspectRatio="xMidYMid slice" focusable="false">
                                <title>{{ job.title }}</title>
                                <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef"
                                    dy=".3em">{{ job.title }}</text>
                            </svg> {% endcomment %}
                            <div class="card-body">
                                <h4>{{ job.title }}</h4>
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                        <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                    <small class="text-body-secondary">{{ job.image.url }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    {% comment %} <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script> {% endcomment %}

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/bf2687ce-ab04-47bc-b134-a873e0fd778c)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1c1d5dce-9926-43b7-96df-5ace887e52ed">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3f463b18-9ec5-4f66-b7e4-1f444e997db9">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/882fa493-acdc-4f5c-9f99-f8539f5925e1">

# #END</details>

<details>
<summary>13. Setup Model Default String Name </summary>

# Setup Model Default String Name

[https://github.com/omeatai/src-python-flask-django/commit/77db2bc76db3f37538be9094a42d1e1f546e51df](https://github.com/omeatai/src-python-flask-django/commit/77db2bc76db3f37538be9094a42d1e1f546e51df)

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

    def __str__(self):
        return self.title
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/cc8f0e4b-5057-423b-be7a-1187673cd69d)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6f8bf4ef-3568-4ff6-b7fa-ca36c850af47">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b198f65d-c54e-430a-a15d-797614f25f1e)

# #END</details>

<details>
<summary>14. Setup URL, View and Template for Details Page </summary>

# Setup URL, View and Template for Details Page

[https://github.com/omeatai/src-python-flask-django/commit/c74f54e88a57b4951d882e75039720ef802a5794](https://github.com/omeatai/src-python-flask-django/commit/c74f54e88a57b4951d882e75039720ef802a5794)

### jobs.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/<int:job_id>', views.job_detail, name='job-detail'),
]

```

### jobs.views:

```py
from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})


def job_detail(request, job_id):
    # job = Job.objects.get(id=job_id)
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/job_detail.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">{{job.title}}</h1>
                    <p class="lead text-body-secondary">{{job.summary}}</p>
                    <p>
                        <a href="#" class="btn btn-primary my-2">Github</a>
                        <a href="#" class="btn btn-secondary my-2">View Demo</a>
                        <a href="{% url 'home' %}" class="btn btn-danger my-2">Back</a>
                    </p>
                    <img src="{{ job.image.url }}" alt='{{job.title}}' width="600" />
                </div>
            </div>
        </section>

    </main>

    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>

</body>

</html>
```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    {% comment %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    {% endcomment %}
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                    <img src="{% static 'picofme.png' %}" width="300" alt="my profile pic" />
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">

                            <a href="{% url 'job-detail' job.id %}"><img src="{{ job.image.url }}" alt='{{job.title}}'
                                    class="bd-placeholder-img card-img-top p-2 bg-black" width="100%"
                                    height="225" /></a>


                            <div class="card-body">
                                <h4>{{ job.title }}</h4>
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <a href="{% url 'job-detail' job.id %}" type="button"
                                            class="btn btn-sm btn-outline-secondary">View</a>
                                        <a href="{% url 'job-detail' job.id %}" type="button"
                                            class="btn btn-sm btn-outline-secondary">Edit</a>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                    <small class="text-body-secondary">{{ job.image.url }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    {% comment %} <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script> {% endcomment %}

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a5ae5547-bba5-4d7c-9702-0ffd26cbcfb5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/aab1e84c-23ba-46db-a85c-581633f90a52)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/d1aed37e-87c6-4ecd-b461-eef3e457b3cd)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3cd13c6e-9387-463c-897f-712e58c2813e">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5ddce9b9-0096-419a-8240-b4ab5a12f9c8">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9a10238f-4581-4dcc-aa82-4a24635ef8bf">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d7c7ddd8-d42f-4b23-9a64-fb45e6fc36e0">

# #END</details>

# #END</details>




<details>
<summary>+LinkedIn - Django Forms </summary>

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
<summary>12. Adding Files to Forms </summary>

# Adding Files to Forms

[https://github.com/omeatai/src-python-flask-django/commit/b507f6a78c7d9e2ab0f26dd8aa0426caf39d8f70](https://github.com/omeatai/src-python-flask-django/commit/b507f6a78c7d9e2ab0f26dd8aa0426caf39d8f70)

## Install Pillow:

```py
pip install pillow
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
        filled_form = PizzaForm(request.POST, request.FILES)
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

    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        widgets = {
            'topping1': forms.TextInput(attrs={'class': 'form-control'}),
            'topping2': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.RadioSelect(attrs={'class': 'form-control'}),
        }

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

    <form enctype="multipart/form-data" action="{% url 'order' %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Order Pizza">

    </form>
</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/351a6625-b2aa-4b54-b7d0-17dc44d50f38)

<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/cf8af387-957e-4e5d-bb3e-1b8f99516098">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ba6fe724-ae09-4e60-902e-d23b4b6bc0c5">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/87a24092-afeb-42d2-960a-97448b09fdd5">

# #END</details>

<details>
<summary>13. Using Formsets - Multiple Forms on a page </summary>

# Using Formsets - Multiple Forms on a page 

[https://github.com/omeatai/src-python-flask-django/commit/afd858b787522e90f3a0cab463c9384db471177a](https://github.com/omeatai/src-python-flask-django/commit/afd858b787522e90f3a0cab463c9384db471177a)

### pizza.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('orders', views.orders, name='orders'),
]

```

### pizza.views:

```py
from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'form': empty_form, 'note': note, "multiple_form": multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form, "multiple_form": multiple_form})


def orders(request):
    number_of_pizzas = 2
    filled_multi_form = MultiplePizzaForm(request.GET)

    if filled_multi_form.is_valid():
        number_of_pizzas = filled_multi_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data)
            note = "Multiple Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"
        return render(request, 'pizza/orders.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/orders.html', {'formset': formset})

```

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

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        widgets = {
            'topping1': forms.TextInput(attrs={'class': 'form-control'}),
            'topping2': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.RadioSelect(attrs={'class': 'form-control'}),
        }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)

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

    <div>
        <form action="{% url 'order' %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Order Pizza">
        </form>
        <br /><br />
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" value="Get Pizzas">
        </form>
    </div>

</body>

</html>
```

### src-python/linkedin/django-forms/pizza/templates/pizza/orders.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multiple Orders</title>
</head>

<body>
    <h1>Make your orders</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <div>
        <form action="{% url 'orders' %}" method="post">
            {% csrf_token %}
            {{ formset.management_form }}

            {% for form in formset %}
            {{ form.as_p }}
            <br />
            <hr>
            {% endfor %}
            <input type="submit" value="Order Pizzas">
            <a type="button" style="padding: 5px 20px; background: red; border-radius: 50px; color: white; "
                href="{% url 'order' %}">I
                want more
                orders</a>
        </form>
    </div>

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ce9acb71-82bf-44a9-837e-20a9964d3830)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8a89d00e-8628-482b-b2a4-822e841a94c7)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/23b9bfa5-c6a4-4ad6-84a3-42fec59cf5d8)

<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c99e3a90-aa0f-43ae-a74a-0ab8f1eb81a3">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/17149a9d-bcac-4fb9-887d-508c2e718ee4">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ea4a7d77-216a-4c86-bd60-a1d6d0f16727">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1c1b44cf-d754-4b9f-90c7-785dbaad46e8">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fd0f7177-5311-414b-8b0d-f45c49093313">

# #END</details>

<details>
<summary>14. Editing Pizza Orders </summary>

# Editing Pizza Orders

[https://github.com/omeatai/src-python-flask-django/commits/main/](https://github.com/omeatai/src-python-flask-django/commits/main/)

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

    def __str__(self):
        return f"{self.size} pizza with {self.topping1} and {self.topping2}."

```

### pizza.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('orders', views.orders, name='orders'),
    path('order/<int:pk>', views.edit_order, name='edit-order'),
]

```

### pizza.views:

```py
from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from .forms import PizzaForm, MultiplePizzaForm
from .models import Pizza
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'created_pizza_pk': created_pizza_pk, 'form': empty_form, 'note': note, "multiple_form": multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form, "multiple_form": multiple_form})


def orders(request):
    number_of_pizzas = 2
    filled_multi_form = MultiplePizzaForm(request.GET)

    if filled_multi_form.is_valid():
        number_of_pizzas = filled_multi_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data)
            note = "Multiple Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"
        return render(request, 'pizza/orders.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/orders.html', {'formset': formset})


def edit_order(request, pk):
    # pizza = Pizza.objects.get(pk=pk)
    pizza = get_object_or_404(Pizza, pk=pk)
    filled_form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            note = "Your order has been updated"
            return render(request, 'pizza/edit_order.html', {'form': filled_form, 'pizza': pizza, 'note': note})
    else:
        return render(request, 'pizza/edit_order.html', {'form': filled_form, 'pizza': pizza})

```

### src-python/linkedin/django-forms/pizza/templates/pizza/edit_order.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Pizza</title>
</head>

<body>
    <h1>Edit Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <div>
        <form action="{% url 'edit-order' pizza.pk %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Edit Your Order">
        </form>
        <br />
        <hr>
    </div>

</body>

</html>
```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
    <style>
        .btn {
            background-color: blue;
            border: none;
            border-radius: 50px;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <h1>Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    {% if created_pizza_pk %}
    <a href="{% url 'edit-order' created_pizza_pk %}" class="btn">Edit Your Order</a>
    {% endif %}

    <div>
        <form action="{% url 'order' %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Order Pizza">
        </form>
        <br /><br />
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" value="Get Pizzas">
        </form>
    </div>

</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a562667c-f6c3-4cb2-b524-e2047bde0db4">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ad62630b-08d6-4ccc-9aea-cff10e82dafd">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7d5b89c9-a063-49d3-acc6-45a34cca2020">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d94221cf-0bfd-4b9a-9078-83da01df3e98">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/28e93711-3018-41f8-ac25-bfaa769e71a9">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/22d67e7e-2e41-4535-b1f6-80e0ec61dd4e">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/78712b66-e122-4ee4-9f75-c5b3f001bd0a">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d3ac196d-1b11-4540-8f44-28681e09c087">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8f3938fd-6f72-4ea7-bb48-15ca656d73ba">

<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/34cd5e26-e5f6-4b69-8618-82782f802f39">
<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ba5d2371-f225-496b-9c48-4b603fef6252">
<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a1de2933-e7bc-4f24-8821-9b0fa0d80e40">
<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bb3f776b-b186-4eb9-bbb5-31a10afd7731">
<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3a883bed-719e-4363-bf24-64de5ef5ec28">

# #END</details>

<details>
<summary>15. Local and Server-based Validation Errors + Form Rendering </summary>

# Local and Server-based Validation Errors + Form Rendering

[https://github.com/omeatai/src-python-flask-django/commit/7381d6d1461ea4493f333249256d03973aac584b](https://github.com/omeatai/src-python-flask-django/commit/7381d6d1461ea4493f333249256d03973aac584b)

### pizza.views:

```py
from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from .forms import PizzaForm, MultiplePizzaForm
from .models import Pizza
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = "Order was not created, please try again"
        return render(request, 'pizza/order.html', {'created_pizza_pk': created_pizza_pk, 'form': filled_form, 'note': note, "multiple_form": multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form, "multiple_form": multiple_form})


def orders(request):
    number_of_pizzas = 2
    filled_multi_form = MultiplePizzaForm(request.GET)

    if filled_multi_form.is_valid():
        number_of_pizzas = filled_multi_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data)
            note = "Multiple Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"
        return render(request, 'pizza/orders.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/orders.html', {'formset': formset})


def edit_order(request, pk):
    # pizza = Pizza.objects.get(pk=pk)
    pizza = get_object_or_404(Pizza, pk=pk)
    filled_form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            note = "Your order has been updated"
            return render(request, 'pizza/edit_order.html', {'form': filled_form, 'pizza': pizza, 'note': note})
    else:
        return render(request, 'pizza/edit_order.html', {'form': filled_form, 'pizza': pizza})

```

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

    email = forms.EmailField()
    website = forms.URLField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        widgets = {
            'topping1': forms.TextInput(attrs={'class': 'form-control'}),
            'topping2': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.RadioSelect(attrs={'class': 'form-control'}),
        }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)

```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
    <style>
        .btn {
            background-color: blue;
            border: none;
            border-radius: 50px;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <h1>Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    {% if created_pizza_pk %}
    <a href="{% url 'edit-order' created_pizza_pk %}" class="btn">Edit Your Order</a>
    {% endif %}

    <div>
        {% comment %} <form action="{% url 'order' %}" method="post" novalidate> {% endcomment %}
            <form action="{% url 'order' %}" method="post">
                {% csrf_token %}
                {{ form.as_p }}

                <hr>
                <table>
                    {{ form.as_table }}
                </table>

                <hr>
                <ul>
                    {{ form.as_ul }}
                </ul>

                <hr>
                <ol>
                    {{ form.as_ul }}
                </ol>

                <hr>
                <input type="submit" value="Order Pizza">
            </form>
            <br /><br />
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" value="Get Pizzas">
        </form>
    </div>

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7f32d26e-cd50-4d3d-920c-08967032210a)

<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a45d64c8-9973-4156-8bd3-f815c6c85e12">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f93b5c1f-7849-426a-a48a-fa699f7a6dc3">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a7a3e182-09d7-4853-8258-75cc7ff3003e">

# #END</details>

<details>
<summary>16. Customizing Form Fields </summary>

# Customizing Form Fields

[https://github.com/omeatai/src-python-flask-django/commit/ee30329b2e87cb46b4869ee97399ae586f047316](https://github.com/omeatai/src-python-flask-django/commit/ee30329b2e87cb46b4869ee97399ae586f047316)

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
    <style>
        .btn {
            background-color: blue;
            border: none;
            border-radius: 50px;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <h1>Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    {% if created_pizza_pk %}
    <a href="{% url 'edit-order' created_pizza_pk %}" class="btn">Edit Your Order</a>
    {% endif %}

    <div>
        {% comment %} <form action="{% url 'order' %}" method="post" novalidate> {% endcomment %}
            <form action="{% url 'order' %}" method="post">
                {% csrf_token %}

                <div>
                    {{ form.topping1.label_tag }}
                    {{ form.topping1 }}
                    {{ form.topping1.errors }}
                </div>
                <br />
                <div>
                    {{ form.topping2.label_tag }}
                    {{ form.topping2 }}
                    {{ form.topping2.errors }}
                </div>
                <br />
                <div>
                    <label for="{{ form.size.id_for_label }}">Size for your Pizza:</label>
                    {% comment %} {{ form.size.label_tag }} {% endcomment %}
                    {{ form.size }}
                    {{ form.size.errors }}
                </div>
                <br />

                <input type="submit" value="Order Pizza">
            </form>
            <br /><br />
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" value="Get Pizzas">
        </form>
    </div>

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1395404d-ee25-4617-8f04-481504e3155f)

<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1fee9e3d-d27d-4c0f-b846-c4b0b379eb07">

# #END</details>

<details>
<summary>17. Using Base Template and Styling with Django-Widget-Tweaks and Bootstrap </summary>

# Using Base Template and Styling with Django-Widget-Tweaks and Bootstrap 

[https://github.com/omeatai/src-python-flask-django/commit/cc5e531355f58bffa3fd110c1a7d0b25c29272d7](https://github.com/omeatai/src-python-flask-django/commit/cc5e531355f58bffa3fd110c1a7d0b25c29272d7)

## Install Django Widget Tweaks

```py
pip install django-widget-tweaks
```

## Run Collect Static

```py
python manage.py collectstatic
```

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
    'widget_tweaks',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### src-python/linkedin/django-forms/pizza/templates/pizza/base.html:

```html
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Anyi's Garden</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>

    <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #238a44">
        <div class="container">
            <a class="navbar-brand" href="{% url 'home' %}">Nandia's Garden</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'order' %}">Order Pizza</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    {% block content %}
    {% endblock content %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>

</body>

</html>
```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
{% extends "pizza/base.html" %}

{% block content %}

{% load widget_tweaks %}

<div class="container">
    <h1 class="my-4">Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    {% if created_pizza_pk %}
    <a href="{% url 'edit-order' created_pizza_pk %}" class="btn btn-lg btn-primary">Edit Your Order</a>
    {% endif %}

    <div>
        {% comment %} <form action="{% url 'order' %}" method="post" novalidate> {% endcomment %}
            <form action="{% url 'order' %}" method="post">
                {% csrf_token %}

                {% for field in form %}

                <div class="form-group">
                    {{ field.label_tag }}
                    {% render_field field class="form-control" %}
                    {{ field.errors }}
                </div>
                <br />

                {% endfor %}

                <input type="submit" class="btn btn-lg btn-success" value="Order Pizza">
            </form>
            <br />
            <hr>
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" class="btn btn-lg btn-primary" value="Get Pizzas">
        </form>
    </div>

</div>

{% endblock content %}
```

### src-python/linkedin/django-forms/pizza/templates/pizza/orders.html:

```html
{% extends "pizza/base.html" %}

{% block content %}

<div class="container">
    <h1>Make your orders</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <div>
        <form action="{% url 'orders' %}" method="post">
            {% csrf_token %}
            {{ formset.management_form }}

            {% for form in formset %}
            {{ form.as_p }}
            <br />
            <hr>
            {% endfor %}
            <input type="submit" value="Order Pizzas">
            <a type="button" style="padding: 5px 20px; background: red; border-radius: 50px; color: white; "
                href="{% url 'order' %}">I
                want more
                orders</a>
        </form>
    </div>

</div>

{% endblock content %}
```

### src-python/linkedin/django-forms/pizza/templates/pizza/edit_order.html:

```html
{% extends "pizza/base.html" %}

{% block content %}

<div class="container">
    <h1>Edit Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <div>
        <form action="{% url 'edit-order' pizza.pk %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Edit Your Order">
        </form>
        <br />
        <hr>
    </div>

</div>

{% endblock content %}
```

### src-python/linkedin/django-forms/pizza/templates/pizza/home.html:

```html
{% extends "pizza/base.html" %}
{% load static %}

{% block content %}


<img src="{% static 'pizza.jpeg' %}" class="img-fluid w-100 min-h-screen" alt='Anyis Garden'></img>

<div>
    <a href="{% url 'order' %}" class="btn btn-toolbar btn-primary py-5">Order pizza</a>
</div>


{% endblock content%}
```

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

    # email = forms.EmailField()
    # website = forms.URLField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        widgets = {
            'topping1': forms.TextInput(attrs={'class': 'form-control'}),
            'topping2': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
        }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)

```

[https://getbootstrap.com/docs/5.3/getting-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8166e251-8d37-493a-80a7-e45dd1ebaf85)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/58250154-03cb-4e62-8cd4-82c14457cd37)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/4e6d0d2f-412a-4c5e-ace0-898a583f29c8)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e18c2df2-4eba-47d3-a49c-c7c6442df37e)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/18232db0-5f9b-4b1f-9b51-c57a38e41466)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/dcc200c8-19da-4631-8cdd-40df5696d7b6)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/28ec3b6c-61f5-4e66-868c-7f07ee47954b)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f0c9c0f1-69c1-4b57-99c8-c54fa8497537)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/43ec87d1-ac41-47d0-8a2b-b170d5d8bbed)

<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/48551516-dd43-46dd-b65c-1c535018b932">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2ec4204e-001e-4b17-b605-25811714691b">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/50835de6-07e6-42e8-a2ff-33d98c0873aa">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/629b9df2-7039-49bf-a85f-24b980475196">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4a1219a0-00d4-4682-a40c-cb8b31047757">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ccbd8316-617d-4867-820d-79a295ecc85a">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/88c21cf2-3dd6-460b-8b58-c9123e5c1b2c">

# #END</details>

# #END</details>

<details>
<summary>+Udemy - Django A-Z Build and Deploy Web Project </summary>

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

## Install Django Project from Template

```py
django-admin startproject --template https://github.com/ciur/django-bootstrap-project-template/archive/master.zip my-project
```

## Add AbstractUser for User model

### account.models:

```py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

### hotelview.settings:

```py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'account',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.User'
```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## View Graph of Model relationships

### Install django extensions
  
```py
$ pip install django-extensions==3.1.5
```

### Install pydotplus 

```py
$ pip install pydotplus==2.0.2
```

### Install GraphViz

via [installer](https://graphviz.org/download/) and MANUALLY add it to the user PATH

### Include django_extensions in settings.py:

```py
INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)
```

### Run command:

```py
python manage.py graph_models -a -o hotelview.png
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/69873eb0-5645-46d5-bbb7-440f0db592c8)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/3d188ac8-e2ae-4c89-9d4c-721f75838899)

## How to configure User when Migrations have already been done

[https://youtu.be/EudKs1HPUfE?si=OWnRWdaf478UsHxg](https://youtu.be/EudKs1HPUfE?si=OWnRWdaf478UsHxg)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/6ac1b4de-da34-4dd8-9555-c93e3a659578)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/62bfc48a-d626-438c-a111-390d4f317722)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b95d3955-9df6-4d0d-98ef-c4f00b6abc16)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/3b44c97a-30b0-4ee8-929c-9a74bc8249d1)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c7b95ac1-217f-4015-8035-8e3877377e8c)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/db8d5329-388f-4297-9077-26c5e00b3a09)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/6c136abd-131f-43c5-a58a-33b74238eb68)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/d6bd08fc-d5e0-4be3-946a-5e258a36418d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/66144a42-2a19-4771-82c0-ca6ce36725f9)

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

# How to add custom fields to the User Model 

[https://youtu.be/kRJpQxi2jIo?si=m8p5MTXKtYd98mpn](https://youtu.be/kRJpQxi2jIo?si=m8p5MTXKtYd98mpn)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/df4b11a2-c3c8-4773-a47f-89643ee27fcb)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/094ae27a-60fc-4c1d-b7c9-9020cbf9d8d3)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e1785752-1a93-450e-add8-f7e1710d2a40)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/15fe9d7d-3779-4e8b-ae6e-805870a6ff1a)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/10b489ca-6f3b-415e-ac24-c2619e0d5fe7)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c8ed99a3-d196-4063-b2ab-8682c74b66e2)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7e3ae82b-2815-4b87-9a63-70b9a41741af)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b4120e85-ce85-4b43-a32d-c9f0f917bfd4)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1ae9c5aa-53fe-413e-975c-a4f1bb9b1111)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/d8163172-f64e-4ac1-a248-fedf541cf3b9)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/85f2587b-42cd-40a3-8a5a-51955bfd7be7)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/769cd5ee-ecca-4534-bf2e-ae0ffb6d98d8)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/6071f30f-6a24-4188-a093-16e9be0cf61f)

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
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Bootstrap demo</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

## Navbar Template

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
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
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />

    <title>Todo List - Taskmate</title>
  </head>

  <body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
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
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
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
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />

    <title>Todo List Manager - {% block title %}{% endblock title %}</title>
  </head>

  <body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Task Mate</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="{% url 'todolist' %}"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
              {% comment %} <a class="nav-link" href="/task">Todo List</a> {%
              endcomment %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'about' %}">About Us</a>
              {% comment %}
              <a class="nav-link" href="/task/about">About Us</a> {% endcomment
              %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
              {% comment %}
              <a class="nav-link" href="/task/contact">Contact Us</a> {%
              endcomment %}
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <main class="container">
      <h1>Taskmate</h1>
      {% block content %} {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/about.html:

```html
{% extends "todolist/base.html" %} {% block title %} About Us {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/contact.html:

```html
{% extends "todolist/base.html" %} {% block title %} Contact Us {% endblock
title %} {% block content %}
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

<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />

    <title>Todo List Manager - {% block title %}{% endblock title %}</title>
  </head>

  <body>
    <nav class="navbar navbar-expand-lg bg-body-dark navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'todolist' %}"
          ><img
            src="{% static 'todolist/images/logo-1.png' %}"
            alt="Taskmate Logo"
        /></a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="{% url 'todolist' %}"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
              {% comment %} <a class="nav-link" href="/task">Todo List</a> {%
              endcomment %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'about' %}">About Us</a>
              {% comment %}
              <a class="nav-link" href="/task/about">About Us</a> {% endcomment
              %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
              {% comment %}
              <a class="nav-link" href="/task/contact">Contact Us</a> {%
              endcomment %}
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <main class="container">
      <h1>Taskmate</h1>
      {% block content %} {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
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
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

{% comment %}
<table class="table table-dark table-striped">
  {% endcomment %}
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
      {% for todo in tasks %} {% if todo.done %}
      <tr class="table-success">
        <th scope="row">{{ todo.task }}</th>
        <td>YES</td>
        <td>
          <a href="" type="button" class="btn btn-warning btn-sm">Edit</a>
        </td>
        <td>
          <a href="" type="button" class="btn btn-danger btn-sm">Delete</a>
        </td>
      </tr>
      {% else %}
      <tr>
        <th scope="row">{{ todo.task }}</th>
        <td>NO</td>
        <td>
          <a href="" type="button" class="btn btn-warning btn-sm">Edit</a>
        </td>
        <td>
          <a href="" type="button" class="btn btn-danger btn-sm">Delete</a>
        </td>
      </tr>
      {% endif %} {% endfor %}
    </tbody>
  </table>

  {% for todo in tasks %}
  <div class="todo">
    <h3>{{ todo.task }} - {{ todo.done }}</h3>
  </div>

  {% endfor %} {% endblock content %}
</table>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/02124501-e51e-44a8-9433-e90626c05762)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1eec6917-7f8f-4ef9-8c26-b6f16b130988)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a04a4aed-1075-4144-b7e2-db3cb0cc7cbb)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/db8b9ea7-1016-44a0-8550-646e391acd3c)

<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9c32960b-e69b-4f62-8313-e599cb6771b5">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5049d062-2360-44a7-a134-414b3d9c14b5">

# #END</details>

<details>
<summary>11. Using Django Forms to Create Tasks </summary>

# Using Django Forms to Create Tasks

[https://getbootstrap.com/docs/5.3/forms/overview/](https://getbootstrap.com/docs/5.3/forms/overview/)

## Bootstrap Form Format:

```html
<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input
      type="email"
      class="form-control"
      id="exampleInputEmail1"
      aria-describedby="emailHelp"
    />
    <div id="emailHelp" class="form-text">
      We'll never share your email with anyone else.
    </div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" />
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1" />
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

### todolist.forms:

```py
from django import forms
from .models import TaskList


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    note = None
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
        note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
        "note": note
    }
    return render(request, 'todolist.html', context)
    # return redirect('todolist')


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
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="my-3">
  {% csrf_token %} {% if note %}
  <div class="alert alert-success" role="alert">{{ note }}</div>
  {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

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
    {% for todo in tasks %} {% if todo.done %}
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
    {% endif %} {% endfor %}
  </tbody>
</table>

{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8afc0f90-f618-4ac8-aefc-478857e50dbe)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/5d8b4547-5156-43c1-ada2-84d89ea33cdb)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a0ac350c-628a-4532-bc46-21c48f266abc)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/115ac876-d1e4-40bd-915b-d9b7ffa680a5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/43c0a4c2-fc8d-4320-b49f-407036a94eba)

<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/57c4415d-d405-448e-9bb8-983c30dc37ca">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/def193eb-d990-4848-90eb-41cf3b3820bb">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2095b37c-9c3b-413b-a050-8f9b306bcdfe">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/57649b4d-8987-42f7-ab9f-18077b67601b">

# #END</details>

<details>
<summary>12. Using Django Messages for Alert </summary>

# Using Django Messages for Alert

[https://github.com/omeatai/src-python-flask-django/commit/f7595ceae38ddf8f9d4557b33d9dd1385b1d75b4](https://github.com/omeatai/src-python-flask-django/commit/f7595ceae38ddf8f9d4557b33d9dd1385b1d75b4)
[https://getbootstrap.com/docs/5.3/components/alerts/](https://getbootstrap.com/docs/5.3/components/alerts/)

## Bootstrap Alert Formats:

```html
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
<div class="alert alert-secondary" role="alert">
  A simple secondary alert—check it out!
</div>
<div class="alert alert-success" role="alert">
  A simple success alert—check it out!
</div>
<div class="alert alert-danger" role="alert">
  A simple danger alert—check it out!
</div>
<div class="alert alert-warning" role="alert">
  A simple warning alert—check it out!
</div>
<div class="alert alert-info" role="alert">
  A simple info alert—check it out!
</div>
<div class="alert alert-light" role="alert">
  A simple light alert—check it out!
</div>
<div class="alert alert-dark" role="alert">
  A simple dark alert—check it out!
</div>
```

```html
<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <strong>Holy guacamole!</strong> You should check in on some of those fields
  below.
  <button
    type="button"
    class="btn-close"
    data-bs-dismiss="alert"
    aria-label="Close"
  ></button>
</div>
```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        # note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
    }
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
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

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
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
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
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/517a9dd3-823e-4dc7-8e85-fd193c699f63)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/60adead8-b2cd-4e83-b129-b5298b2456f7)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/161b66c4-e1d9-44b2-8990-a23df0dc86ae)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/2d72e0aa-bc86-4224-86ca-32689a5c77d5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/75d1697b-d560-48e8-901f-eebc11d6324c)

<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b0974a5c-390b-4a5b-a2c6-644c8b35ef1b">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4cb1326a-a41b-45cd-b6b3-486e82eaffed">

# #END</details>

<details>
<summary>13. Delete Tasks </summary>

# Delete Tasks

[https://github.com/omeatai/src-python-flask-django/commit/9eb57b3f196c9a625b1883007a9d963ca70b3d03](https://github.com/omeatai/src-python-flask-django/commit/9eb57b3f196c9a625b1883007a9d963ca70b3d03)

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
]

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        # note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
    }
    return render(request, 'todolist.html', context)


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


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```py
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
    {% csrf_token %}

    {% if messages %}

    {% for message in messages %}
    {% comment %} <div class="alert alert-success" role="alert">
        {{ message }}
    </div> {% endcomment %}

    <div class="alert alert-success alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>

    {% endfor %}

    {% endif %}

    <div class="mb-3">
        <label for="task" class="form-label">Add Task</label>
        <input type="text" class="form-control" id="task" name="task" aria-describedby="textHelp"
            placeholder="Call Alex...">
        <div id="textHelp" class="form-text">What would you want to do?</div>
    </div>
    <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>


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
        {% if tasks %}

        {% for todo in tasks %}

        {% if todo.done %}
        <tr class="table-success">
            <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
            <td>YES</td>
            <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
            <td><a href="{% url 'delete-task' todo.id %}" type="button" class="btn btn-danger btn-sm">Delete</a></td>
        </tr>
        {% else %}
        <tr>
            <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
            <td>NO</td>
            <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
            <td><a href="{% url 'delete-task' todo.id %}" type="button" class="btn btn-danger btn-sm">Delete</a></td>
        </tr>
        {% endif %}

        {% endfor %}

        {% endif %}
    </tbody>
</table>


{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/d8037a7b-5c93-4ae2-81b0-2fb983c5289b)

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a1daed4b-7fd1-4b94-86fd-d227b4e87a3a">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3bddcff2-4dc8-4606-a86c-b07ea8221247">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/878de8d9-5022-4a11-b3fb-9e270bfb9849">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/97d438f0-911b-4b71-9f50-d7d7d8291660">

# #END</details>

<details>
<summary>14. Edit Tasks </summary>

# Edit Tasks

[https://github.com/omeatai/src-python-flask-django/commit/5b431c4a4c4af67bd8b0ed70c091670358ab47be](https://github.com/omeatai/src-python-flask-django/commit/5b431c4a4c4af67bd8b0ed70c091670358ab47be)

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
]

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        # note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
    }
    return render(request, 'todolist.html', context)


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


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/edit.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Edit Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      value="{{ task.task }}"
      aria-describedby="textHelp"
      placeholder="{{ task.task }}"
    />
    <div id="textHelp" class="form-text">Make your changes</div>
  </div>
  <div class="mb-3">
    {% comment %} <input type="hidden" name="done" value="{{ task.done }}" /> {%
    endcomment %}

    <label for="done" class="form-label">Is it Done?</label>
    <select
      class="form-select"
      id="done"
      name="done"
      aria-label="Default select example"
    >
      <option value="False" {% if not task.done %} selected {% endif %}>
        NO
      </option>
      <option value="True" {% if task.done %} selected {% endif %}>YES</option>
    </select>
  </div>
  <button type="submit" class="btn btn-primary my-2">Update TASK</button>
  <a href="{% url 'todolist' %}" class="btn btn-danger my-2">Back</a>
</form>

{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

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
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success">
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>YES</td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% else %}
    <tr>
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>NO</td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f1916e5e-8010-43b6-a546-712b9d8b92f2)
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/71fea5e5-ad70-4a76-bd3c-b3a89f3addd8">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/55525c60-ff7b-45f0-8b6e-c914293905d9">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b87be038-0546-4ba7-9ca8-b08b3f0d7ac5">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1017bfaf-45dd-4cad-a5c6-97386b55a1c2">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bc47c73b-882f-4beb-b4dc-738f1032a1ff">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0f814752-599a-481d-8cfa-523f465d373a">

# #END</details>

<details>
<summary>15. Mark Tasks as Completed or Pending </summary>

# Mark Tasks as Completed or Pending

[https://github.com/omeatai/src-python-flask-django/commit/5b431c4a4c4af67bd8b0ed70c091670358ab47be](https://github.com/omeatai/src-python-flask-django/commit/5b431c4a4c4af67bd8b0ed70c091670358ab47be)

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('pending/<int:id>', views.pending, name="pending"),
]

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        # note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
    }
    return render(request, 'todolist.html', context)


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
    return redirect('todolist')


def pending(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = False
    task.save()
    return redirect('todolist')


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


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

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
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success">
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>
        <a
          href="{% url 'pending' todo.id %}"
          type="button"
          class="btn btn-success btn-sm"
          >YES - Mark as Pending</a
        >
      </td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% else %}
    <tr>
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>
        <a
          href="{% url 'completed' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >NO - Mark as Completed</a
        >
      </td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

{% endblock content %}
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a9253b7e-bee3-4fe4-9edd-0430a610fda7">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4b87c611-dde2-4111-ab00-b73fdf9d8d48">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/960dc91d-0e91-4be1-ade4-8fcab1eef1f6">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5e982354-79e9-48d9-bf99-64edba4b4e5a">

# #END</details>

<details>
<summary>16. Using Django Pagination </summary>

# Using Django Pagination

[https://github.com/omeatai/src-python-flask-django/commit/6717a9bee64a99ecffe19d9d989a2e6bdb4fd416](https://github.com/omeatai/src-python-flask-django/commit/6717a9bee64a99ecffe19d9d989a2e6bdb4fd416)

## Pagination Format

```html
<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    <li class="page-item disabled">
      <a class="page-link">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('pending/<int:id>', views.pending, name="pending"),
]

```

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

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.task} - {self.done}"

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlparse, parse_qs

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        res = redirect('todolist')
    else:
        tasks = TaskList.objects.all()
        no_per_pages = 5
        paginator = Paginator(tasks, no_per_pages)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)

        context = {
            'tasks': tasks,
            "welcome_text": "Welcome to your Todo List!",
        }
        return render(request, 'todolist.html', context)


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


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

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
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success">
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>
        <a
          href="{% url 'pending' todo.id %}"
          type="button"
          class="btn btn-success btn-sm"
          >YES - Mark as Pending</a
        >
      </td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% else %}
    <tr>
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>
        <a
          href="{% url 'completed' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >NO - Mark as Completed</a
        >
      </td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    {% comment %} {% for i in tasks.paginator.page_range %}{% endfor %}{%
    endcomment %}

    <li class="page-item {% if not tasks.has_previous %} disabled {% endif %}">
      <a class="page-link" href="?pg=1">First</a>
    </li>

    {% if tasks.has_previous %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}"
        >Previous</a
      >
    </li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}"
        >{{ tasks.previous_page_number }}</a
      >
    </li>
    {% endif %}

    <li class="page-item active">
      <a class="page-link" href="#">{{ tasks.number }}</a>
    </li>

    {% if tasks.has_next %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}"
        >{{ tasks.next_page_number }}</a
      >
    </li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}">Next</a>
    </li>
    {% endif %}

    <li class="page-item {% if not tasks.has_next %} disabled {% endif %}">
      <a class="page-link" href="?pg={{ tasks.paginator.num_pages }}">Last</a>
    </li>
  </ul>
</nav>

{% endblock content %}
```

<img width="1402" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5a62d9d0-6e6b-4509-87d4-d4bfeb500217">
<img width="1402" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b5c017a0-5974-413b-a6ac-15f1dd07df98">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1d8410b8-083c-495e-a65d-26582710f04c)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/90aadddc-6dbf-48fb-882b-890072028d17)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/93840e33-4778-4816-a3ff-fd404fcccf26)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c14ad119-bd1e-4b0d-8200-8c2da8f3a62f)

<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f8be2323-0489-4681-908a-686338658626">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e7c4b243-8f57-42e7-8507-9a88f11b9813">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/349b9cad-191e-4cff-b614-e0e517736faa">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ce1ac473-c04d-4305-811d-cbd88dfb01c4">

# #END</details>

<details>
<summary>17. Setup HomePage </summary>

# Setup HomePage

[https://github.com/omeatai/src-python-flask-django/commit/cccec3cbe9d4a96abbbc1ed9d9ddb682938063a1](https://github.com/omeatai/src-python-flask-django/commit/cccec3cbe9d4a96abbbc1ed9d9ddb682938063a1)

[https://unsplash.com/s/photos/notes](https://unsplash.com/s/photos/notes)

### taskmate.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
]

```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home, name="home"),
    path('todolist/', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('pending/<int:id>', views.pending, name="pending"),
]

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlparse, parse_qs

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def home(request):
    context = {
        "welcome_text": "Welcome to the Home Page!"
    }
    return render(request, 'home.html', context)


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        res = redirect('todolist')
    else:
        tasks = TaskList.objects.all()
        no_per_pages = 5
        paginator = Paginator(tasks, no_per_pages)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)

        context = {
            'tasks': tasks,
            "welcome_text": "Welcome to your Todo List!",
        }
        return render(request, 'todolist.html', context)


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


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/templates/todolist/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />
    <link
      rel="icon"
      href="{% static 'todolist/images/favicon.ico' %}"
      type="image/gif"
      sizes="16x16"
    />

    <title>Todo List Manager - {% block title %}{% endblock title %}</title>
  </head>

  <body class="bg-light">
    <nav class="navbar navbar-expand-lg bg-body-dark navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'home' %}"
          ><img
            src="{% static 'todolist/images/logo-1.png' %}"
            alt="Taskmate Logo"
        /></a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="{% url 'home' %}"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
              {% comment %} <a class="nav-link" href="/task">Todo List</a> {%
              endcomment %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'about' %}">About Us</a>
              {% comment %}
              <a class="nav-link" href="/task/about">About Us</a> {% endcomment
              %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
              {% comment %}
              <a class="nav-link" href="/task/contact">Contact Us</a> {%
              endcomment %}
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <main class="container">
      <h1>Taskmate</h1>
      {% block content %} {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### src-python/udemy/django-A-Z/todolist/templates/home.html:

```html
{% extends "todolist/base.html" %}
{% load static %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>

<div class="text-center">
  <div class="row mt-5">
    <div class="col-lg-4">
      <img src="{% static 'todolist/images/stickynotes-1.jpg' %}" alt='stickynotes' width="360" height="250" class="rounded-lg shadow-lg"></img>
    </div>
    <div class="col-lg-4">
      <img src="{% static 'todolist/images/stickynotes-2.jpg' %}" alt='stickynotes' width="360" height="250" class="rounded-lg shadow-lg"></img>
    </div>
    <div class="col-lg-4">
      <img src="{% static 'todolist/images/stickynotes-3.jpg' %}" alt='stickynotes' width="360" height="250" class="rounded-lg shadow-lg"></img>
    </div>
  </div>

  <div class="row mt-5">
    <div class="col-md-10 offset-md-1">
        <p class="h1 text-success">Quick And Easy To Use, Anytime, Anywhere!</p>
        <p class="h2 mt-3">"Plan Your Day Better, Get Your Life Organized"</p>
        <p class="h5">TASKMATE Lets You Keep Track Of Your Task In One Place.</p>
        <a href="{% url 'todolist' %}" type="button" class="btn btn-primary btn-lg mt-3 shadow-lg">Let's Get Started!</a>
    </div>
  </div>
</div>

{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

<table
  class="table table-light table-striped table-hover table-bordered text-center"
>
  <thead>
    <tr class="table-dark row">
      <th class="col-7">Task</th>
      <th class="col-3">Done</th>
      <th class="col-1">Edit</th>
      <th class="col-1">Delete</th>
    </tr>
  </thead>
  <tbody>
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success row">
      <th class="col-7">{{ todo.task }}</th>
      <td class="col-3">
        <a
          href="{% url 'pending' todo.id %}"
          type="button"
          class="btn btn-success btn-sm"
          >YES - Mark as Pending</a
        >
      </td>
      <td class="col-1">
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning"
          >Edit</a
        >
      </td>
      <td class="col-1">
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger"
          >Delete</a
        >
      </td>
    </tr>
    {% else %}
    <tr class="row">
      <th class="col-7">{{ todo.task }}</th>
      <td class="col-3">
        <a
          href="{% url 'completed' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >NO - Mark as Completed</a
        >
      </td>
      <td class="col-1">
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning"
          >Edit</a
        >
      </td>
      <td class="col-1">
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger"
          >Delete</a
        >
      </td>
    </tr>
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    {% comment %} {% for i in tasks.paginator.page_range %}{% endfor %}{%
    endcomment %}

    <li class="page-item {% if not tasks.has_previous %} disabled {% endif %}">
      <a class="page-link" href="?pg=1">First</a>
    </li>

    {% if tasks.has_previous %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}"
        >Previous</a
      >
    </li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}"
        >{{ tasks.previous_page_number }}</a
      >
    </li>
    {% endif %}

    <li class="page-item active">
      <a class="page-link" href="#">{{ tasks.number }}</a>
    </li>

    {% if tasks.has_next %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}"
        >{{ tasks.next_page_number }}</a
      >
    </li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}">Next</a>
    </li>
    {% endif %}

    <li class="page-item {% if not tasks.has_next %} disabled {% endif %}">
      <a class="page-link" href="?pg={{ tasks.paginator.num_pages }}">Last</a>
    </li>
  </ul>
</nav>

{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/cf3f7b77-2f22-4de4-bb9f-18b99cf26757)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/492e8aa7-c89c-4922-9a86-55f4a4e8cad5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a5d38adc-26d3-471d-8d1e-c8368bd07169)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/91d6e012-3c45-4808-a78b-df57f7406007)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/2433351e-2e6e-4b7d-996f-cdc6bfe500de)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/10ae459e-a070-4b31-95c0-83fc1e1ea562)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/36c29504-0069-4311-9103-3f7ea2f94748)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/58096026-7c9a-4087-9310-70419bd8bf87)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/14ce4007-3c1e-49f4-b2b9-639c9af4033d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/516d72c5-c66d-44f2-b5e2-46f31f484537)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8c5756d5-d482-4511-a4b0-6e25d3687113)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ddcf4e06-07d1-4f1a-a9e6-110e6a106a5d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/628c02f1-4e54-40b5-9e90-7176f133cfb5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/138600da-b0ad-4708-9c39-a163a9223ab5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/dabb6bb7-d14e-407b-b915-f5465510c62e)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/5d7399a9-d188-4f74-b2f0-f0d7af03210f)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/bc09af4c-f39d-454a-bff4-3212121f512a)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e355e3f0-1038-4dbd-8e68-347c0a99a544)

<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ec865bef-7c88-4720-9ea8-52f5b9b18ca2">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5b350bda-4be3-424b-a10e-d3e1d4cd5b66">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/89c12ac8-a650-4132-8124-db2470f2b637">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7aefe9c3-c94c-4e5a-8bda-aac412a3f9f6">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/74ebaebc-4d46-4f50-b5c2-0f7637280f67">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/25cb6276-4c08-4594-a3ec-b3c0d9d0e36b">

# #END</details>

<details>
<summary>18. Setup User Authentication App </summary>

# Setup User Authentication App

[https://github.com/omeatai/src-python-flask-django/commit/071b0e57d5f1903d870b67c2bec349bef8770c9b](https://github.com/omeatai/src-python-flask-django/commit/071b0e57d5f1903d870b67c2bec349bef8770c9b)

### Create User App

```py
python manage.py startapp user_auth
```

### taskmate.settings:

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
    'todolist',
    'user_auth',
]
```

### taskmate.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
    path('account/', include('user_auth.urls')),
]
```

### user_auth.urls:

```py
from django.urls import path
from user_auth import views

urlpatterns = [
    path('register/', views.register, name="register"),

    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
    # path('profile/', views.profile, name="profile"),
    # path('edit-profile/', views.edit_profile, name="edit-profile"),
    # path('change-password/', views.change_password, name="change-password"),
    # path('reset-password/', views.reset_password, name="reset-password"),
    # path('reset-password-done/', views.reset_password_done, name="reset-password-done"),
    # path('reset-password-confirm/<uidb64>/<token>/', views.reset_password_confirm, name="reset-password-confirm"),
    # path('reset-password-complete/', views.reset_password_complete, name="reset-password-complete"),
    # path('delete-account/', views.delete_account, name="delete-account"),
]

```

### user_auth.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def register(request):
    return HttpResponse("<h1>User registration Page is working!</h1>")
    # return render(request, 'register.html', {})

```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e4a251f1-43e0-4416-a791-862ec83beed2)

<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/46946c8a-2738-4526-9e41-e07251234608">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e906c58e-310f-44da-81ad-9a085d9e6ce6">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/90398f9e-5c4c-4898-9910-aae10b343f05">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3bc0762d-c8f6-483e-a7ab-4f5769133b0b">

# #END</details>

<details>
<summary>19. Setup Registration userCreationForm, Views and Template with Errors and Messages </summary>

# Setup Registration userCreationForm, Views and Template with Errors and Messages

[https://github.com/omeatai/src-python-flask-django/commit/a9d6c021a3d5cf2bdf7591043b5b21dcfc894940](https://github.com/omeatai/src-python-flask-django/commit/a9d6c021a3d5cf2bdf7591043b5b21dcfc894940)

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = UserCreationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/register.html:

```html
{% extends "todolist/base.html" %} {% block title %} Sign Up - Taskmate {%
endblock title %} {% block content %}

<div>
  <form action="" method="POST" class="form-group my-3">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert {% if message.tags == 'error' %} alert-danger {% elif message.tags == 'success' %} alert-success {% else %} alert-warning {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %}

    <hr />

    {% if register_form.errors %} {% for field in register_form %} {{
    field.errors }} {% endfor %} {% endif %}

    <hr />

    {% if register_form.errors %} {% for field in register_form %} {% for error
    in field.errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endfor %} {% endif %}

    <hr />

    {% if register_form.non_field_errors %} {% for error in
    register_form.non_field_errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endif %}

    <hr />

    {{ register_form.as_p}}

    <button type="submit" class="btn btn-primary">Sign Up</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8a3212cc-4284-461c-bd13-3e334a1a281d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/56eef428-a699-4462-bc72-ad15a5e5768d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b3866b11-26b3-4403-9488-cf4c9466e712)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7462171d-5d6c-4f08-abb5-e5162463312a)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/0a1aacd4-81bb-496a-b194-b05c79763967)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/79beffcf-e612-4499-a038-04f8270d7095)

# #END</details>

<details>
<summary>20. Add Email Field to Form with forms.py </summary>

# Add Email Field to Form with forms.py

[https://github.com/omeatai/src-python-flask-django/commit/d3c63eda49bdb6f0cfd92c935930d850010d4126](https://github.com/omeatai/src-python-flask-django/commit/d3c63eda49bdb6f0cfd92c935930d850010d4126)

### user_auth.forms:

```py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

```

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CustomRegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = CustomRegistrationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/register.html:

```html
{% extends "todolist/base.html" %} {% block title %} Sign Up - Taskmate {%
endblock title %} {% block content %}

<div>
  <form action="" method="POST" class="form-group my-3">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %} {% if register_form.errors %} {% for field in
    register_form %} {% for error in field.errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endfor %} {% endif %} {{ register_form.as_p}}

    <button type="submit" class="btn btn-primary">Sign Up</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f0fef2cd-8bf0-42fb-bf1b-80032ff682d9)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c1253e16-e4be-463a-b4f7-a74f942de281)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/2f237133-d42c-471e-bc56-181b8c631fa1)

<img width="1377" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/908fed7d-8b70-4886-ac79-027087017e59">
<img width="1377" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/124d7dd2-bca9-4523-83bc-0886f7386f31">
<img width="1377" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d73fb41c-6967-4489-908b-902721ad6181">

# #END</details>

<details>
<summary>21. Redesign the Register Page with Crispy Forms </summary>

# Redesign the Register Page with Crispy Forms

[https://github.com/omeatai/src-python-flask-django/commit/9ea3288a858fe8e5a453b400794e894cfe16a213](https://github.com/omeatai/src-python-flask-django/commit/9ea3288a858fe8e5a453b400794e894cfe16a213)

## Install Crispy Forms

```x
pip install crispy-bootstrap5
```

### taskmate.settings:

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
    'todolist',
    'user_auth',
    'crispy_forms',
    'crispy_bootstrap5',
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/register.html:

```html
{% extends "todolist/base.html" %} {% load crispy_forms_tags %} {% block title
%} Sign Up - Taskmate {% endblock title %} {% block content %}

<div>
  <h2>Sign Up</h2>
  <form action="" method="POST" class="form-group my-3 col-6">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %} {% if register_form.errors %} {% for field in
    register_form %} {% for error in field.errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endfor %} {% endif %} {{ register_form|crispy }}

    <button type="submit" class="btn btn-primary">Sign Up</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/92e7f747-7986-4410-af6d-95c8e83a4527)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f19ad3d6-4d0c-49e8-a619-bdfecff9c029)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f488d0f0-1734-44bd-b8de-fba7e47134b9)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/dba5eccb-5065-48d8-a0b5-69e3a4ed0096)

<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b4ac9c23-ae6e-4cb9-9e26-79513d47fece">
<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/36e9fbc4-35c1-4e66-bdf0-6a41ace252d7">

# #END</details>

<details>
<summary>22. Login Functionality </summary>

# Login Functionality

[https://github.com/omeatai/src-python-flask-django/commit/6cd6828e1377c2306776d47d8f21e5c13b3dd1a8](https://github.com/omeatai/src-python-flask-django/commit/6cd6828e1377c2306776d47d8f21e5c13b3dd1a8)

### taskmate.settings:

```py
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

LOGIN_REDIRECT_URL = 'todolist'
```

### user_auth.urls:

```py
from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name="login"),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
    # path('profile/', views.profile, name="profile"),
    # path('edit-profile/', views.edit_profile, name="edit-profile"),
    # path('change-password/', views.change_password, name="change-password"),
    # path('reset-password/', views.reset_password, name="reset-password"),
    # path('reset-password-done/', views.reset_password_done, name="reset-password-done"),
    # path('reset-password-confirm/<uidb64>/<token>/', views.reset_password_confirm, name="reset-password-confirm"),
    # path('reset-password-complete/', views.reset_password_complete, name="reset-password-complete"),
    # path('delete-account/', views.delete_account, name="delete-account"),
]

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/login.html:

```html
{% extends "todolist/base.html" %} {% load crispy_forms_tags %} {% block title
%} Sign In - Taskmate {% endblock title %} {% block content %}

<div>
  <h2>Sign In</h2>
  <form action="" method="POST" class="form-group my-3 col-6">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %} {% if register_form.errors %} {% for field in
    register_form %} {% for error in field.errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endfor %} {% endif %} {{ form|crispy }}

    <button type="submit" class="btn btn-primary">Sign In</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ced09a03-fb3d-4c64-b01a-bbfb1df602d9)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f6421499-d2da-45e5-acc6-7e1ca124b53c)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1d4896ff-b121-43ac-8f40-d5044f27fc5a)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b278fdfa-68b0-47d6-b4e2-fac4b2d5e95b)

<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/023f6b2d-e771-438b-bb2d-9d06cb1b1b79">
<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/851925dd-fa3a-4743-b7ac-473c0eaea69a">
<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1acc64db-a3df-477c-bfc3-e7561f93b6c7">

# #END</details>

<details>
<summary>23. Logout Functionality and Username in Navbar </summary>

# Logout Functionality and Username in Navbar

[https://github.com/omeatai/src-python-flask-django/commit/a8686d606c7ce2e0a6a988dd3e345b8ccd2be50a](https://github.com/omeatai/src-python-flask-django/commit/a8686d606c7ce2e0a6a988dd3e345b8ccd2be50a)

### user_auth.urls:

```py
from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name="login"),
    path('logout/', views.logout, name="logout"),

    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
    # path('profile/', views.profile, name="profile"),
    # path('edit-profile/', views.edit_profile, name="edit-profile"),
    # path('change-password/', views.change_password, name="change-password"),
    # path('reset-password/', views.reset_password, name="reset-password"),
    # path('reset-password-done/', views.reset_password_done, name="reset-password-done"),
    # path('reset-password-confirm/<uidb64>/<token>/', views.reset_password_confirm, name="reset-password-confirm"),
    # path('reset-password-complete/', views.reset_password_complete, name="reset-password-complete"),
    # path('delete-account/', views.delete_account, name="delete-account"),
]

```

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.views import LogoutView

from .forms import CustomRegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = CustomRegistrationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})


def logout(request):
    if request.method == 'POST':
        messages.success(
            request, "Awesome! You have been logged out successfully!")
        return LogoutView.as_view(next_page='login')(request)
    else:
        return render(request, 'user_auth/logout.html')


# class UserLogoutView(LogoutView):
#     def get(self, request):
#         logout(request)
#         return redirect('login')

```

### src-python/udemy/django-A-Z/templates/todolist/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />
    <link
      rel="icon"
      href="{% static 'todolist/images/favicon.ico' %}"
      type="image/gif"
      sizes="16x16"
    />

    <title>Todo List Manager - {% block title %}{% endblock title %}</title>
  </head>

  <body class="bg-light">
    <nav class="navbar navbar-dark bg-dark navbar-expand-lg bg-body-dark mb-4">
      <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'home' %}"
          ><img
            src="{% static 'todolist/images/logo-1.png' %}"
            alt="Taskmate Logo"
        /></a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="{% url 'home' %}"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'about' %}">About Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
            </li>
          </ul>
          {% if user.is_authenticated %}
          <div class="d-flex text-secondary mx-2">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Welcome, {{ user.username|title }}
                </a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Profile</a></li>
                  <li><a class="dropdown-item" href="#">Change Password</a></li>
                  <li><hr class="dropdown-divider" /></li>
                  <li><a class="dropdown-item" href="#">Settings</a></li>
                </ul>
              </li>
            </ul>
          </div>
          <div class="d-flex mx-2">
            <a href="{% url 'logout' %}" class="btn btn-danger" type="submit"
              >Logout</a
            >
          </div>
          {% else %}
          <div class="d-flex mx-2">
            <a href="{% url 'login' %}" class="btn btn-success" type="submit"
              >Login</a
            >
          </div>
          <div class="d-flex mx-2">
            <a href="{% url 'register' %}" class="btn btn-primary" type="submit"
              >Register</a
            >
          </div>
          {% endif %}
        </div>
      </div>
    </nav>

    <main class="container">
      <h1>Taskmate</h1>
      {% block content %} {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/logout.html:

```html
{% extends "todolist/base.html" %} {% block title %} Logged Out - Taskmate {%
endblock title %} {% block content %}

<div>
  <form action="{% url 'logout' %}" method="POST" class="form-group my-3 col-6">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %}

    <h2 class="text-secondary">Sure you want to Logout of Taskmate?</h2>

    <button type="submit" class="btn btn-danger">Logout</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7c7e0b1a-a083-4019-8037-6b79ef1f1eac)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/170123a2-d524-4809-ac1a-ce44213feb86)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/3b019d45-f235-4f14-99c3-4b384bf30ba5)

<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ceaaf8c7-f786-4154-bfc1-f48615ebda56">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/67be9e97-ef33-4f58-875c-3e11781e19ce">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6b6ce0ff-9357-4e0b-92bb-4608e2ff7955">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/43f565e8-c61e-436f-8b5a-ec4278959f3a">

# #END</details>

<details>
<summary>24. Login Manually with authenticate and login </summary>

# Login Manually with authenticate and login

[https://github.com/omeatai/src-python-flask-django/commit/783ee1680b9f55b5b86f5ee8eab2d787531046fc](https://github.com/omeatai/src-python-flask-django/commit/783ee1680b9f55b5b86f5ee8eab2d787531046fc)

## Logic for Creating users

```py
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
>>> user.last_name = "Lennon"
>>> user.save()
```

## Command for creating SuperUser from Prompt

```py
python manage.py createsuperuser --username=joe --email=joe@example.com
```

## Logic for changing Passwords

```py
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username="john")
>>> u.set_password("new password")
>>> u.save()
```

## Logic for Authenticating users manually

```py
from django.contrib.auth import authenticate

user = authenticate(username="john", password="secret")
if user is not None:
    # A backend authenticated the credentials
else:
    # No backend authenticated the credentials
```

```py
from django.contrib.auth import authenticate, login


def my_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        # Return an 'invalid login' error message.
```

### user_auth.urls:

```py
from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    # path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name="login"),
    path('login/', views.auth_login, name="login"),
    path('logout/', views.logout, name="logout"),

    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
    # path('profile/', views.profile, name="profile"),
    # path('edit-profile/', views.edit_profile, name="edit-profile"),
    # path('change-password/', views.change_password, name="change-password"),
    # path('reset-password/', views.reset_password, name="reset-password"),
    # path('reset-password-done/', views.reset_password_done, name="reset-password-done"),
    # path('reset-password-confirm/<uidb64>/<token>/', views.reset_password_confirm, name="reset-password-confirm"),
    # path('reset-password-complete/', views.reset_password_complete, name="reset-password-complete"),
    # path('delete-account/', views.delete_account, name="delete-account"),
]

```

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views import View
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, logout, login

from .forms import CustomRegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = CustomRegistrationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST["username"]
        # password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist')
        else:
            messages.error(
                request, "Sorry! Your credentials could not be validated. Please try again.")
            return redirect('login')
    else:
        return render(request, 'user_auth/login_manual.html')


def logout(request):
    if request.method == 'POST':
        messages.success(
            request, "Awesome! You have been logged out successfully!")
        return LogoutView.as_view(next_page='login')(request)
    else:
        return render(request, 'user_auth/logout.html')


# class UserLogoutView(LogoutView):
#     def get(self, request):
#         logout(request)
#         return redirect('login')

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/login_manual.html:

```py
{% extends "todolist/base.html" %}
{% load crispy_forms_tags %}

{% block title %}
Sign In - Taskmate
{% endblock title %}

{% block content %}

<div>
    <h2>Sign In</h2>
    <form action="{% url 'login' %}" method="POST" class="form-group my-3 col-6">
        {% csrf_token %}

        {% if messages %}
        {% for message in messages %}

        <div class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
        role="alert">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>

        {% endfor %}
        {% endif %}

        {% if register_form.errors %}
        {% for field in register_form %}
            {% for error in field.errors %}
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                {{ error|escape }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            {% endfor %}
        {% endfor %}
        {% endif %}

        <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter your username">
        </div>
        <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Enter your password">
        </div>

        <button type="submit" class="btn btn-primary">Sign In</button>
    </form>
</div>
{% endblock content %}
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5f48f582-9988-4d85-af9d-3e8632159d81">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d5255ec2-66eb-4741-8ef6-019891312111">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b0518f62-982c-4d1a-aff3-bfd6790f9b78">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7df9b66e-1e73-420b-a772-d14c3adf2ccb">

<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c3a052d9-b46a-43f4-9217-d4ce5f2f6c73">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c626753a-c0b9-4492-bbd5-d57783bd52ba">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1cd66482-7585-4ce3-8456-13ff487e89b1">

# #END</details>

<details>
<summary>25. Logout Manually with logout </summary>

# Logout Manually with logout

[https://github.com/omeatai/src-python-flask-django/commit/96a65ce7e583625918360741f65d6262c5bcec7e](https://github.com/omeatai/src-python-flask-django/commit/96a65ce7e583625918360741f65d6262c5bcec7e)

## Logic to Logout user

```py
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    # Redirect to a success page.
```

### user_auth.urls:

```py
from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    # path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name="login"),
    path('login/', views.auth_login, name="login"),
    path('logout/', views.auth_logout, name="logout"),
]

```

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views import View
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, logout, login

from .forms import CustomRegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = CustomRegistrationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST["username"]
        # password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist')
        else:
            messages.error(
                request, "Sorry! Your credentials could not be validated. Please try again.")
            return redirect('login')
    else:
        return render(request, 'user_auth/login_manual.html')


def auth_logout(request):
    if request.method == 'POST':
        messages.success(
            request, "Awesome! You have been logged out successfully!")
        logout(request)
        return redirect('login')
    else:
        return render(request, 'user_auth/logout.html')


# def logout(request):
#     if request.method == 'POST':
#         messages.success(
#             request, "Awesome! You have been logged out successfully!")
#         return LogoutView.as_view(next_page='login')(request)
#     else:
#         return render(request, 'user_auth/logout.html')

# class UserLogoutView(LogoutView):
#     def get(self, request):
#         logout(request)
#         return redirect('login')

```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/917adbcb-da8c-414c-8600-558eab84afa6)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/875647ac-661f-447d-be16-426b87d56378)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b32b8e06-94cb-429a-bf27-673815b9bef6)

<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f51cb95d-5d8c-47db-8e2e-682c68024aaf">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9c1512bc-b101-4fc4-9777-341b9fb7050b">

# #END</details>

<details>
<summary>26. Auth Page Restrictions </summary>

# Auth Page Restrictions

[https://github.com/omeatai/src-python-flask-django/commit/b4056b0987df08efd47c40f81287360628340a9a](https://github.com/omeatai/src-python-flask-django/commit/b4056b0987df08efd47c40f81287360628340a9a)

## Logic for Limiting access to logged-in users

```py
from django.conf import settings
from django.shortcuts import redirect


def my_view(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
```

```py
from django.shortcuts import render


def my_view(request):
    if not request.user.is_authenticated:
        return render(request, "myapp/login_error.html")
```

```py
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='next', login_url='login')
def my_view(request):
    pass
```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home, name="home"),
    path('todolist/', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('pending/<int:id>', views.pending, name="pending"),
]

```

### taskmate.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

LOGIN_REDIRECT_URL = 'todolist'
LOGIN_URL = 'login'

```

### todolist.views:

```py
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
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
            redirect('todolist')
    else:
        tasks = TaskList.objects.all()
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
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5d98a05e-65f7-48c5-ab43-790ee183ddb7">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3f8612c5-453c-406b-8300-8e360cdbe030">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8f604bfb-003e-49c1-bcc0-3826f710a831">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c5d58131-bb38-4d92-a4e0-2c35d6be2193">

# #END</details>

<details>
<summary>27. Relationship between User to Task </summary>

# Relationship between User to Task

[https://github.com/omeatai/src-python-flask-django/commit/1be6a912f9b2beedb658c1d66d0bbba390d02722](https://github.com/omeatai/src-python-flask-django/commit/1be6a912f9b2beedb658c1d66d0bbba390d02722)

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

### todolist.models:

```py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskList(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.task} - {self.done} (by {self.owner})"

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8018cdbb-7c36-4375-abc2-20494ab58204">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c797c459-c6d7-494c-ab1e-0ff1f8ed3e02">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/37615109-bd40-4d9e-8f9f-51c9c0aee3ce">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/be18e020-040f-4347-96d2-d0b8eb8e90f6">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bdc66f6f-fecf-4390-95e8-a069a673b77b">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ae23443a-b580-43d9-b913-55690e852ca6">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f62994e3-8a2f-47ee-b26b-109db254e151">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/11a0c0c9-4990-40be-bf16-bdc2c8ddafc9">

# #END</details>

<details>
<summary>28. Creating Task with User </summary>

# Creating Task with User

[https://github.com/omeatai/src-python-flask-django/commit/04beb8749f460cf1395eeb32366a47e1949cb775](https://github.com/omeatai/src-python-flask-django/commit/04beb8749f460cf1395eeb32366a47e1949cb775)

### todolist.views:

```py
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
        tasks = TaskList.objects.all()
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

```

### todolist.models:

```py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskList(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.task} - {self.done} (by {self.owner})"

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0258fa19-5d19-4dc4-8d88-0b1eac716fde">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9da45c4f-1564-4410-ac51-4dd4efbfdc62">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a01cfe23-14f6-452a-a49e-48df7a0d2984">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bdfd047b-67eb-4876-a868-45c45cb9169a">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1fa1e8c3-3858-46a9-91d5-9553d424254c">

# #END</details>

<details>
<summary>29. Showing Task of Logged-In User only </summary>

# Showing Task of Logged-In User only

[https://github.com/omeatai/src-python-flask-django/commit/484dbe8a3eb8f7d1657c71ad04e5337318e4bb83](https://github.com/omeatai/src-python-flask-django/commit/484dbe8a3eb8f7d1657c71ad04e5337318e4bb83)

### todolist.views:

```py
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

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```py
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
    {% csrf_token %}

    {% if messages %}

    {% for message in messages %}
    {% comment %} <div class="alert alert-success" role="alert">
        {{ message }}
    </div> {% endcomment %}

    <div class="alert alert-success alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>

    {% endfor %}

    {% endif %}

    <div class="mb-3">
        <label for="task" class="form-label">Add Task</label>
        <input type="text" class="form-control" id="task" name="task" aria-describedby="textHelp"
            placeholder="Call Alex...">
        <div id="textHelp" class="form-text">What would you want to do?</div>
    </div>
    <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>


<table class="table table-light table-striped table-hover table-bordered text-center">
    <thead>
        <tr class="table-dark row">
            <th class="col-7">Task</th>
            <th class="col-3">Done</th>
            <th class="col-1">Edit</th>
            <th class="col-1">Delete</th>
        </tr>
    </thead>
    <tbody>
        {% if tasks %}

        {% for todo in tasks %}

        {% if todo.done %}
        <tr class="table-success row">
            <th class="col-7"><del>{{ todo.task }}</del> <small>(by {{ todo.owner|title }})</small></th>
            <td class="col-3"><a href="{% url 'pending' todo.id %}" type="button" class="btn btn-success btn-sm">YES - Mark as Pending</a></td>
            <td class="col-1"><a href="{% url 'edit-task' todo.id %}" type="button" class="btn btn-warning">Edit</a></td>
            <td class="col-1"><a href="{% url 'delete-task' todo.id %}" type="button" class="btn btn-danger">Delete</a></td>
        </tr>
        {% else %}
        <tr class="row">
            <th class="col-7">{{ todo.task }} <small>(by {{ todo.owner|title }})</small></th>
            <td class="col-3"><a href="{% url 'completed' todo.id %}" type="button" class="btn btn-danger btn-sm">NO - Mark as Completed</a></td>
            <td class="col-1"><a href="{% url 'edit-task' todo.id %}" type="button" class="btn btn-warning">Edit</a></td>
            <td class="col-1"><a href="{% url 'delete-task' todo.id %}" type="button" class="btn btn-danger">Delete</a></td>
        </tr>
        {% endif %}

        {% endfor %}

        {% endif %}
    </tbody>
</table>

<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">

    {% comment %} {% for i in tasks.paginator.page_range %}{% endfor %}{% endcomment %}

    <li class="page-item {% if not tasks.has_previous %} disabled {% endif %}">
      <a class="page-link" href="?pg=1">First</a>
    </li>

    {% if tasks.has_previous %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}">Previous</a>
    </li>

    <li class="page-item"><a class="page-link" href="?pg={{ tasks.previous_page_number }}">{{ tasks.previous_page_number }}</a></li>
    {% endif %}

     <li class="page-item active"><a class="page-link" href="#">{{ tasks.number }}</a></li>


    {% if tasks.has_next %}
    <li class="page-item"><a class="page-link" href="?pg={{ tasks.next_page_number }}">{{ tasks.next_page_number }}</a></li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}">Next</a>
    </li>
    {% endif %}

    <li class="page-item {% if not tasks.has_next %} disabled {% endif %}">
      <a class="page-link" href="?pg={{ tasks.paginator.num_pages }}">Last</a>
    </li>
  </ul>
</nav>


{% endblock content %}
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ee798918-a0e5-4814-a3f3-e04c35176d00">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1bf29b62-4325-4717-9382-f0780d996acf">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8063b383-0de8-490b-9a89-77fd7c327550">

# #END</details>

<details>
<summary>30. Allow only Owners to Update, Delete or changes Status of their Tasks </summary>

# Allow only Owners to Update, Delete or changes Status of their Tasks

[https://github.com/omeatai/src-python-flask-django/commit/6f5f8d6591a65b34dd77615fdc78dca64fe6958b](https://github.com/omeatai/src-python-flask-django/commit/6f5f8d6591a65b34dd77615fdc78dca64fe6958b)

### todolist.views:

```py
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


@login_required
def completed(request, id):
    task = TaskList.objects.get(pk=id)
    if task.owner == request.user:
        task.done = True
        task.save()
        # GET previous url
        previous_url = request.META.get('HTTP_REFERER')
        parsed_url = urlparse(previous_url)
        query_params = parse_qs(parsed_url.query)
        pg_value = query_params.get('pg', [None])[0]

        res = reverse('todolist') + f"?pg={pg_value}"
        return redirect(res)
    else:
        messages.error(
            request, "You are not allowed to mark this task as completed!")
        return redirect('todolist')


@login_required
def pending(request, id):
    task = TaskList.objects.get(pk=id)
    if task.owner == request.user:
        task.done = False
        task.save()
        # GET previous url
        previous_url = request.META.get('HTTP_REFERER')
        parsed_url = urlparse(previous_url)
        query_params = parse_qs(parsed_url.query)
        pg_value = query_params.get('pg', [None])[0]

        res = reverse('todolist') + f"?pg={pg_value}"
        return redirect(res)
    else:
        messages.error(
            request, "You are not allowed to mark this task as pending!")
        return redirect('todolist')


@login_required
def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    if task.owner == request.user:
        task.delete()
        messages.success(request, "Task has been deleted successfully!")
    else:
        messages.error(
            request, "You are not allowed to delete this task!")
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

```

### src-python/udemy/django-A-Z/todolist/templates/edit.html:

```py
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>

{% if task.owner == request.user %}

<form method="POST" class="row my-3">
    {% csrf_token %}

    {% if messages %}

    {% for message in messages %}

    <div class="alert alert-success alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>

    {% endfor %}

    {% endif %}

    <div class="mb-3">
        <label for="task" class="form-label">Edit Task</label>
        <input type="text" class="form-control" id="task" name="task" value="{{ task.task }}" aria-describedby="textHelp"
            placeholder="{{ task.task }}">
        <div id="textHelp" class="form-text">Make your changes</div>
    </div>
    <div class="mb-3">
        {% comment %} <input type='hidden' name="done" value="{{ task.done }}" /> {% endcomment %}

        <label for="done" class="form-label">Is it Done?</label>
        <select class="form-select" id="done" name="done" aria-label="Default select example">
            <option value=False {% if not task.done %} selected {% endif %}>NO</option>
            <option value=True {% if task.done %} selected {% endif %}>YES</option>
        </select>
    </div>
    <button type="submit" class="btn btn-primary my-2">Update TASK</button>
    <a href="{% url 'todolist' %}" class="btn btn-danger my-2">Back</a>
</form>

{% else %}

<h2>Access Denied! You are Not the Owner of this Post!</h2>
<a href="{% url 'todolist' %}" class="btn btn-danger my-2">Go To Your Todolist</a>

{% endif %}

{% endblock content %}
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/caeaf8ef-43bc-48d0-99f7-1a454b84645b">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/05a13074-87ef-4209-ac2b-79314ddfbef9">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e01329e7-6110-4a24-92f1-268570fcf576">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7eb5f0a8-2e96-448b-b085-621abe52e4e8">

# #END</details>

<details>
<summary>31. Connect PostgreSQL Database </summary>

# Connect PostgreSQL Database

[https://github.com/omeatai/src-python-flask-django/commit/5bb357bc434afaed09e1113094a862a01d515897](https://github.com/omeatai/src-python-flask-django/commit/5bb357bc434afaed09e1113094a862a01d515897)

## Install psycopg2

```py
pip install psycopg2
```

### taskmate.settings:

```py
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## Create SuperUser

```py
python manage.py createsuperuser
```

## Run Dev Server

```py
python manage.py runserver
```

<img width="763" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9f325a9d-21ba-403b-88cb-48618213066c">
<img width="1426" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/360aa47c-e52b-4e49-8ba5-0c7e1f4c9be6">
<img width="1350" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/71c3dc64-e62a-421a-8f7f-dd5f68413b93">
<img width="1382" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a6051e6d-a525-4491-b8a8-77a682053b49">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7567daca-eed8-4a71-af3d-a1716efd60ca)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/55e2f81e-c9f9-4e6a-97e2-faa0e3885b05)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/55b2c7b7-9520-4aff-81ab-7d2411181a4a)

<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/14708696-36fa-486f-a296-53fa90f14fe5">

# #END</details>

<details>
<summary>32. Deploy to Production </summary>

# Deploy to Production

## Install latest version of git

```py
brew install git
```

## Install venv

```py
python -m venv myproject-env
source myproject-env/bin/activate
```

```py
pip install virtualenv
virtualenv myproject-env
```

## Install Django

```py
python -m pip install Django
```

## Upgrade Django Version

```py
pip install --upgrade django==4.2
pip install django --upgrade
python -m pip install Django==5.0.4
```

## Install Crispy Forms

```py
pip install crispy-bootstrap5
```

## Install psycopg2

```py
pip install psycopg2
```

## Save Dependencies to Requirements.txt

```py
pip freeze
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

### .gitignore File:

```txt
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
Ex_Files/
exercise_files/

# C extensions
*.so

# Distribution / packaging
dist/
build/
*.egg-info/
*.egg

# Virtual environments
venv/
env/
env.bak/
env1/
env2/

# IDEs and editors
.idea/
.vscode/
*.sublime-project
*.sublime-workspace

# Logs and databases
*.log
*.sqlite3
*.db

# OS generated files
.DS_Store
Thumbs.db

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```

## Install django-environ

```py
pip install django-environ
```

Create .env file in same directory where settings.py exists and add the following:

- DJANGO_SECRET_KEY=XXX
- DJANGO_DEBUG=True

- DJANGO_DB_NAME=postgres
- DJANGO_DB_USER=postgres
- DJANGO_DB_PASSWORD=
- DJANGO_DB_HOST=localhost
- DJANGO_DB_PORT=5432

### taskmate.settings:

```py
from pathlib import Path
import os

import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")

ALLOWED_HOSTS = ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*"]
CSRF_TRUSTED_ORIGINS = ['https://your-base-domain']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DJANGO_DB_NAME'),
        'USER': env('DJANGO_DB_USER'),
        'PASSWORD': env('DJANGO_DB_PASSWORD'),
        'HOST': env('DJANGO_DB_HOST'),
        'PORT': env('DJANGO_DB_PORT'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

```

## Run Collectstatic

```py
python manage.py collectstatic
```

## Install Whitenoise

```py
pip install whitenoise
```

### taskmate.settings:

```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #added whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

## Create Github Project - Taskmate

## Set email and name

```py
git config --global user.name "o"
git config --global user.email "o@gmail.com"
```

### create a new repository on the command line

```py
echo "# project-django-taskmate" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add taskmate https://github.com/omeatai/project-django-taskmate.git
git push -u taskmate main
```

### push an existing repository from the command line

```py
git remote add taskmate https://github.com/omeatai/project-django-taskmate.git
git branch -M main
git push -u taskmate main
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/130b9f54-a98b-4ec2-b479-feb9d75e8a8d">

## Configure SamKirkland/FTP-Deploy for Namecheap hosting

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1ecd3b8b-ac17-440c-8ae1-d5ef19541868)

### /.github/workflows/main.yml

[https://github.com/SamKirkland/FTP-Deploy-Action](https://github.com/SamKirkland/FTP-Deploy-Action)

[Deploy To Shared Hosting With Github Actions](https://youtu.be/UNWIXYSZfZY?si=KpqsJOvREIEQ3dfV)

[Deploy Django 4.0 to Shared Hosting](https://youtu.be/nvq7NNSfKdw?si=LVJOM3xW6VukdtWi)

[https://pythonfusion.com/deploy-django-on-shared-hosting/](https://pythonfusion.com/deploy-django-on-shared-hosting/)

[https://www.namecheap.com/support/knowledgebase/article.aspx/1249/89/how-to-remotely-connect-to-a-mysql-database-located-on-our-shared-server/](https://www.namecheap.com/support/knowledgebase/article.aspx/1249/89/how-to-remotely-connect-to-a-mysql-database-located-on-our-shared-server/)

```py
on: push
name: 🚀 Deploy taskmate website on push
jobs:
  web-deploy:
    name: 🎉 Deploy
    runs-on: ubuntu-latest
    steps:
      - name: 🚚 Get latest code
        uses: actions/checkout@v4

      - name: 📂 Sync files
        uses: SamKirkland/FTP-Deploy-Action@v4.3.5
        with:
          server: ftp.ifeanyiomeata.com
          username: taskmate@ifeanyiomeata.com
          password: ${{ secrets.ftp_password }}
          protocol: ftp
          port: 21
          server-dir: /public_html/projects/taskmate/

```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ee315874-29bf-4a36-9eb0-daddb9b260e0)

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/22204623-ffc9-4745-be92-52797a0bbe78">
<img width="1414" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d6ea157f-e6a9-416e-913b-f7c2a7379ba1">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/9fa1abb8-987e-490f-b717-2515a71d82a1)

## Install requirements

```py
pip install -r requirements.txt

pip install django==3.1 psycopg2-binary django-environ whitenoise crispy-bootstrap4
pip install django psycopg2 django-environ whitenoise crispy-bootstrap5

source /home/omeatai/virtualenv/taskmate/3.9/bin/activate && cd /home/omeatai/taskmate
cd ../public_html/project_taskmate/
psql -p 5432 <dbname> <dbuser>

psql -V
psql --version
```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## For MySQL Database (Edit the **init**.py file)

```py
pip install mysqlclient

pip install pymysql
```

```py
import pymysql

pymysql.install_as_MySQLdb()
```

```py
 'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'databasename',
        'USER': 'databaseusername',
        'PASSWORD': 'databasepassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
```

# Revert to Crispy-Forms Bootstrap 4

[https://getbootstrap.com/docs/4.6/getting-started/introduction/](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

[https://pypi.org/project/crispy-bootstrap4/](https://pypi.org/project/crispy-bootstrap4/)

## Install Crispy-Bootstrap4

```py
pip install crispy-bootstrap4
```

## Update INSTALLED_APPS in settings.py

```py
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap4",
    ...
)
```

## Add CRISPY_TEMPLATE_PACK in settings.py

```py
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
```

# Revert to Crispy-Forms Bootstrap 5

[https://getbootstrap.com/](https://getbootstrap.com/)

[https://github.com/django-crispy-forms/crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5)

## Install Crispy-Bootstrap5

```py
pip install crispy-bootstrap5
```

## Update INSTALLED_APPS in settings.py

```py
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap5",
    ...
)
```

## Add CRISPY_TEMPLATE_PACK in settings.py

```py
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
```

# Setup passenger_wsgi.py

```py
# from taskmate.wsgi import application

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    start_response('200 OK', [(Content-Type, 'text/plain')])
    message = 'It works!'
    response = message
    return [response.encode()]
```

[taskmate.ifeanyiomeata.com/todolist/](taskmate.ifeanyiomeata.com/todolist/)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e68abb6f-bbab-4cb7-9b08-3d53f8532845)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/45ded09c-b989-486d-8b50-0fc0fec5f1bf)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7bde54ca-daa0-4422-b4d8-099aa64365c2)

## Run collectstatic

```py
python manage.py collectstatic
```

## Run createsuperuser

```py
python manage.py createsuperuser
```

## Export all the data from the database to a json file

```py
python manage.py dumpdata>data.json
```

## Clear the new database

```py
python manage.py flush
```

## Load the data from the data.json file into the new database

```py
python manage.py loaddata data.json
```

# #END</details>

# #END</details>



