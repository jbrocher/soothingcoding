from django import template
register = template.Library()


@register.inclusion_tag('main/blocks/b-header.html')
def header():
    pass
