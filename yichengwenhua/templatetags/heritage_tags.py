from django import template

register = template.Library()


@register.simple_tag
def getTopPos(size, index):
    print dir(size)
    return index / 4 * size[1]
    
@register.simple_tag
def getLeftPos(size, index):
    print dir(size)
    return index % 4 * size[0]
    
@register.simple_tag
def showClassInfo(obj):
    print obj.placeholders.all()
    print obj.__class__.__name__