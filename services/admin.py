from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import *


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    verbose_name_plural = 'all orders'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['get_email', 'get_name', 'total_orders']
    inlines = [OrderInline]

    def get_email(self, client):
        return client.user.email
    get_email.short_description = 'email'

    def get_name(self, client):
        return f'{client.user.first_name} {client.user.last_name}'
    get_name.short_description = 'name'

    
    

@admin.register(Service)
class ServiceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = [
        'order',
        'title',
        'display',
        'has_icon',
        'service_type',
        'price_display',
        'payment_type',
        'created_date',
        'call_to_action',
    ]
    list_display_links = ['title']
    fieldsets = (
        (None, {
            'fields': (
                'icon',
                ('title', 'display'),
                ('service_type'),
                ('payment_type', 'price'),
                'short_description',
                'call_to_action',)
        }),
        ('Sales Page', {
            'fields': ('long_description', 'deliverables',),
            'classes': ('collapse',)
        })
    )
    list_editable = ['display', 'call_to_action']
    list_filter = ['display', 'service_type']

    def has_icon(self, obj):
        return bool(obj.icon)
    has_icon.boolean = True
    has_icon.short_description = 'icon'


admin.site.register(Deliverable)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'client_email',
        'client_name',
        'total',
        'date',
    ]
    list_filter = ['date']

    fields = (
        'services',
        'client',
    )

    def client_name(self, order):
        return f'{order.client.user.first_name} {order.client.user.last_name}'
    client_name.short_description = 'client name'

    def client_email(self, order):
        return order.client.user.email
    client_email.short_description = 'client email'
