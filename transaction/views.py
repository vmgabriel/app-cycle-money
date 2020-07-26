# Develop: vmgabriel

"""Module that define views of app"""

import re
from typing import List, Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from django.db.models import Q

from .models import Bill, Priority
from .forms import PriorityForm

MAX_DATA = 10

r_edit = re.compile(r'/edit/$')
r_delete = re.compile(r'/delete/$')
r_create = re.compile(r'/create/$')
r_show = re.compile(r'/show/$')


def delete_last_comma(data: List[Any]):
    """delete last comma in data"""
    return data[:-1] if data[-1] == ',' else data if len(data) > 0 else data


class BillsView(generic.ListView):
    """Bill Complete Views"""
    model = Bill
    context_object_name = 'object_list'
    template_name = 'bill/list.html'


class PriorityEntityView(View):
    """Priority Create View"""
    def get(self, request, *args, **kwargs):
        """Get Priority Data"""
        if r_show.search(request.build_absolute_uri()) is not None:
            return self.detail(request, args, kwargs)

        if r_create.search(request.build_absolute_uri()) is not None:
            return self.get_one(request, args, kwargs)

        if r_edit.search(request.build_absolute_uri()) is not None:
            return self.get_edit(request, args, kwargs)

        template = 'priority/index.html'

        offset = int(request.GET['page']) if 'page' in request.GET else 0
        order = delete_last_comma(request.GET['order']).split(',') if 'order' \
            in request.GET else ['name']
        search = request.GET['search'] if 'search' in request.GET else ''

        count = Priority.objects.filter(
            Q(name__contains=search) |
            Q(description__contains=search),
            is_delete=False
        ).count()
        priorities = Priority.objects.filter(
            Q(name__contains=search) |
            Q(description__contains=search),
            is_delete=False
        ).order_by(*tuple(order))[MAX_DATA*offset:MAX_DATA*(offset+1)]
        count_getted = len(priorities)
        return render(
            request,
            template,
            {
                'count_priorities': count,
                'priorities': priorities,
                'count_getted': count_getted,
                'max_data': MAX_DATA,
                'offset': offset,
                'orders': order,
                'search': search,
                'next': (offset + 1) * MAX_DATA < count,
                'paginator': [
                    (offset + 2, ((offset + 1) * MAX_DATA) < count),
                    (offset + 3, ((offset + 2) * MAX_DATA) < count)
                ]
            }
        )

    def detail(self, request, *args, **kwargs):
        """Detail Template"""
        template = 'priority/detail.html'
        _id = args[1]['id']
        priority = get_object_or_404(Priority, pk=_id)
        return render(
            request,
            template, {
                'priority': priority
            }
        )

    def get_edit(self, request, *args, **kwargs):
        """Get Edit Template"""
        template = 'priority/create.html'
        _id = args[1]['id']
        priority = get_object_or_404(Priority, pk=_id)
        print('priority - ', priority)
        return render(
            request,
            template,
            {
                'mode': 'edit',
                'priority': priority
            }
        )

    def get_one(self, request, *args, **kwargs):
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
        if r_edit.search(request.build_absolute_uri()) is not None:
            return self.put(request, args, kwargs)

        if r_delete.search(request.build_absolute_uri()) is not None:
            return self.delete(request, args, kwargs)

        to_save_priority = PriorityForm(request.POST)
        if to_save_priority.is_valid():
            _ = to_save_priority.save()
            return redirect('transactions:priorities_list')
        return HttpResponse('')

    def put(self, request, *args, **kwargs):
        """Update Priority Data"""
        print('this is the put')
        _id = args[1]['id']
        to_update = get_object_or_404(Priority, pk=_id)
        to_update_priority = PriorityForm(request.POST, instance=to_update)
        if to_update_priority.is_valid():
            _ = to_update_priority.save()
            return redirect('transactions:priorities_list')
        return HttpResponse('')

    def delete(self, request, *args, **kwargs):
        """Delete Priority Data"""
        _id = args[1]['id']
        _ = Priority.objects.filter(pk=_id).update(is_delete=True)
        return redirect('transactions:priorities_list')

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


