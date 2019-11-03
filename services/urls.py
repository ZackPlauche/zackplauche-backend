from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.index, name='index'),
    #path('<slug:service_title>/', views.service, name='service'),
]
