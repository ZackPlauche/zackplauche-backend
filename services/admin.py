from django.contrib import admin
from .models import *

# class ReviewInline(admin.TabularInline):
#     model = Review
#
# class TierInline(admin.TabularInline):
#     model = Tier

# class ServiceAdmin(admin.ModelAdmin):
#     inlines = [TierInline, ReviewInline]

class TestimonialInline(admin.TabularInline):
    model = Testimonial

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'display', 'created_date', 'call_to_action']
    fields = (
        'icon',
        ('title', 'display'),
        'price',
        'short_description',
        'deliverables',
        'call_to_action',
    )

admin.site.register(Deliverable)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['service', 'order_total', 'date', 'email', 'full_name', 'id']
    fields = (
        'service',
        ('first_name', 'last_name'),
        'email',
    )
