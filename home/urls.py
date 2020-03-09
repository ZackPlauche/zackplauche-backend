from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('olga/', views.olga, name='olga'),
    path('thank-you/', views.thankyou, name='thankyou'),

]
