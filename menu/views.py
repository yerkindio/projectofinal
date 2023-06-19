from django.shortcuts import render,redirect
from .models import Equipo,Tipo,Usuario
from .forms import EquipoForm



# Create your views here.
#-----------------form----------------------#
def listar(request):
    equipos = Equipo.objects.all()
    context={"equipo":equipos}
    return render(request, 'menu/listar.html',context)

def form_agregar(request):
    datos = {
        'form': EquipoForm()
    }
    if request.method == 'POST':
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    tipo = Tipo.objects.all()
    usuario = Usuario.objects.all()
    context = {
        "listatipo": tipo,
        "listausuario": usuario
    }
    return render(request, 'menu/form_agregar.html', context)

def form_modificar(request,id):
    
    equipo = Equipo.objects.get(id_equipo = id)
    tipo = Tipo.objects.all()
    usuario= Usuario.objects.all()

    context = {
        'form': EquipoForm(instance=equipo),
        "datos": equipo,
        "listatipo": tipo,
        "listausuario": usuario
    }
    
    if request.method== 'POST':
        formulario = EquipoForm(data=request.POST,instance=equipo)
        if formulario.is_valid:
            formulario.save()

           
   


    return render(request,'menu/form_modificar.html',context)
#---------------html en general------------------------#


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

def ingresado(request):
    return render (request,'menu/ingresado.html')

def iniciosesion(request):
    return render (request,'menu/iniciosesion.html')

def micuenta(request):
    return render (request,'menu/micuenta.html')

def notebookingresado(request):
    return render (request,'menu/notebookingresado.html')

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

#----------------------agregar/modificar/eliminar------------------------------------#

def agregar(request):
    id_equipoM = request.POST["id_equipo"]
    id_tipoM = request.POST["id_tipo"]
    id_usuarioM = request.POST["id_usuario"]
    descripcionM = request.POST["descripcion"]
    sesionM = request.POST["sesion"]
    cap_discoM = request.POST["cap_disco"]
    ramM = request.POST["ram"]
    placaMM = request.POST["placaM"]
    procesadorM = request.POST["procesador"]
    fuente_poderM = request.POST["fuente_poder"]
    sistema_opM = request.POST["sistema_op"]
    tipo_discM = request.POST["tipo_disc"]
    gpuM = request.POST["gpu"]

    registroTipo = Tipo.objects.get(id_tipo1=id_tipoM)
    registroUsuario = Usuario.objects.get(id_usuario1=id_usuarioM)

    Equipo.objects.create(id_equipo=id_equipoM, id_tipo=registroTipo, id_usuario=registroUsuario, descripcion=descripcionM,
                          sesion=sesionM, cap_disco=cap_discoM, ram=ramM, placaM=placaMM, procesador=procesadorM,
                          fuente_poder=fuente_poderM, sistema_op=sistema_opM, tipo_disc=tipo_discM, gpu=gpuM)
    return redirect('form_agregar')

def modificar(request):
    id_equipoM = request.POST["id_equipo"]
    id_tipoM = request.POST["id_tipo"]
    id_usuarioM = request.POST["id_usuario"]
    descripcionM = request.POST["descripcion"]
    sesionM = request.POST["sesion"]
    cap_discoM = request.POST["cap_disco"]
    ramM = request.POST["ram"]
    placaMM = request.POST["placaM"]
    procesadorM = request.POST["procesador"]
    fuente_poderM = request.POST["fuente_poder"]
    sistema_opM = request.POST["sistema_op"]
    tipo_discM = request.POST["tipo_disc"]
    gpuM = request.POST["gpu"]

    equipo = Equipo.objects.get(id_equipo=id_equipoM)
    equipo.descripcion = descripcionM
    equipo.sesion = sesionM
    equipo.cap_disco = cap_discoM
    equipo.ram = ramM
    equipo.placaM = placaMM
    equipo.procesador = procesadorM
    equipo.fuente_poder = fuente_poderM
    equipo.sistema_op = sistema_opM
    equipo.tipo_disc = tipo_discM
    equipo.gpu = gpuM

    tipo2 = Tipo.objects.get(id_tipo1=id_tipoM)
    equipo.id_tipo = tipo2

    usuario2 = Usuario.objects.get(id_usuario1=id_usuarioM)
    equipo.id_usuario = usuario2

    equipo.save()
    return redirect('listar')

def eliminar(request, id):
    equipo = Equipo.objects.get(id_equipo = id)
    equipo.delete()
    return redirect(to="listar")
