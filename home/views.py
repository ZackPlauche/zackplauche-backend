from django.shortcuts import render
from django.http import HttpResponseRedirect
from services.models import Service


def index(request):
    services = Service.objects
    context = {'services': services}
    return render(request, 'home/index.html', context=context)

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def olga(request):
    return render(request, 'home/olga.html')
