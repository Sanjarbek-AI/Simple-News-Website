from django import template

register = template.Library()


@register.filter
def one_cut(title):
    return title[:40]

