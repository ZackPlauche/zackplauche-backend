from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, TemplateView, FormView

from .forms import OrderForm
from .models import Service, Order
from base.forms import ContactForm
from base.models import Contact



class ServiceList(ListView):
    model = Service
    template_name = 'services/index.html'
    context_object_name = 'services'

class ServiceDetail(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

def order_summary(request, slug):

    service = Service.objects.get(slug=slug)

    # Create initial forms
    form = OrderForm(initial={'service': service})


    if request.method == 'POST':

        # Call filled forms
        form = OrderForm(request.POST)

        # Validate data
        if form.is_valid():
            form.save()
            return redirect('../thank-you')

    else:
        context = {
            'service': service,
            'form': form,
        }
        return render(request, 'services/order_summary.html', context)


class OrderThankYou(DetailView):
    model = Service
    template_name = 'services/thankyou.html'
