from django.shortcuts import render, get_object_or_404
from .models import Service

def index(request):
    service_list = Service.objects.all()
    return render(request, 'services/index.html', {'service_list': service_list})

# def service(request):
    pass
