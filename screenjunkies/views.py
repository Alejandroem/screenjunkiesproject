from django.shortcuts import render


# Create your views here.
def registrarse(request):
    return render(request, "Usuario/registrarse.html")