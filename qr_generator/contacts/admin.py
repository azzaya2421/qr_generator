from django.contrib import admin

from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'image', 'phone','email', 'qr_code']
    search_fields = ('first_name', )


admin.site.register(Contact,ContactAdmin)

