"""VMware gaming board  URL Configuration
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api-upload-excel-file/<int:pk>/', views.ReadExcelFile.as_view()),
    path('api-get-score/', views.GetTeamScore.as_view()),
    path('api-upload-excel-file-v2/<int:pk>/', views.ReadExcelFileV2.as_view()),
    path('api-get-score-v2/', views.GetTeamScoreV2.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
