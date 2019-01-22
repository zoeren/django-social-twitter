from django import template

register = template.Library()


@register.filter()
def hello(name):
    """
    """
    return "Hello, %s" % name
