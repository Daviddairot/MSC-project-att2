from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("add-temperature/", views.add_temperature, name="add_temperature"),
]