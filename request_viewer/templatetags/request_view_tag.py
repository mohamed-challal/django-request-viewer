from django import template
import json

register = template.Library()

@register.filter('startswith')
def startswith(text, starts):
    texts = str(starts).split(',')
    return any([str(text).startswith(tx) for tx in texts])


@register.filter('to_json')
def to_json(ls_string):
    return json.dumps(ls_string)

