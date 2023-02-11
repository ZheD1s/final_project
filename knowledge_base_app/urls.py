from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('analysis/<int:pk>', AnalysisDetailView.as_view(), name='analysis_detail'),
    path('analysis/<int:pk>/update', AnalysisUpdateView.as_view(), name='analysis_update'),
    path('analysis/new/', AnalysisCreateView.as_view(), name='analysis_create'),
    path('analysis/<int:pk>/delete', AnalysisDeleteView.as_view(), name='analysis_delete'),
    path('my_cabinet/', TemplateView.as_view(template_name='my_cabinet.html'), name='my_cabinet'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', AnalysisListView.as_view(), name='home'),
]