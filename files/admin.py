from django.contrib import admin
from django.template.defaultfilters import filesizeformat

from .models import *


class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'content', 'date_pub', 'correct_size', 'user']
    list_display_links = ['name', 'file', 'content', 'date_pub',]
    readonly_fields = ['size', 'correct_size']

    def delete_queryset(self, request, queryset):
        for file in queryset:
            file.delete()



class AdvUserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'correct_max_size_of_files', 'correct_engaged_size']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        total_size = 0
        for user in qs:
            for file in user.file.all():
                total_size += file.size
            #user.engaged_size = total_size
            AdvUser.objects.filter(id = user.id).update(engaged_size = total_size,
                                                        correct_engaged_size = filesizeformat(total_size))

        return qs


admin.site.register(File, FileAdmin)
admin.site.register(AdvUser, AdvUserAdmin)