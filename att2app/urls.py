from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("index/", views.index, name='index'),
    path("room2/", views.room2, name = "room2"),
    path("add-temperature/", views.add_temperature, name="add_temperature"),
    path("sensor_data/", views.sensor_data, name="sensor_data"),
    path("sensor_data1/", views.sensor_data1, name="sensor_data1"),
    path("sensor_data2/", views.sensor_data2, name="sensor_data2"),
    path("sensor_data3/", views.sensor_data3, name="sensor_data3"),
    path("sensor_data4/", views.sensor_data4, name="sensor_data4"), 
    path("sensor_data5/", views.sensor_data5, name="sensor_data5"),
]