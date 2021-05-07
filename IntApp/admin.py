from django.contrib import admin
from .models import Video, Curso, Asignatura

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display=['video','nombre','asignatura']

class CursoAdmin(admin.ModelAdmin):
    list_display=['nombre']

class AsignaturaAdmin(admin.ModelAdmin):
    list_display=['nombre','curso','profesor']


admin.site.register(Video, VideoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
