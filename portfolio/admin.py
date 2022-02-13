from django.utils.html import format_html
from django.contrib import admin

from .models import Contributor, Project, Image, Technology, Contribution, Review, ReviewSource


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('contributor', 'project', 'role', 'description')

    fields = (
        'contributor',
        'project',
        'role',
        'description',
    )


class ContributionInline(admin.TabularInline):
    model = Contribution
    extra = 1
    fields = ('contributor', 'project', 'role', 'description')
    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'clickable_site_url', 'active', 'featured', 'status')
    list_editable = ('active', 'featured', 'status')
    list_filter = ('active', 'featured', 'status')
    search_fields = ('title',)
    inlines = [ContributionInline]

    @admin.display(description='Site URL')
    def clickable_site_url(self, obj):
        return format_html(f'<a href="{obj.site_url}" target="_blank">{obj.site_url}</a>')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('alt', 'file', 'url')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'has_icon')

    @admin.display(boolean=True, description='Icon')
    def has_icon(self, obj):
        return bool(obj.icon)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_name', 'source')
    list_editable= ('source', )

    @admin.display(description='Review')
    def review_name(self, obj):
        return str(obj)


admin.site.register(Contributor)
admin.site.register(ReviewSource)
