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


