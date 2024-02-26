from django import template

register = template.Library()

@register.simple_tag
def get_attr(obj, attr):
    return getattr(obj, attr)
