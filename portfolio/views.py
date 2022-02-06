from rest_framework import viewsets

from .serializers import ImageSerializer, ProjectSerializer
from portfolio.models import Project, Image


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
