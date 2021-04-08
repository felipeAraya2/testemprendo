from django.shortcuts import render
from .models import Video

# Create 
def index(request):
    vervideo = Video.objects.all()
    if request.POST:
        linkvideo = request.POST.get('txtlink').replace('https://youtu.be/','https://www.youtube.com/embed/')
        videonuevo = Video(video=linkvideo)
        videonuevo.save()
    
        return render (request,'web/index.html',{'mostrarvideo':vervideo})

    return render (request,'web/index.html',{'mostrarvideo':vervideo})

