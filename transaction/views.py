# Develop: vmgabriel

"""Module that define views of app"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Bill


class BillsView(generic.ListView):
    """Bill Complete Views"""
    model = Bill
    context_object_name = 'object_list'
    template_name = 'bill/list.html'


def index(request):
    """Get Process"""
    template = 'transaction/create.html'
    return render(request, template)


def create(request):
    """Create Process Data"""

    if request.method == 'POST':
        data = dict(request.POST)
        print(str(data))
        message = 'Datos - {}'.format(str(data))
        return HttpResponse(message)
    message = 'Create a New Transaction'
    return HttpResponse(message)
