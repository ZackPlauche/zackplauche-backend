from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project