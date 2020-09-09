from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView

from services.models import Service
from .models import *
from .forms import *

class Home(FormView):
    form_class = NewsletterForm
    template_name = 'base/home.html'
    success_url = 'thank-you/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(display=True)
        context['clients'] = clients = Client.objects.filter(display=True)
        return context


# Create your views here.
class About(TemplateView):
    template_name = 'base/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.order_by('title')
        context['values'] = Value.objects.all()


class SignupThankYou(TemplateView):
    template_name = 'base/thank-you-signup.html'


class Contact(FormView):
    form_class = ContactForm
    template_name='base/contact.html'
    success_url = '/contact/thank-you/'

class ContactThankYou(TemplateView):
    template_name = 'base/thank-you-contact.html'

class Olga(TemplateView): 
    template_name = 'base/olga.html'
