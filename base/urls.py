from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('olga/', views.OlgaView.as_view(), name='olga'),
    path('thank-you/', views.SignupThankYouView.as_view(), name='thank_you_signup'),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/thank-you/', views.ContactThankYouView.as_view(), name='thank_you_contact'),
]
