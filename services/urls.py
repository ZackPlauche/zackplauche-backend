from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.index, name='index'),  # /services/
    path('<slug:service_slug>/', views.service_detail, name='service_detail'),  # /services/service-name/
    path('<slug:service_slug>/order-summary/', views.order_summary, name='order_summary'),
]
