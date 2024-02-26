from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name='home'),
    path('continent_list/', ContinentListView.as_view(), name="continent_list"),
    path('create_continent/', ContinentCreateView.as_view(), name="create_continent"),
    path('update_continent/<int:pk>', ContinentUpdateView.as_view(), name="update_continent"),
    path('supcont/<int:id>', deleteContinent, name="supcont"),
    path('pays_list/', PaysListView.as_view(), name="pays_list"),
    path('create_pays/', PaysCreateView.as_view(), name="create_pays"),
    path('update_pays/<int:pk>', PaysUpdateView.as_view(), name="update_pays"),
    path('suppays/<int:id>', deletePays, name="suppays"),
]
