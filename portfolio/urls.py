from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet)
router.register('images', views.ImageViewSet)
router.register('reviews', views.ReviewViewSet)

urlpatterns = router.urls