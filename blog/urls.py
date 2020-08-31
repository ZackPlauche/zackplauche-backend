from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # /blog/
    path('<slug:slug>/', views.PostDetail.as_view(), name='post'),  # /blog/post-title
]
