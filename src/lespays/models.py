from django.db import models

# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
    def get_class_name(self):
        return self.__class__.__name__
    

class Pays(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    superficie = models.FloatField(null=False, blank=False)
    population = models.IntegerField(null=False, blank=False)
    devise = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.DO_NOTHING, related_name='pays', null=True)
    


