from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from base.models import *


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput({'placeholder': 'Enter your email.'}), label='')

    class Meta:
        model = Contact
        fields = ['email']

    def save(self, commit=True, *args, **kwargs):
        email = self.cleaned_data['email']
        user, user_created = User.objects.get_or_create(email=email)
        contact, contact_created = Contact.objects.get_or_create(user=user)
        if commit:
            contact.save()
        return contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput({'placeholder': 'First Name'}), label='')
    last_name = forms.CharField(max_length=20, widget=forms.TextInput({'placeholder': 'Last Name'}), label='')
    email = forms.EmailField(widget=forms.EmailInput({'placeholder': 'Email Address (e.g., youremail@gmail.com)'}), label='')
    message = forms.CharField(widget=forms.Textarea({'placeholder': 'Message'}), label='')

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')

    def save(self, commit=True, *args, **kwargs):
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        message = self.cleaned_data['message']
        user, user_created = User.objects.get_or_create(email=email)
        user.first_name = first_name
        user.last_name = last_name
        contact, contact_created = Contact.objects.get_or_create(user=user)
        contact.messages.append(message)
        if commit:
            user.save()
            contact.save()
        return contact


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'password')

    def clean_password(self):
        return self.initial['password']
