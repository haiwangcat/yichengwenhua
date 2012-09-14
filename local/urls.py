# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from photologue.models import Gallery

handler500 = 'djangotoolbox.errorviews.server_error'

admin.autodiscover()


from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response

def getImages(request, slug):
    if request.is_ajax():
        galleries = Gallery.objects.filter(title_slug = slug)
        if galleries.count() == 0:
            return HttpResponse('<p>很抱歉，目前没有相关图片。</p>')
        return render_to_response('show-images.html', {'album': galleries[0]})
    else:
        return HttpResponse('<p>很抱歉，目前没有相关图片。</p>')
    
    

urlpatterns = patterns('',
    (r'.*/(?P<slug>[\-\d\w]+)/get_images/?$', getImages),
    #url(r'.*/(?P<slug>[\-\d\w]+)/get_images$', 'django.views.generic.list_detail.object_detail', {'slug_field': 'title_slug', 'queryset': Gallery.objects.filter(is_public=True), 'template_name': 'show-images.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')), 
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
