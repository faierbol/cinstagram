from django.urls import path, include
from . import views

urlpatterns = [
    # home
    path("", views.home, name="home"),
    # home
    path("home/", views.home, name="home"),
]
