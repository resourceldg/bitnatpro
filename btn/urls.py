# -*- coding: utf-8 -*-
"""bn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# de django
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


# nuestras
from bitnat import views

# de terceros
from django.contrib.sitemaps.views import index
from django.contrib.sitemaps.views import sitemap
from zinnia.sitemaps import AuthorSitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import TagSitemap


sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns = [
    #sitemap

    url(r'^sitemap.xml$',
        index,
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    #bitnativo.com

    
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^contact/$', views.Contact.as_view(), name='Contact'),
    url(r'^sitemap/$', views.sitemap, name='sitemap'),
    url(r'^robots.txt/$', views.robots, name='robots'),
    url(r'^contact/gracias/$', views.gracias, name='gracias'),
    url(r'^ventas-en-redes-sociales/gracias/$', views.gracias, name='gracias'),#dry(dont repeat yourself): me estoy repitiendo (SOLUCION: APRENDER A USAR REGEX EN PATRONES URL)
    url(r'^negocios-digitales/gracias/$', views.gracias, name='gracias'),#dry(dont repeat yourself): me estoy repitiendo (SOLUCION: APRENDER A USAR REGEX EN PATRONES URL)
    url(r'^analitica-web/gracias/$', views.gracias, name='gracias'),#dry(dont repeat yourself): me estoy repitiendo (SOLUCION: APRENDER A USAR REGEX EN PATRONES URL)
    url(r'^marketing-de-contenidos/gracias/$', views.gracias, name='gracias'),#dry(dont repeat yourself): me estoy repitiendo (SOLUCION: APRENDER A USAR REGEX EN PATRONES URL)
    url(r'^posicionamiento-web/gracias/$', views.gracias, name='gracias'),#dry(dont repeat yourself): me estoy repitiendo (SOLUCION: APRENDER A USAR REGEX EN PATRONES URL)
    url(r'^email-marketing/gracias/$', views.gracias, name='gracias'),#dry(dont repeat yourself): me estoy repitiendo (SOLUCION: APRENDER A USAR REGEX EN PATRONES URL)
    url(r'^asesoria-gratuita-en-marketing-digital/gracias/$', views.gracias, name='gracias'),#dry(dont repeat yourself): me estoy repitiendo (SOLUCION: APRENDER A USAR REGEX EN PATRONES URL)
#LANDING PAGES
    url(r'^ventas-en-redes-sociales/$', views.Social_lp.as_view(), name='ventas-en-redes-sociales'),
    url(r'^negocios-digitales/$', views.Negocio_lp.as_view(), name='negocios-digitales'),
    url(r'^analitica-web/$', views.Analytics_lp.as_view(), name='analitica-web'),
    url(r'^marketing-de-contenidos/$', views.Contenido_lp.as_view(), name='marketing-de-contenidos'),
    url(r'^posicionamiento-web/$', views.Posicionamiento_web.as_view(), name='posicionamiento-web'),
    url(r'^email-marketing/$', views.Emailmkt_lp.as_view(), name='email-marketing'),
    url(r'^asesoria-gratuita-en-marketing-digital/$', views.Ctalider_lp.as_view(), name='asesoria-gratuita-en-marketing-digital'),
#FIN LANDING PAGES



    #zinnia

    url(r'^blog/', include('zinnia.urls')),

    url(r'^comments/', include('django_comments.urls')),

]

if settings.DEBUG==False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

