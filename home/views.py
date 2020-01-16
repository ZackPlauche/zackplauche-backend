from django.shortcuts import render
from django.http import HttpResponseRedirect
from services.models import Service


def home(request):
    services = Service.objects
    context = {'services': services}
    return render(request, 'home/home.html', context=context)

def contact(request):
    return render(request, 'home/contact.html')

def olga(request):
    return render(request, 'home/olga.html')
