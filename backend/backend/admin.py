from django.contrib import admin
from .models import *


class JobAdmin(admin.ModelAdmin):
    list_display=('title','company')


admin.site.register(Job,JobAdmin)
admin.site.register(Application)


