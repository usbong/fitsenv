# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('fitsapp.upload.views',
    url(r'^search/', 'upload_search', name='upload_search'),
    url(r'^$', 'upload', name='upload'),
)