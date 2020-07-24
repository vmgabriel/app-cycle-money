# Develop: vmgabriel

"""Module that Define all Rooute of the module"""

from django.urls import path
from . import views


app_name = 'transactions'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('bills/', views.BillsView.as_view(), name='views')
]
