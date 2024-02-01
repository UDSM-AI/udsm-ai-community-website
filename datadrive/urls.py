from django.urls import path
from . import views


urlpatterns = [
    path('', views.data_drive_home, name='index'),
]