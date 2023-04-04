from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Worker, Employer

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
    

def register(request):
    return render(request, 'classified/register.html')

def success(request):
    user = Employer.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            phone_number = request.POST['phone_number']
        )
    user.save()

    return HttpResponse("Registro exitoso")

    

    