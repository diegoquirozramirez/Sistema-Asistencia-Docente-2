from django.contrib import admin
from Aplicaciones.Control.models import Ciclo, Curso, Categoria, Horario, HoraEntrada, HoraSalida
# Register your models here.
admin.site.register(Ciclo)
admin.site.register(Curso)
admin.site.register(Categoria)
admin.site.register(Horario)
admin.site.register(HoraEntrada)
admin.site.register(HoraSalida)
