"""
Brian Shoemaker
2025F INF601 A Advanced Programming with Python
Mini Project 4
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]