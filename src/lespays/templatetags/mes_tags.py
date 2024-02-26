from django import template

from lespays.models import Continent, Pays
register = template.Library()

@register.filter
def class_name(liste):
    if len(liste) > 0:
        instance_type = liste[0].__class__.__name__
        return instance_type

@register.simple_tag
def nb_continent():
    return Continent.objects.all().count()

@register.simple_tag
def nb_pays():
    return Pays.objects.all().count()
