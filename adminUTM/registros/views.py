from django.shortcuts import render
from .forms import ComentarioContactoForm
from .forms import RegistroSolicitudesForm
from .models import RegistroSolicitudes
from django.shortcuts import get_object_or_404

# Create your views here.

def contacto(request):
    return render(request,"registros/contacto.html")

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"registros/contacto.html")
    form = ComentarioContactoForm()
    return render(request,"registros/contacto.html",{"form":form})


def solicitud(request):
    return render(request,"registros/registrarSolicitud.html")

def registrarSolicitud(request):
    if request.method == 'POST':
        form = RegistroSolicitudesForm(request.POST)
        if form.is_valid():
            form.save()
            solicitudes=RegistroSolicitudes.objects.all()
            return render(request,"registros/consultaSolicitud.html",{"solicitudes":solicitudes})
    form = RegistroSolicitudesForm()
    return render(request,"registros/registrarSolicitud.html",{"form":form})

def consultarSolicitud(request):
    solicitudes=RegistroSolicitudes.objects.all()
    return render(request,"registros/consultaSolicitud.html",{"solicitudes":solicitudes})

def eliminarSolicitud(request, id, confirmacion="registros/confirmarEliminacion.html"):
    solicitud = get_object_or_404(RegistroSolicitudes, id=id)
    if request.method=="POST":
        solicitud.delete()
        solicitudes=RegistroSolicitudes.objects.all()
        return render(request,"registros/consultaSolicitud.html",{"solicitudes":solicitudes})
    return render(request, confirmacion, {"object":solicitud})

def consultarSolicitudIndividual(request, id):
    solicitud = RegistroSolicitudes.objects.get(id=id)
    return render(request,"registros/formEditarSolicitud.html",{"solicitud":solicitud})

def editarSolicitud(request, id):
    solicitud = get_object_or_404(RegistroSolicitudes, id=id)
    form = RegistroSolicitudesForm(request.POST, instance=solicitud)
    if form.is_valid():
        form.save()
        solicitudes=RegistroSolicitudes.objects.all()
        return render(request,"registros/consultaSolicitud.html",{"solicitudes":solicitudes})
    return render(request,"registros/formEditarSolicitud.html",{"solicitud":solicitud})
