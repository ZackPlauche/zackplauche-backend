from django import forms
from django.forms import ModelForm
from .models import Order, Service

class OrderForm(ModelForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label="")
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}), label="")
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label="")
    class Meta:
        model = Order
        fields = ('service', 'first_name', 'last_name', 'email')
