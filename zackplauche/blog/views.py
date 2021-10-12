from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    
