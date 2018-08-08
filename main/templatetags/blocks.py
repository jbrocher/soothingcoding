from django import template
register = template.Library()


@register.inclusion_tag('main/blocks/b-header.html')
def header(title):
    return {'title': title}


@register.inclusion_tag('main/blocks/b-section-title.html')
def section_title(title):
    return {'title': title}


@register.inclusion_tag('main/blocks/b-card-icon.html')
def card_icon(icon, title, text):
    return {'icon': icon, 'title': title, 'text': text}
