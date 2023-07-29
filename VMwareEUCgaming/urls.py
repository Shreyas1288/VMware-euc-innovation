"""VMwareEUCgaming URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
# from gaming_board import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('gaming_board.urls')),
]
