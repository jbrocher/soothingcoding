from django import template
register = template.Library()


@register.inclusion_tag('main/blocks/b-header.html')
def header(title):
    return {'title': title}


@register.inclusion_tag('main/blocks/b-section-title.html')
def section_title(modifier, title):
    return {'title': title, "modifier": modifier}


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


@register.inclusion_tag('main/blocks/b-cta.html')
def cta(text, modifier, link):
    return {'text': text, 'modifier': modifier, 'link': link}


@register.inclusion_tag('main/blocks/b-button.html')
def button(text, modifiers):
    return {'text': text, 'modifiers': modifiers}


@register.inclusion_tag('main/blocks/b-value-service.html')
def value_service(icon, title, text):
    return {
        'icon': icon,
        'title': title,
        'text': text
    }
