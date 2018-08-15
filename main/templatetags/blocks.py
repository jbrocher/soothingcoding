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


@register.inclusion_tag('main/blocks/b-subtitle.html')
def subtitle(text):
    return {'text': text}


@register.inclusion_tag('main/blocks/b-step.html')
def step(step, icon, title, text, color):
    return {
        'step': step,
        'text': text,
        'title': title,
        'icon': icon,
        'color': color
        }
