from django import forms
from django.forms import ModelForm
from base.models import Contact

class NewsletterForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput({'placeholder':'Enter your email.'}), label='')
    class Meta:
        model = Contact
        fields = ['email']

class ContactForm(ModelForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput({'placeholder':'First Name'}), label='')
    email = forms.EmailField(widget=forms.EmailInput({'placeholder':'Email Address (e.g., youremail@gmail.com)'}), label='')
    message = forms.CharField(widget=forms.Textarea({'placeholder':'Message'}), label='')
    class Meta:
        model = Contact
        fields = ('first_name', 'email', 'message')
