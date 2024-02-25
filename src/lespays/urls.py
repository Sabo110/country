from django.urls import path
from .views import home, ContinentCreateView, ContinentUpdateView, ContinentDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('create_continent/', ContinentCreateView.as_view(), name="create_continent"),
    path('update_continent/<int:pk>', ContinentUpdateView.as_view(), name="update_continent"),
    path('delete_continent/<int:pk>', ContinentDeleteView.as_view(), name="delete_continent"),
]
