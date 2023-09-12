from django import template

register = template.Library()


@register.filter
def convert_empty_string(value):
    if not value:
        return '   /'
    return value
