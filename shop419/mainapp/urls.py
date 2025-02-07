from django.urls import path

from . import views  # importing the views from the mainapp to access the functions

urlpatterns = [
    path("", views.homeView, name='home'),
    path("about", views.aboutView, name="aboutpage")
]

