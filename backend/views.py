from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
        return render(request, 'backend/index_template.html', context={})


def dice(request):
        return render(request, 'backend/dice_template.html', context={})

def luffer(request):
        return render(request, 'backend/luffer_template.html', context={})

def klingberg(request):
        return render(request, 'backend/klingberg_template.html', context={})