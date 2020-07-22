# Develop: vmgabriel

"""Module that define views of app"""

from django.shortcuts import render


def index(request):
    """Get Process"""
    template = 'transaction/create.html'
    return render(request, template)
