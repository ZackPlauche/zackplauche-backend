from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Service
from .forms import OrderForm


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

def order_summary(request, service_slug):

    for service in services.all():
        if slugify(service.title) == service_slug:
            instance = service
            break

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../thank-you/')
        else:
            print(form.errors)

    else:
        form = OrderForm(initial={'service_ordered': instance})
        context = {
            'service': instance,
            'form': form,
        }
        return render(request, 'services/order_summary.html', context)

def order_form(request, service_slug):

    for service in services.all():
        if slugify(service.title) == service_slug:
            instance = service
            break

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../thank-you/')
        else:
            print(form.errors)

    else:
        form = OrderForm(initial={'service_ordered': instance})
        context = {
            'service': instance,
            'form': form,
        }
        return render(request, 'services/order_form.html', context)

def thankyou(request, service_slug):
    return render(request, 'services/thankyou.html')
