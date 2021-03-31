from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='service_list'),
    path('<slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('<slug>/order-summary/', views.order_summary_view, name='order_summary'),
    path('<slug>/thank-you', views.OrderThankYouView.as_view(), name='thankyou')
]
