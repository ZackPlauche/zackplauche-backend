from django.shortcuts import render
from .models import Project
from django.utils.text import slugify
# Create your views here.

projects = Project.objects

def index(request):
    """View for the index of owners portfolio projects."""
    context = {'projects': projects}
    return render(request, 'portfolio/index.html', context)

def project_detail(request, project_title):

    for project in projects.all():
        if slugify(project.title) == project_title:
            instance = project
            break

    context = {'project': instance}

    return render(request, 'portfolio/project_detail.html', context)
