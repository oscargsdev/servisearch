from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Worker

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'classified/index.html'
    context_object_name = 'workers_list'

    def get_queryset(self):
        return Worker.objects.all()
    
class DetailView(generic.DetailView):
    model = Worker
    template_name = 'classified/detail.html'

    def get_queryset(self):
        return Worker.objects.all()