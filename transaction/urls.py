# Develop: vmgabriel

"""Module that Define all Rooute of the module"""

from django.urls import path
from . import views


app_name = 'transactions'
urlpatterns = [
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

    # Type Bill Routes
    path(
        'type-bills/',
        views.TypeBillEntityView.as_view(),
        name='type_bills_list',
    ),
    path(
        'type-bills/create/',
        views.TypeBillEntityView.as_view(),
        name='type_bills_create'
    ),
    path(
        'type-bills/<int:id>/edit/',
        views.TypeBillEntityView.as_view(),
        name='type_bills_edit'
    ),
    path(
        'type-bills/<int:id>/delete/',
        views.TypeBillEntityView.as_view(),
        name='type_bills_delete'
    ),
    path(
        'type-bills/<int:id>/show/',
        views.TypeBillEntityView.as_view(),
        name='type_bills_show'
    ),
]
