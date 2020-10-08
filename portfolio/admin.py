from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'display',
        'project_type',
        'live_url',
        'github_repository',
        'download_file'
    ]
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'display'),
                'category',
            )
        }),
    )


admin.site.register(Technology)
admin.site.register(Contributor)
