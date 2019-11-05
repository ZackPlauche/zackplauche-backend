from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
#   # /services/
    path('', views.index, name='index'),

    # /services/service-name/
    path('<slug:service>/', views.service_detail, name='service_detail'),
]
