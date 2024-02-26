from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import UpdateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import *
from .forms import ContinentForm, PaysForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

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

    def form_valid(self, form):
        messages.success(self.request, "Création réalisée avec succès!")
        return super().form_valid(form)


class ContinentUpdateView(UpdateView):
    model = Continent
    form_class = ContinentForm 
    template_name = 'update_continent.html'
    success_url = reverse_lazy('continent_list')

    def form_valid(self, form):
        messages.success(self.request, "Modification réalisée avec succès!")
        return super().form_valid(form)


def deleteContinent(request, id):
    try:
        cont = Continent.objects.get(id=id)
        cont.delete()
        messages.success(request, 'Suppression réalisée avec succès!')
    except Continent.DoesNotExist:
        messages.error(request, "Ce continent a déjà été supprimé!")
    finally:
        return redirect('continent_list')
       
class PaysListView(ListView):
    model = Pays
    template_name = "pays_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = ['id', 'name', 'devise', 'continent']
        #on definit l'url pour la suppression d'un pays
        context["url_sup"] = 'suppays'
        context["url_modif"] = 'update_pays'
        #on definit l'url pour la creation d'un continent
        context["url_create"] = 'create_pays'
        return context

class PaysCreateView(CreateView):
    model = Pays
    template_name = 'create_pays.html'
    form_class = PaysForm
    success_url = reverse_lazy('pays_list')

    def form_valid(self, form):
        messages.success(self.request, "Création réalisée avec succès!")
        return super().form_valid(form)

class PaysUpdateView(UpdateView):
    model = Pays
    template_name = 'update_pays.html'
    form_class = PaysForm
    success_url = reverse_lazy('pays_list')

    def form_valid(self, form):
        messages.success(self.request, "Modification réalisée avec succès!")
        return super().form_valid(form)

def deletePays(request, id):
    try:
        pays = Pays.objects.get(id=id)
        pays.delete()
        messages.success(request, 'Suppression réalisée avec succès!')
    except Continent.DoesNotExist:
        messages.error(request, "Ce pays a déjà été supprimé!")
    finally:
        return redirect('pays_list')






