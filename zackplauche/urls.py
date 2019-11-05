from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
