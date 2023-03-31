from django.contrib import admin
from .models import Profile, Log
from blog.admin import PostInline, CommentInline

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['created_at']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "nc"]
    inlines = [PostInline, CommentInline]
