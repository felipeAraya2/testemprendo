"""Intranet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index,login, cerrar_sesion,busqueda_asig, actualizar_asig, asignatura,eliminar_video

urlpatterns = [
    path('',index,name='INDEX'),
    path('asignatura', asignatura, name='ASIG'),
    path('login', login, name='LOGIN'),
    path('cerrar_sesion',cerrar_sesion, name='LOGOUT'),
    path('buscar/<id>/',busqueda_asig,name='BUSCAR'),
    path('modificar',actualizar_asig,name='MOD'),
    path('eliminar-video/<id>/',eliminar_video, name='ELIMINAR')


    

]
