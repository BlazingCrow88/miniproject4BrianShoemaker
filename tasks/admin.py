"""
Brian Shoemaker
2025F INF601 A Advanced Programming with Python
Mini Project 4
"""

from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for Task model
    """
    list_display = ['title', 'priority', 'status', 'due_date', 'user', 'created_at']
    list_filter = ['priority', 'status', 'created_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'user')
        }),
        ('Task Details', {
            'fields': ('priority', 'status', 'due_date')
        }),
    )