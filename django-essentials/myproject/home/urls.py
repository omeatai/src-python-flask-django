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
