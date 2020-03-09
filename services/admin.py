from django.contrib import admin
from .models import Service, Deliverable

# class ReviewInline(admin.TabularInline):
#     model = Review
#
# class TierInline(admin.TabularInline):
#     model = Tier

# class ServiceAdmin(admin.ModelAdmin):
#     inlines = [TierInline, ReviewInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'display', 'created_date', 'call_to_action']

admin.site.register(Deliverable)
