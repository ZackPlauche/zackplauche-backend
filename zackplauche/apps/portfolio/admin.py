from django.contrib import admin
from .models import Project, Technology, Contributor

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'display',
        'project_type',
        'live_url',
        'download_file'
    ]
    fieldsets = (
        (None, {
            'fields': (
                'image',
                ('title', 'display'),
                'status',
                'project_type',
                'purpose',
                'description',
            )
        }),
        ('Resources', {
            'fields': (
                'technologies_used',
                'contributors',
                'github_repository',
                'demo_vid_url',
                'live_url',
                'download_file',
            )
        })
    )


admin.site.register(Technology)
admin.site.register(Contributor)
