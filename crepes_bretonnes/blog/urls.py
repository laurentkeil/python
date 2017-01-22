#/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView, ListView
from blog.views import Article, ListeArticles, LireArticle


urlpatterns = patterns('blog.views',
    url(r'^accueil$', 'home'),
    url(r'^art/(?P<id_article>\d+)$', 'view_article', name="afficher_article"),
    url(r'^articles/(?P<month>\d{2})/(?P<year>\d{4})$', 'list_articles'),
    url(r'^redirection$', 'view_redirection'),
    url(r'^date$', 'date_actuelle'),
	url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
    url(r'^$', 'accueil'),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', 'lire'),
    url(r'^article/(?P<pk>\d+)$', LireArticle.as_view(), name='blog_lire'), #2
    url(r'^contact/$', 'contact'),
    url(r'^articleform$', 'articleForm'),
    url(r'^newcontact$', 'nouveau_contact'),
    url(r'^seecontact$', 'voir_contacts'),
    url(r'^faq', TemplateView.as_view(template_name='blog/faq.html')),
    url(r'^a$', ListView.as_view(model=Article,
                    context_object_name="derniers_articles",
                    template_name="blog/accueil.html"
                                )),
    url(r'^liste$', ListeArticles.as_view(), name="blog_liste"),
    url(r'^categorie/(\d+)$', ListeArticles.as_view(), name='blog_categorie'),
 
)