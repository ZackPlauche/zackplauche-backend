from django import forms
from django.forms import ModelForm

from base.models import *
from .models import *


class OrderForm(ModelForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label="")
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label="")
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label="")

    class Meta:
        model = Order
        fields = ('service', 'first_name', 'last_name', 'email')

    def save(self, commit=True, *args, **kwargs):
        order = super().save(commit=False)
        user, user_created = User.objects.get_or_create(email=self.cleaned_data['email'])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        client, client_created = Client.objects.get_or_create(user=user)
        order.client = client
        if commit:
            order.save()
        return order

