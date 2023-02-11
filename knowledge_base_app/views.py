from django.shortcuts import render, redirect
from django.views.generic import ListView, \
    DetailView, UpdateView, CreateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from django.db.models import Q


class AnalysisListView(ListView):
    model = Analysis
    template_name = 'home.html'
    context_object_name = 'analysis'

class AnalysisDetailView(DetailView):
    model = Analysis
    template_name = 'analysis_detail.html'
    context_object_name = 'analysis_detail'

class AnalysisUpdateView(UpdateView):
    model = Analysis
    template_name = 'analysis_update.html'
    fields = ['analysis_code', 'completion_date', 'price', 'consumables', 'rater', 'how_prepare']

class AnalysisCreateView(CreateView):
    model = Analysis
    template_name = 'analysis_new.html'
    fields = '__all__'

class AnalysisDeleteView(DeleteView):
    model = Analysis
    template_name = 'analysis_delete.html'
    success_url = reverse_lazy('home')

class SearchResultView(ListView):
    model = Analysis
    template_name = 'search_results.html'
    # queryset = Analysis.objects.filter(title__icontains='Гликолизированный гемоглобин')

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Analysis.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
