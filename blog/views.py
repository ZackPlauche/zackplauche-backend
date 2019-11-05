from django.shortcuts import render
from .models import Post
from django.utils.text import slugify

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context=context)

def post_detail(request, post_headline):

    for post in Post.objects.all():
        if slugify(post.headline) == post_headline:
            instance = post
            break

    return render(request, 'blog/post_detail.html', {'post': instance})
