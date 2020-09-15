from django.contrib import admin
from .models import *

admin.site.register(Tag)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin): 
    list_display = ['full_name', 'post_count']

    def full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'
    full_name.short_description = 'Author'

    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Posts'
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'has_image']
    list_editable = ['published']
    save_on_top = True
    fields = (
        'author',
        ('title', 'published'),
        'image',
        'body',
    )

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Image'
