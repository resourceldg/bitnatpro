# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import Formulario_Contacto

from .models import Contacto


def inicio(request):
    return render(request, 'inicio.html')



class Contact(View):

    form_class = Formulario_Contacto
    initial = {'key': 'value'}
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                datos = form.cleaned_data
                fnombre = datos.get("fnombre")
                femail = datos.get("femail")
                ftelefono = datos.get("ftelefono")
                fempresa = datos.get("fempresa")
                fmensaje = datos.get("fmensaje")
                db_register = Contacto(nombre=fnombre, email=femail,telefono=ftelefono,empresa=fempresa,mensaje=fmensaje)
                db_register.save()
                return HttpResponseRedirect('gracias', {'form': form})

        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})


def gracias(request):
    return render(request, 'gracias.html')

def sitemap(request):
    return render(request, 'sitemap.xml')

def robots(request):
    return render(request, 'robots.txt')

#dry(dont repeat yourself): me estoy repitiendo grrrr.(SOLUCIONAR LAS SIGUIENTE VISTAS GENERERICAS)
#APRENDER A USAR DECORADORES, MIXINS HERENCIAS DE VISTAS GENERICAS Y DE MODELOS

class Social_lp(View):
    form_class = Formulario_Contacto
    initial = {'key': 'value'}
    template_name = 'ventas-en-redes-sociales.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                datos = form.cleaned_data
                fnombre = datos.get("fnombre")
                femail = datos.get("femail")
                ftelefono = datos.get("ftelefono")
                fempresa = datos.get("fempresa")
                fmensaje = datos.get("fmensaje")
                db_register = Contacto(nombre=fnombre, email=femail,telefono=ftelefono,empresa=fempresa,mensaje=fmensaje)
                db_register.save()
                body = render_to_string(
                       'email_content.html', {
                            'fnombre': fnombre,
                            'fmensaje': fmensaje,
                            'femail': femail,
                            },
                        )
                email_message = EmailMessage(
                    subject='mensaje de usuario',
                    body=body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                )
                email_message.content_subtype = 'html'
                email_message.send()
                return HttpResponseRedirect('gracias', {'form': form})

        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})


class Negocio_lp(View):
    form_class = Formulario_Contacto
    initial = {'key': 'value'}
    template_name = 'negocios-digitales.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                datos = form.cleaned_data
                fnombre = datos.get("fnombre")
                femail = datos.get("femail")
                ftelefono = datos.get("ftelefono")
                fempresa = datos.get("fempresa")
                fmensaje = datos.get("fmensaje")
                db_register = Contacto(nombre=fnombre, email=femail,telefono=ftelefono,empresa=fempresa,mensaje=fmensaje)
                db_register.save()
                body = render_to_string(
                       'email_content.html', {
                            'fnombre': fnombre,
                            'fmensaje': fmensaje,
                            'femail': femail,
                            },
                        )
                email_message = EmailMessage(
                    subject='mensaje de usuario',
                    body=body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                )
                email_message.content_subtype = 'html'
                email_message.send()
                return HttpResponseRedirect('gracias', {'form': form})

        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})


class Analytics_lp(View):
    form_class = Formulario_Contacto
    initial = {'key': 'value'}
    template_name = 'analitica-web.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                datos = form.cleaned_data
                fnombre = datos.get("fnombre")
                femail = datos.get("femail")
                ftelefono = datos.get("ftelefono")
                fempresa = datos.get("fempresa")
                fmensaje = datos.get("fmensaje")
                db_register = Contacto(nombre=fnombre, email=femail,telefono=ftelefono,empresa=fempresa,mensaje=fmensaje)
                db_register.save()
                body = render_to_string(
                       'email_content.html', {
                            'fnombre': fnombre,
                            'fmensaje': fmensaje,
                            'femail': femail,
                            },
                        )
                email_message = EmailMessage(
                    subject='mensaje de usuario',
                    body=body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                )
                email_message.content_subtype = 'html'
                email_message.send()
                return HttpResponseRedirect('gracias', {'form': form})

        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})



