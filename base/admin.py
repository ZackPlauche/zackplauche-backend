from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import *
from .models import *

# Register your models here.


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_superuser',
        'is_staff',
        'is_client'
    ]
    list_editable = ['is_active', 'is_superuser', 'is_staff']
    ordering = ['email']
    search_fields = ['email']
    fieldsets = (
        (None, {
            'fields': ['email', 'password'],
        }),
        ('Personal info', {'fields': ['first_name', 'last_name']}),
        ('Permissions', {'fields': ['is_active', 'is_superuser', 'is_staff']})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    def is_client(self, user):
        try:
            return bool(user.client)
        except:
            return False
    is_client.boolean = True
    is_client.short_description = 'client'


admin.site.register(User, UserAdmin)
admin.site.register(Contact)
admin.site.unregister(Group)
