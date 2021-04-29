from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('certifications', views.certifications, name='certifications'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]
