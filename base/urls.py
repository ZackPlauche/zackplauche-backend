from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('olga/', views.olga, name='olga'),
    path('thank-you/', views.thank_you_signup, name='thank_you_signup'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name='contact'),
    path('contact/thank-you/', views.thank_you_contact, name='thank_you_contact'),
]
