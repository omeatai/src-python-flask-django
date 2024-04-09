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
