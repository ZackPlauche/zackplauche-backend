from django.contrib import admin
from .models import Service, Deliverable, Order

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

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'service_ordered']
