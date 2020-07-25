# Develop: vmgabriel

"""Module that Define all Rooute of the module"""

from django.urls import path
from . import views


app_name = 'transactions'
urlpatterns = [
    path('data/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('bills/', views.BillsView.as_view(), name='views'),
    path(
        'priorities/',
        views.PriorityListView.as_view(),
        name='priorities_list'
    ),
    path(
        'priorities/create/',
        views.PriorityCreateView.as_view(),
        name='priorities_create'
    ),
    path(
        'priorities/<int:id>/edit/',
        views.PriorityCreateView.as_view(),
        name='priorities_edit'
    )
]
