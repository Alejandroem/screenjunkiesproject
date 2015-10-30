from django.shortcuts import render,HttpResponse
from screenjunkies.forms import *


# Create your views here.
def registrarse(request):

    if request.method =="POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse('<h1>Usuario Creado</h1>')
        else:
            return render(request, "Usuario/registrarse.html",{'form':form})
    else:
        form = UsuarioForm()

    return render(request, "Usuario/registrarse.html",{'form':form})

def vincular(request):
    if request.method =="POST":
        form = VinculoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Vinculo Creado</h1>')
        else:
            return render(request, "Usuario/vincular.html",{'form':form})
    else:
        form = VinculoForm()

    return render(request, "Usuario/vincular.html",{'form':form})