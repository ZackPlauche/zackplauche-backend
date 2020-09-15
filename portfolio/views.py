from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
class ProjectList(ListView):
    model = Project

class ProjectDetail(DetailView):
    model = Project