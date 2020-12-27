from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    fields = ('User', 'description','image')
