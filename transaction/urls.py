# Develop: vmgabriel

"""Module that Define all Rooute of the module"""

from django.urls import path, re_path
from . import views


app_name = 'transactions'
urlpatterns = [
    path('data/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('bills/', views.BillsView.as_view(), name='views'),
    path(
        'priorities/',
        views.PriorityEntityView.as_view(),
        name='priorities_list',
    ),
    path(
        'priorities/create/',
        views.PriorityEntityView.as_view(),
        name='priorities_create'
    ),
    path(
        'priorities/<int:id>/edit/',
        views.PriorityEntityView.as_view(),
        name='priorities_edit'
    ),
    path(
        'priorities/<int:id>/delete/',
        views.PriorityEntityView.as_view(),
        name='priorities_delete'
    )
]
