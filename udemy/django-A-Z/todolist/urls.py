from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
]
