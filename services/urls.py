from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.ServiceList.as_view(), name='service_list'),  # /services/
    path('<slug:service_slug>/', views.ServiceDetail.as_view(), name='service_detail'),  # /services/service-name/
    path('<slug:service_slug>/order-summary/', views.order_summary, name='order_summary'),
    path('<slug:service_slug>/thank-you/', views.OrderThankYou.as_view(), name='thankyou')
]
