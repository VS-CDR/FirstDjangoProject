"""first_django_dz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path

from root import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('profile/<str:username>', profile_page),
    path('riddle/', views.riddle),
    path('answer/', views.answer),
    path('multiply/', views.multiply),
    path('expression/', views.expression),
    path('history/', views.history),
    path('str2words/', views.str2words),
    path('str_history/', views.str_history),
    path('clicker/', views.clicker)
]
