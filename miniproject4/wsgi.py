"""
Brian Shoemaker
2025F INF601 A Advanced Programming with Python
Mini Project 4
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproject4.settings')

application = get_wsgi_application()