from django import template
from django.contrib.auth.models import Group


register = template.Library()

@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None



@register.filter
def add(x, y):
    try:
        return x + y
    except:
        return None
