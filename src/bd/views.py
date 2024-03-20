from rest_framework import viewsets

from .models import Salle, Etudiant
from .serializers import SalleSerializer, EtudiantSerializer

class SalleViewset(viewsets.ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer

class EtudiantViewset(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer