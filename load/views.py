from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
    }
    return render(request, 'index.html', context)

def prof(request):
    context = {
    }
    return render(request, 'prof.html', context)
