from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # /blog/
    path('<slug:post_headline>/', views.post_detail, name='post_detail'),  # /blog/post-title
]
