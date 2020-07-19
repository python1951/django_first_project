from django import template
register = template.Library()
@register.filter('cut')
#we can also use decorators
def cut(value,arg):
    return value.replace(aarg,"")

#register.filter('cut',cut)
