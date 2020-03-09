from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('thank-you/', views.thankyou, name='thankyou')
]
