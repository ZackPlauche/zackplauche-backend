from django.shortcuts import render
from .models import Service
from django.utils.text import slugify

services = Service.objects

def index(request):

    return render(request, 'services/index.html', {'services': services})


def service_detail(request, service_slug):

    for service in services.all():
        if slugify(service.title)  == service_slug:
            instance = service
            break

    #service = Service.objects.get(slug=service)
    # context = {'service': service}
    return render(request, 'services/service_detail.html', {'service': instance})
