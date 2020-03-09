from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from services.models import Service
from contact.models import Contact
from home.forms import NewsletterForm

def home(request):
    services = Service.objects

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        form.save()
        return HttpResponseRedirect('thank-you/')
    else:
        form = NewsletterForm()
        context = {
            'services': services,
            'form': form,
        }
        return render(request, 'home/home.html', context=context)

def thankyou(request):
    return render(request, 'home/thankyou.html')

def olga(request):
    return render(request, 'home/olga.html')
