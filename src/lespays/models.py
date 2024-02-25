from django.db import models

# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=50)

class Pays(models.Model):
    name = models.CharField(max_length=50)
    superficie = models.DecimalField(max_digits=5, decimal_places=2)
    population = models.IntegerField()
    devise = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.DO_NOTHING, related_name='pays')
    


