from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'menu/inicio.html')

def clientes(request):
    return render(request,'menu/clientes.html')

def contacto(request):
    return render(request,'menu/contacto.html')

def contactoingresado(request):
    return render(request,'menu/contactoingresado.html')

def crearcuenta(request):
    return render(request,'menu/crearcuenta.html')

def index(request):
    return render(request,'menu/index.html')

def ingresado(request):
    return render (request,'menu/ingresado.html')

def iniciosesion(request):
    return render (request,'menu/iniciosesion.html')

def micuenta(request):
    return render (request,'menu/micuenta.html')

def notebookingresado(request):
    return render (request,'menu/notebooks.html')

def notebooks (request):
    return render (request,'menu/notebooks.html')

def pc (request):
    return render (request,'menu/pc.html')

def pcingresado(request):
    return render (request,'menu/pcingresado.html')

def Perfil(request):
    return render(request,'menu/Perfil.html')

def recuperarcontra(request):
    return render(request,'menu/recuperarcontra.html')

def reparaciones(request):
    return render(request,'menu/reparaciones.html')

def reparacioningresado(request):
    return render(request,'menu/reparacioningresado.html')
