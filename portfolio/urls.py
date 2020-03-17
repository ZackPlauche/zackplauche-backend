from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:project_title>/', views.project_detail, name="project_detail")
]
