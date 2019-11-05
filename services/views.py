from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service
from django.utils.text import slugify

def index(request):
    services = Service.objects.all()
    return render(request, 'services/index.html', {'services': services})

def service_detail(request, service):

    for serv in Service.objects.all():
        print(serv.title, slugify(self.title))
        if slugify(serv.title)  == service:
            instance = serv
            break

    #service = Service.objects.get(slug=service)
    # context = {'service': service}
    return render(request, 'services/service_detail.html', {'service': instance})
