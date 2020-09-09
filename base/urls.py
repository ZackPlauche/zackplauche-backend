from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('olga/', views.Olga.as_view(), name='olga'),
    path('thank-you/', views.SignupThankYou.as_view(), name='thank_you_signup'),
    path('about/', views.About.as_view(), name="about"),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('contact/thank-you/', views.ContactThankYou.as_view(), name='thank_you_contact'),
]
