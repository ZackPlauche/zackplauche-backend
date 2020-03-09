from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponseRedirect

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
        return HttpResponseRedirect('thank-you/')
    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'home/contact.html', context=context)


def thankyou(request):
    return render(request, 'contact/thankyou.html')
