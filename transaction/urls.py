# Develop: vmgabriel

"""Module that Define all Rooute of the module"""

from django.urls import path
from . import views


app_name = 'transactions'
urlpatterns = [
    path('data/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('bills/', views.BillsView.as_view(), name='views'),
    # Priorities Routes
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
    ),
    path(
        'priorities/<int:id>/show/',
        views.PriorityEntityView.as_view(),
        name='priorities_show'
    ),

    # Type Consume Routes
    path(
        'type-consumes/',
        views.TypeConsumeEntityView.as_view(),
        name='type_consumes_list',
    ),
    path(
        'type-consumes/create/',
        views.TypeConsumeEntityView.as_view(),
        name='type_consumes_create'
    ),
    path(
        'type-consumes/<int:id>/edit/',
        views.TypeConsumeEntityView.as_view(),
        name='type_consumes_edit'
    ),
    path(
        'type-consumes/<int:id>/delete/',
        views.TypeConsumeEntityView.as_view(),
        name='type_consumes_delete'
    ),
    path(
        'type-consumes/<int:id>/show/',
        views.TypeConsumeEntityView.as_view(),
        name='type_consumes_show'
    ),
]
