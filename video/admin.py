from django.contrib import admin
from .models import *


admin.site.register(Video)
admin.site.register(Upcoming_video)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Authorities)
class AuthoritiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'role']
