from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, \
    DetailView, UpdateView, CreateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from django.db.models import Q
import requests
import json



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

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Analysis.objects.filter(
            Q(title__icontains=query)
        )
        return object_list

api_key = '0c8447a978d6455d8e14dced0d08f42a'
api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key
def get_ip_geolocation_data(id_address):
    response = requests.get(api_url)
    return response.content
def home(request):
    x_frowarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_frowarded_for:
        ip = x_frowarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    geolocation_json = get_ip_geolocation_data(ip)
    geolocation_data = json.loads(geolocation_json)
    country = geolocation_data['country']
    region = geolocation_data['region']

    return HttpResponse('Welcome! '
                        'Your IP address is: {} and you are visiting from {} in {}'.format(ip, region, country))