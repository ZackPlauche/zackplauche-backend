from django.contrib import admin
from .models import Project, Tag, Technology, Category, Requirement, Contributor

# Register your models here.

admin.site.register(Technology)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Requirement)
admin.site.register(Contributor)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'display', 'favorite', 'category', 'live_url', 'github_repository', 'download_file']
