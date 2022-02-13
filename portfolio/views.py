from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets


from .serializers import ImageSerializer, ProjectSerializer, ReviewSerializer
from .models import Project, Image, Review


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filter_fields = '__all__'

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        print('we are called from frontend')
        return super().list(request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
