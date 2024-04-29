"""Techpile URL Configuration

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
from django.urls import path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register/',views.register),
    path('contact/',views.contact),
    path('feedback/',views.feedback),
    path('aboutus/',views.aboutus),
    path('placement/',views.placement),
    path('policy/',views.policy),
    path('course/',views.course),
    path('summer/',views.summer),
    path('winter/',views.winter),
    path('apprenticeship/',views.apprenticeship),
    path('syllabus/',views.syllabus),
    path('industrial/',views.industrial),
    path('video/',views.video),
    path('image/',views.image),
    path('python/',views.python),
    path('php/',views.php),
    path('java/',views.java),
    path('android/',views.android),
    path('html/',views.html),
    path('css/',views.css),
    path('c/',views.c),
    path('net/',views.net),
]
