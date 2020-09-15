from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),  # /blog/
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),  # /blog/post-title
]
