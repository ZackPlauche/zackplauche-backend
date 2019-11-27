from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # /blog/
    path('<slug:post_title>/', views.post, name='post'),  # /blog/post-title
]