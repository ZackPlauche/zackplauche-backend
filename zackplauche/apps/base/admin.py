from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm
from .models import User, Contact

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
        'is_author',
        'is_client',
        'is_contact',
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


admin.site.register(User, UserAdmin)
admin.site.register(Contact)
admin.site.unregister(Group)