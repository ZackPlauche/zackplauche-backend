from django.shortcuts import render
from .models import Service
from django.utils.text import slugify

def index(request):
    services = Service.objects.all()
    return render(request, 'services/index.html', {'services': services})

def service_detail(request, service):

    for serv in Service.objects.all():
        if slugify(serv.title)  == service:
            instance = serv
            break

    #service = Service.objects.get(slug=service)
    # context = {'service': service}
    return render(request, 'services/service_detail.html', {'service': instance})
