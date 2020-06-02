from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Service, Order
from base.models import Contact
from .forms import OrderForm
from base.forms import ContactForm


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

    # Get current service
    for service in services.all():
        if slugify(service.title) == service_slug:
            instance = service
            break

    # Create initial forms
    form = OrderForm(initial={'service': instance})


    if request.method == 'POST':

        # Call filled forms
        filled_form = OrderForm(request.POST)

        # Validate data
        if filled_form.is_valid():
            filled_form.save()
            return HttpResponseRedirect('../thank-you')

    else:
        context = {
            'service': instance,
            'form': form,
        }
        return render(request, 'services/order_summary.html', context)

def thankyou(request, service_slug):
    return render(request, 'services/thankyou.html')
