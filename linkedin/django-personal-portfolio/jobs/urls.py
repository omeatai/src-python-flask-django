from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/<int:job_id>', views.job_detail, name='job-detail'),
]
