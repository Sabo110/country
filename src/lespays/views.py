from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
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

class ContinentListView(ListView):
    model = Continent
    template_name = "continent_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = ['id', 'name']
        #on definit l'url pour la suppression d'un continent
        context["url_sup"] = 'supcont'
        #on definit l'url pour la modification d'un continent
        context["url_modif"] = 'update_continent'
        #on definit l'url pour la creation d'un continent
        context["url_create"] = 'create_continent'
        return context

class ContinentCreateView(CreateView):
    model = Continent
    form_class = ContinentForm 
    template_name = 'create_continent.html'
    success_url = reverse_lazy('continent_list')

def deleteContinent(request, id):
    try:
        cont = Continent.objects.get(id=id)
        cont.delete()
        messages.success(request, 'Continent supprimé!')
    except Continent.DoesNotExist:
        messages.error(request, "Ce continent a déjà été supprimé!")
    finally:
        return redirect('continent_list')

def updateContinent(request, id):
    try:
        cont = Continent.objects.get(id=id)
        if request.method == 'POST':
            form = ContinentForm(request.POST, instance=cont)
            if form.is_valid():
                form.save()
                messages.success(request, 'Continent modifié!')
                return redirect('continent_list')
    except Continent.DoesNotExist:
        messages.error(request, "Continent introuvale!")

def deleteCountry(request, id):
    try:
        pays = Pays.objects.get(id=id)
        pays.delete()
        messages.success(request, 'Pays supprimé!')
    except Continent.DoesNotExist:
        messages.error(request, "Pays introuvale!")
    finally:
        return redirect('continent_list')
       
class PaysListView(ListView):
    model = Pays
    template_name = "pays_list.html"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = ['id', 'name', 'devise', 'continent']
        #on definit l'url pour la suppression d'un pays
        context["url_sup"] = 'suppays'
        return context



class ContinentUpdateView(UpdateView):
    model = Continent
    form_class = ContinentForm 
    template_name = 'update_continent.html'
    success_url = reverse_lazy('continent_list')

class ContinentDeleteView(DeleteView):
    model = Continent
    template_name = 'delete_continent.html'
    success_url = reverse_lazy('home')


