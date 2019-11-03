from django.contrib import admin
from .models import Service

# class ReviewInline(admin.TabularInline):
#     model = Review
#
# class TierInline(admin.TabularInline):
#     model = Tier

# class ServiceAdmin(admin.ModelAdmin):
#     inlines = [TierInline, ReviewInline]

admin.site.register(Service)
