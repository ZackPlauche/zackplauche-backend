from django.views.generic import TemplateView, CreateView

from ..services.models import Service, Company
from .forms import NewsletterForm, ContactForm


class HomeView(CreateView):
    form_class = NewsletterForm
    template_name = 'base/home.html'
    success_url = 'thank-you/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(display=True)
        context['companies'] = Company.objects.filter(worked_with=True)
        return context


# Create your views here.
class AboutView(TemplateView):
    template_name = 'base/about.html'


class SignupThankYouView(TemplateView):
    template_name = 'base/thank-you-signup.html'


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'base/contact.html'
    success_url = '/contact/thank-you/'


class ContactThankYouView(TemplateView):
    template_name = 'base/thank-you-contact.html'


class OlgaView(TemplateView):
    template_name = 'base/olga.html'
