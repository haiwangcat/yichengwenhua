from django import template

register = template.Library()


@register.simple_tag
def trasform_text(text):
    return text