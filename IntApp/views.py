from django.shortcuts import render
from .models import Video, Asignatura, Curso
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login as login_aut
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

# Create 
from datetime import datetime

def saludo():
    currentTime = datetime.now()
    currentTime.hour

    if 6<= currentTime.hour < 12:
        msgS= "Buenos días "
    elif 12 <= currentTime.hour < 20:
        msgS= "Buenas tardes "
    else:
        msgS= "Buenas noches "
    return msgS

def login(request):
    if request.POST:
        usuario = request.POST.get('txtUsuario')
        password = request.POST.get('password')
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_aut(request,us)
            if request.user.is_superuser:
                current_user=request.user
                boxasignatura = Asignatura.objects.all()
                vervideo = Video.objects.all()
                boxcurso = Curso.objects.all()
                usuario = User.objects.all()

                return render(request,'web/index.html',{'msg':saludo(),'current_user':current_user,'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'usuario':usuario})
            
            current_user=request.user
            boxasignatura = Asignatura.objects.filter(profesor = current_user.id)
            vervideo = Video.objects.filter(asignatura__profesor__id = current_user.id )                
            boxcurso = Curso.objects.all()     
            return render(request,'web/index.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura, 'current_user':current_user})     
        else:
            return render (request, 'web/login.html',{'msg':'usuario o contraseña no coinciden con ninguna cuenta'})
    return render (request, 'web/login.html')

@login_required(login_url='/login')
def index(request):
    if request.user.is_superuser:
        current_user=request.user
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
            return render (request,'web/index.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'usuario':usuario, 'current_user':current_user})
        return render (request,'web/index.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura, 'usuario':usuario,'current_user':current_user})


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
    
        return render (request,'web/index.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'current_user':current_user})

    return render (request,'web/index.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'current_user':current_user})

def eliminar_video(request,id):
    current_user=request.user
    if request.user.is_superuser:
        boxasignatura = Asignatura.objects.all()
        vervideo = Video.objects.all()
        boxcurso = Curso.objects.all()
        try:
            videoElim = Video.objects.get(nombre=id)
            videoElim.delete()
            msgE='eliminó video'
        except:
            msgE='no eliminó video'
            return render (request,'web/index.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'current_user':current_user, 'msgE':msgE})
        return render (request,'web/index.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'current_user':current_user, 'msgE':msgE})

    boxasignatura = Asignatura.objects.filter(profesor = current_user.id)
    vervideo = Video.objects.filter(asignatura__profesor__id = current_user.id )
    boxcurso = Curso.objects.all()
    try:
        videoElim = Video.objects.get(nombre=id)
        videoElim.delete()
        msgE='eliminó video'
    except:
        msgE='no eliminó video'
        return render (request,'web/index.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'current_user':current_user, 'msgE':msgE})
  
    return render (request,'web/index.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'current_user':current_user, 'msgE':msgE})


def asignatura (request):
    if request.user.is_superuser:
        current_user=request.user
        boxasignatura = Asignatura.objects.all()
        usuario = User.objects.all()
        return render (request,'web/asignatura.html',{'msg':saludo(), 'asignatura':boxasignatura,'usuario':usuario,'current_user':current_user})
    return render (request,'web/403.html')


@login_required(login_url='/login')
def actualizar_asig(request):
        current_user=request.user
        boxasignatura = Asignatura.objects.all()
        vervideo = Video.objects.all()
        boxcurso = Curso.objects.all()
        if request.POST:
            nombre = request.POST.get('nombre')
            profesor = User.objects.get(username = request.POST.get('profesor') ) 
        
            asignatura= Asignatura.objects.get(nombre=nombre)
            asignatura.profesor = profesor
            asignatura.save()
        return render (request,'web/asignatura.html',{'msg':saludo(),'mostrarvideo':vervideo, 'curso':boxcurso, 'asignatura':boxasignatura,'current_user':current_user})

@login_required(login_url='/login')
def busqueda_asig(request,id):
    if request.user.is_superuser:
        current_user=request.user
        user = User.objects.all()
        asignatura = Asignatura.objects.get(nombre = id)
        return render(request,'web/asignatura-mod.html',{'msg':saludo(),'asignatura':asignatura, 'user':user,'current_user':current_user})
    return render (request,'web/403.html')



@login_required(login_url='/login')

def cerrar_sesion(request):
    logout(request)
    return render(request,'web/login.html')         
