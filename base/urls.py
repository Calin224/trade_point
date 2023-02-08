from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'base'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(authentication_form = LoginForm, template_name='base/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/logout.html'), name="logout"),
]
