from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    # path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name="login"),
    path('login/', views.auth_login, name="login"),
    path('logout/', views.auth_logout, name="logout"),
]
