from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class Index(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    
