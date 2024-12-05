from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import MiFormulario

def index(request):
    if request.method == 'POST':
        form = MiFormulario(request.POST)
        if form.is_valid():
            # Aquí puedes manejar los datos del formulario
            return HttpResponse("Formulario enviado correctamente")
    else:
        form = MiFormulario()

    return render(request, 'formulario/index.html', {'form': form})
