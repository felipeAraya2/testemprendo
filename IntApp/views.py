from django.shortcuts import render
from .models import Video, Asignatura, Curso
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login as login_aut
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

# Create 

def login(request):
    if request.POST:
        usuario = request.POST.get('txtUsuario')
        password = request.POST.get('password')
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_aut(request,us)
            if request.user.is_superuser:
                user=request.user
                boxasignatura = Asignatura.objects.all()
                vervideo = Video.objects.all()
                boxcurso = Curso.objects.all()
                usuario = User.objects.all()

                return render(request,'web/index.html',{'user':user,'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'usuario':usuario})
            
            current_user=request.user
            boxasignatura = Asignatura.objects.filter(profesor = current_user.id)
            vervideo = Video.objects.filter(asignatura__profesor__id = current_user.id )                
            boxcurso = Curso.objects.all()     
            return render(request,'web/index.html',{'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura})     
        else:
            return render (request, 'web/login.html',{'msg':'usuario o contraseña no coinciden con ninguna cuenta'})
    return render (request, 'web/login.html')

@login_required(login_url='/login')
def index(request):
    if request.user.is_superuser:
        boxasignatura = Asignatura.objects.all()
        vervideo = Video.objects.all()
        boxcurso = Curso.objects.all()
        usuario = User.objects.all()
        if request.POST:
            linkvideo = request.POST.get('txtlink').replace('https://youtu.be/','https://www.youtube.com/embed/')
            nombrevideo= request.POST.get('txtnombre')
            asignatura = request.POST.get('asig')
            videonuevo = Video(
                nombre=nombrevideo,
                video=linkvideo,
                asignatura=Asignatura.objects.get(nombre=asignatura))

            videonuevo.save()
            return render (request,'web/index.html',{'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'usuario':usuario})
        return render (request,'web/index.html',{'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura, 'usuario':usuario})


    current_user=request.user
    boxasignatura = Asignatura.objects.filter(profesor = current_user.id)
    vervideo = Video.objects.filter(asignatura__profesor__id = current_user.id )
    boxcurso = Curso.objects.all()

    if request.POST:
        linkvideo = request.POST.get('txtlink').replace('https://youtu.be/','https://www.youtube.com/embed/')
        nombrevideo= request.POST.get('txtnombre')
        asignatura = request.POST.get('asig')
        videonuevo = Video(
            nombre=nombrevideo,
            video=linkvideo,
            asignatura=Asignatura.objects.get(nombre=asignatura))

        videonuevo.save()
    
        return render (request,'web/index.html',{'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura})

    return render (request,'web/index.html',{'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura})

def actualizar_asig(request):
    boxasignatura = Asignatura.objects.all()
    vervideo = Video.objects.all()
    boxcurso = Curso.objects.all()
    if request.POST:
        nombre = request.POST.get('nombre')
        profesor = User.objects.get(username = request.POST.get('profesor') ) 
        
        asignatura= Asignatura.objects.get(nombre=nombre)
        asignatura.profesor = profesor
        asignatura.save()
    return render (request,'web/index.html',{'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura})


def busqueda_asig(request,id):
    user = User.objects.all()
    asignatura = Asignatura.objects.get(nombre = id)
    return render(request,'web/asignatura.html',{'asignatura':asignatura, 'user':user})

def cerrar_sesion(request):
    logout(request)
    return render(request,'web/login.html')         
