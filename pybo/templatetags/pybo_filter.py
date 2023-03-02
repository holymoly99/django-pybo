import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def mark(value):
    extension = ['nl2br', 'fenced_code']
    return mark_safe(markdown.markdown(value, extensions=extension))

@register.simple_tag()
def avarta(uid):
    tag = f'<img class="avarta" src="https://randomuser.me/api/portraits/men/{uid}.jpg"/>'
    return mark_safe(tag)


# {% avarta user.id %}
