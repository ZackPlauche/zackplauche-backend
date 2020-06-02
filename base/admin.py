from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Skill)
admin.site.register(Value)
admin.site.register(Client)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
