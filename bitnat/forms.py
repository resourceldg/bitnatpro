
from django import forms


class Formulario_Contacto(forms.Form):
    fnombre = forms.CharField(max_length=50, required=True, label="nombre",
     widget=(forms.TextInput(attrs={"value": ""})))
    femail = forms.EmailField(max_length=150, required=True, label="email",
    widget=(forms.TextInput(attrs={"value": ""})))
    ftelefono = forms.CharField(max_length=30, required=False, label="telefono",
    widget=(forms.TextInput(attrs={"value": ""})))
    fempresa = forms.CharField(max_length=70, required=False, label="empresa",
    widget=(forms.TextInput(attrs={"value": ""})))
    fmensaje = forms.CharField(max_length=500, required=True, label="mensaje",
    widget=(forms.Textarea(attrs={"value": ""})))
