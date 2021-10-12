from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView

from .forms import OrderForm
from .models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'services/index.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

def order_summary_view(request, slug):
    service = Service.objects.get(slug=slug)
    form = OrderForm(initial={'service': service})

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('services:thankyou', kwargs={'slug': service.slug}))
        else:
            print(form.errors)
    context = {
        'service': service,
        'form': form,
    }
    return render(request, 'services/order_summary.html', context)


class OrderThankYouView(DetailView):
    model = Service
    template_name = 'services/thankyou.html'
