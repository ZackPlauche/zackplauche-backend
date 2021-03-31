from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zackplauche.apps.base.urls')),
    path('services/', include('zackplauche.apps.services.urls')),
    path('blog/', include('zackplauche.apps.blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('portfolio/', include('zackplauche.apps.portfolio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)