# Develop: vmgabriel

"""Module that define views of app"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View

from .models import Bill, Priority
from .forms import PriorityForm


class BillsView(generic.ListView):
    """Bill Complete Views"""
    model = Bill
    context_object_name = 'object_list'
    template_name = 'bill/list.html'


class PriorityListView(View):
    """Priority List View"""

    def get(self, request, *args, **kwargs):
        """Get Priority View"""
        template = 'priority/index.html'
        count = Priority.objects.all().count()
        priorities = Priority.objects.all()[:10]
        return render(
            request,
            template,
            {
                'count_priorities': count,
                'priorities': priorities
            }
        )


class PriorityCreateView(View):
    """Priority Create View"""

    def get(self, request, *args, **kwargs):
        """Get Priority Create/Edit List"""
        template = 'priority/create.html'
        return render(
            request,
            template,
            {
                'mode': 'create'
            }
        )

    def post(self, request, *args, **kwargs):
        """Post Priority Create/Edit"""
        print('request.Post - ', dict(request.POST))
        print('.-----.')
        print('data - {}'.format(PriorityForm()))
        print('.-----.')
        to_save_priority = PriorityForm(request.POST)

        print('valid? - ', to_save_priority.is_valid())

        if to_save_priority.is_valid():
            _ = to_save_priority.save()
            return redirect('transactions:priorities_list')
        return HttpResponse('')


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
