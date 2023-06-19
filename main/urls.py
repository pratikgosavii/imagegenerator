"""templategenerator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from .views import *

urlpatterns = [
    path('admin-dashbaord/', admin_dashbaord, name="admin_dashbaord"),
    path('dashboard/', dashbaord, name="dashboard"),
    path('generate_card/', generate_card, name="generate_card"),
    path('all_generate_card/', all_generate_card, name="all_generate_card"),
    path('downlaod_image/<image_path>', downlaod_image, name="downlaod_image"),
    path('theme-details/<theme_id>', theme_details, name="theme_details"),
    path('select-frame', select_frame, name="select_frame"),
]
