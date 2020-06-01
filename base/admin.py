from django.contrib import admin
from .models import Contact, Skill, Value

# Register your models here.
admin.site.register(Skill)
admin.site.register(Value)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
