## -*- coding: utf-8 -*-
from django.conf.urls import url
#from django.conf.urls import include
from bitnat import views

urlpatterns = [

    #url(r'^$', views.Inicio.as_view(), name='inicio'),
    #url(r'^gracias/', views.gracias, name='gracias'),
    url(r'^no_gracias/$', views.no_gracias, name='no_gracias'),


    ##zinnia

    #url(r'^blog/', include('zinnia.urls')),

    #url(r'^comments/', include('django_comments.urls')),

]
