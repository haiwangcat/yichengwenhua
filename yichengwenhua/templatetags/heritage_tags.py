from django import template
from photologue.models import Gallery

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
    print obj.placeholders.__class__.__name__
    for ph in obj.placeholders.all():
        print ph.__unicode__()
        print ph.id
        print ph.get_plugins()
        #print dir(ph.get_plugins)
    print obj.__class__.__name__

@register.simple_tag
def mul(a, b):
    return a * b
 
@register.filter
def hasImages(page):
    galleries = Gallery.objects.filter(title_slug = page.get_slug())
    if galleries.count() == 0:
        return False
    return True
    
@register.filter
def hasVideos(page):
    for ph in page.placeholders.all():
        if ph.slot == "heritage-video":
            if ph.get_plugins().count() == 0:
                return False
    return True