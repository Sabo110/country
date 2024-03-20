from django.db import models

class Salle(models.Model):
    nom = models.CharField(max_length=255, null=False, blank=False)
    specialite = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.specialite

class Etudiant(models.Model):
    nom = models.CharField(max_length=255, null=False, blank=False)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    date_naissance = models.DateField(null=False, blank=False)
    lieu = models.CharField(max_length=255, null=False, blank=False)
    salle = models.ForeignKey(Salle, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nom