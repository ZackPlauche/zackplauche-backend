from django.shortcuts import render
from .models import Post
from django.utils.text import slugify

def index(request):
    posts = Post.objects
    context = {'posts': posts}
    return render(request, 'blog/index.html', context=context)

def post(request, post_title):

    for post in Post.objects.all():
        if slugify(post.title) == post_title:
            instance = post
            break

    return render(request, 'blog/post.html', {'post': instance})