class Contenido_lp(View):
    form_class = Formulario_Contacto
    initial = {'key': 'value'}
    template_name = 'marketing-de-contenidos.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                datos = form.cleaned_data
                fnombre = datos.get("fnombre")
                femail = datos.get("femail")
                ftelefono = datos.get("ftelefono")
                fempresa = datos.get("fempresa")
                fmensaje = datos.get("fmensaje")
                db_register = Contacto(nombre=fnombre, email=femail,telefono=ftelefono,empresa=fempresa,mensaje=fmensaje)
                db_register.save()
                body = render_to_string(
                       'email_content.html', {
                            'fnombre': fnombre,
                            'fmensaje': fmensaje,
                            'femail': femail,
                            },
                        )
                email_message = EmailMessage(
                    subject='mensaje de usuario',
                    body=body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                )
                email_message.content_subtype = 'html'
                email_message.send()
                return HttpResponseRedirect('gracias', {'form': form})

        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})



class Posicionamiento_web(View):
    form_class = Formulario_Contacto
    initial = {'key': 'value'}
    template_name = 'posicionamiento-web.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                datos = form.cleaned_data
                fnombre = datos.get("fnombre")
                femail = datos.get("femail")
                ftelefono = datos.get("ftelefono")
                fempresa = datos.get("fempresa")
                fmensaje = datos.get("fmensaje")
                db_register = Contacto(nombre=fnombre, email=femail,telefono=ftelefono,empresa=fempresa,mensaje=fmensaje)
                db_register.save()
                body = render_to_string(
                       'email_content.html', {
                            'fnombre': fnombre,
                            'fmensaje': fmensaje,
                            'femail': femail,
                            },
                        )
                email_message = EmailMessage(
                    subject='mensaje de usuario',
                    body=body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                )
                email_message.content_subtype = 'html'
                email_message.send()
                return HttpResponseRedirect('gracias', {'form': form})

        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})



class Emailmkt_lp(View):
    form_class = Formulario_Contacto
    initial = {'key': 'value'}
    template_name = 'emailmkt_lp.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                datos = form.cleaned_data
                fnombre = datos.get("fnombre")
                femail = datos.get("femail")
                ftelefono = datos.get("ftelefono")
                fempresa = datos.get("fempresa")
                fmensaje = datos.get("fmensaje")
                db_register = Contacto(nombre=fnombre, email=femail,telefono=ftelefono,empresa=fempresa,mensaje=fmensaje)
                db_register.save()
                body = render_to_string(
                       'email_content.html', {
                            'fnombre': fnombre,
                            'fmensaje': fmensaje,
                            'femail': femail,
                            },
                        )
                email_message = EmailMessage(
                    subject='mensaje de usuario',
                    body=body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                )
                email_message.content_subtype = 'html'
                email_message.send()
                return HttpResponseRedirect('gracias', {'form': form})

        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})



class Ctalider_lp(View):
    form_class = Formulario_Contacto
    initial = {'key': 'value'}
    template_name = 'ctalider_lp.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                datos = form.cleaned_data
                fnombre = datos.get("fnombre")
                femail = datos.get("femail")
                ftelefono = datos.get("ftelefono")
                fempresa = datos.get("fempresa")
                fmensaje = datos.get("fmensaje")
                db_register = Contacto(nombre=fnombre, email=femail,telefono=ftelefono,empresa=fempresa,mensaje=fmensaje)
                db_register.save()
                body = render_to_string(
                       'email_content.html', {
                            'fnombre': fnombre,
                            'fmensaje': fmensaje,
                            'femail': femail,
                            },
                        )
                email_message = EmailMessage(
                    subject='mensaje de usuario',
                    body=body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                )
                email_message.content_subtype = 'html'
                email_message.send()
                return HttpResponseRedirect('gracias', {'form': form})

        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})






