from django.contrib import admin
from website.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date', 'updated_date')
    date_hierarchy = 'created_date'
    search_fields = ('name', 'email')
    list_filter = ('created_date', 'updated_date', 'name')

admin.site.register(Contact,ContactAdmin)
