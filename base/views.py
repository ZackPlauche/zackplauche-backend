from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, CreateView

from services.models import *
from .models import *
from .forms import *


class Home(CreateView):
    form_class = NewsletterForm
    template_name = 'base/home.html'
    success_url = 'thank-you/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(display=True)
        context['companies'] = Company.objects.filter(worked_with=True)
        return context


# Create your views here.
class About(TemplateView):
    template_name = 'base/about.html'


class SignupThankYou(TemplateView):
    template_name = 'base/thank-you-signup.html'


class Contact(CreateView):
    form_class = ContactForm
    template_name = 'base/contact.html'
    success_url = '/contact/thank-you/'


class ContactThankYou(TemplateView):
    template_name = 'base/thank-you-contact.html'


class Olga(TemplateView):
    template_name = 'base/olga.html'
