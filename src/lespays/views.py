from django.shortcuts import render
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import ContinentForm
# Create your views here.
def home(request):
    context = {
        'nb_continent' : Continent.objects.all().count(),
        'nb_pays': Pays.objects.all().count(),
    }
    return render(request, 'sidebar.html', context)


class ContinentCreateView(CreateView):
    model = Continent
    form_class = ContinentForm 
    template_name = 'create_continent.html'
    success_url = reverse_lazy('home')

class ContinentUpdateView(UpdateView):
    model = Continent
    form_class = ContinentForm 
    template_name = 'update_continent.html'
    success_url = reverse_lazy('home')

class ContinentDeleteView(DeleteView):
    model = Continent
    template_name = 'delete_continent.html'
    success_url = reverse_lazy('home')


