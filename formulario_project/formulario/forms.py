from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
