from django.urls import path

from .views import homeView, aboutView # importing the views from the mainapp to access the functions

urlpatterns = [
    path("", homeView, name='homepage'),
    path("about", aboutView, name="aboutpage")
]

