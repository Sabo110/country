from django import template

register = template.Library()

@register.filter
def class_name(liste):
    if len(liste) > 0:
        instance_type = liste[0].__class__.__name__
        return instance_type