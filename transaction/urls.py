# Develop: vmgabriel

"""Module that Define all Rooute of the module"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]

