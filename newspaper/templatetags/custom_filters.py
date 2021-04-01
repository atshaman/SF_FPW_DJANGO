from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    return str(value).replace('черт!', 'упс!')