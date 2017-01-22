#/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from views import URLCreate, URLUpdate, URLDelete

urlpatterns = patterns('mini_url.views',
    url(r'^$', 'liste', name='url_liste'),  # Une string vide indique la racine
    #url(r'^nouveau$', 'nouveau', name='url_nouveau'),
    url(r'^nouveau$', URLCreate.as_view(), name='url_nouveau'),
	url(r'^edition/(?P<code>\w{6})$', URLUpdate.as_view(), name='url_update'),
	url(r'^supprimer/(?P<code>\w{6})$', URLDelete.as_view(), name='url_delete'),
    url(r'^(?P<code>\w{6})/$', 'redirection', name='url_redirection'),
)