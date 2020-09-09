from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class PostList(ListView):
    model = Post
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    
