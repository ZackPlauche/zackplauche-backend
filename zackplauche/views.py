from django.shortcuts import render, get_object_or_404
from services.models import Service


def home(request):
    """https://zackplauche.com/"""
    service_list = Service.objects.all()
    return render(request, 'home.html',{'service_list':service_list})
