from django.contrib import admin
from .models import *

class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'content', 'date_pub', 'size', ]
    list_display_links = ['name', 'file', 'content', 'date_pub',]
    readonly_fields = ['size',]


admin.site.register(File, FileAdmin)