from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from services.models import Service
from .models import Contact, CriteriaForSuccess, Skill, Value
from .forms import NewsletterForm, ContactForm

def home(request):
    services = Service.objects.filter(display=True)

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
        return render(request, 'base/home.html', context=context)



# Create your views here.
def about(request):
    success_criteria = CriteriaForSuccess.objects.all()
    skills = Skill.objects.all().order_by('title')
    values = Value.objects.all()

    context = {
        'success_criteria': success_criteria,
        'skills': skills,
        'values': values,
    }

    return render(request, 'base/about.html', context=context)

def thank_you_signup(request):
    return render(request, 'base/thank-you-signup.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
        return HttpResponseRedirect('thank-you/')
    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'base/contact.html', context=context)


def thank_you_contact(request):
    return render(request, 'base/thank-you-contact.html')

def olga(request):
    return render(request, 'base/olga.html')
