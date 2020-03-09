from django import forms
from django.forms import ModelForm
from contact.models import Contact

class NewsletterForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput({'placeholder':'Enter your email.'}), label='')
    class Meta:
        model = Contact
        fields = ['email']
