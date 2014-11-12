from django import template

register = template.Library()

@register.filter(name='minus')
def minus(value, arg):
    """Subtracts the value of arg from the givin integer"""
    return value - arg
