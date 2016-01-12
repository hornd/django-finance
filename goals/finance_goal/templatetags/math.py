from django import template

register = template.Library()

def to_percent(value, arg):
    return int((int(value) / int(arg)) * 100)

register.filter('to_percent', to_percent)
