from __future__ import unicode_literals
from django.shortcuts import render, redirect,  get_object_or_404
from Aplicaciones.Control.models import Curso, Horario, HoraEntrada, HoraSalida
from Aplicaciones.Control.forms import HorarioForm,CursoForm#, HoraEntradaForm, CategoriaForm
from django.http import HttpResponse,  Http404, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
import datetime
import time
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from Aplicaciones.Control.utileria import render_pdf



# Create your views here.
def index(request):
    us = User.objects.filter(id=request.user.id)
    if us[0].id == 1:
        context = {'us':us}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
    return render(request, 'index.html')

def Cursos(request):
    cursos = Curso.objects.filter(iduser_id=request.user.id)
    contexto = {'cursos':cursos}
    return render(request, 'cursos.html', contexto)

def HorarioEscuela(request, idcur):
    #categoria = Categoria.objects.filter(iduser_id=request.user.id).first()
    asignatura = get_object_or_404(Curso, id=idcur)
    try:
        asignatura = get_object_or_404(Curso, id=idcur)
        horario = Horario.objects.filter(idcurso_id=idcur)

        #fecha actual
        fecha_actual = time.strftime("%Y/%m/%d")
        fecha_convertida = datetime.datetime.strptime(fecha_actual, '%Y/%m/%d')
        hour_marcada_entrada = HoraEntrada.objects.filter(f_entrada=fecha_actual).filter(idhorario_id=horario[0].id) #objects.last()
        hour_marcada_salida = HoraSalida.objects.filter(id_hora_entrada__in=hour_marcada_entrada)

        contexto = {'horario':horario, 'asignatura':asignatura,'hour_marcada_entrada':hour_marcada_entrada, 'hour_marcada_salida':hour_marcada_salida }
        return render(request, 'horario.html', contexto)
    except IndexError:
        messages.error(request, 'El curso '+asignatura.curso+' no tiene horario establecido, consulte al Administrador o respectiva escuela Profesional.')
        return redirect('Control:Cursos')


def MarcarEntrada(request, idcur, idho):
    try:

        # para la hora de marcaje
        hora_entrada = time.strftime("%H:%M")
        #hora_entrada = datetime.datetime.now()
        date_con = datetime.datetime.strptime(hora_entrada, '%H:%M')

        #Codigo de horario de entrada
        cod_fecha_entrada = time.strftime("%Y/%m/%d")
        cod_entra = datetime.datetime.strptime(cod_fecha_entrada, '%Y/%m/%d')

        b = HoraEntrada(cod_entrada=str(cod_entra)+str(idho),h_entrada=date_con,f_entrada=cod_fecha_entrada,h_entrada_str= hora_entrada, idhorario_id=idho)
        b.save()
        return HttpResponseRedirect(reverse('Control:HorarioEscuela', args={str(idcur)}))
    except IntegrityError as e:
        return HttpResponseRedirect(reverse('Control:HorarioEscuela', args={str(idcur)}))

def MarcarSalida(request, idhe):
    try:

        # maracaje de salida
        hora_salida = time.strftime("%H:%M")
        hora_convertida = datetime.datetime.strptime(hora_salida, '%H:%M')
        hora_enrada = get_object_or_404(HoraEntrada, id=idhe)

        #codigo hora de salida
        cod_fecha_salida = time.strftime("%Y/%m/%d")
        cod_sali = datetime.datetime.strptime(cod_fecha_salida, '%Y/%m/%d')

        b = HoraSalida(cod_salida=str(cod_sali)+str(idhe), h_salida=hora_convertida,f_salida=cod_fecha_salida,h_salida_str=hora_salida,id_hora_entrada_id=idhe )#iduser_id=request.user.id, idcurso_id=idcur)
        b.save()
        return HttpResponseRedirect(reverse('Control:HorarioEscuela', args={str(hora_enrada.idhorario.idcurso.id)}))
    except IntegrityError as e:
        return HttpResponseRedirect(reverse('Control:HorarioEscuela', args={str(hora_enrada.idhorario.idcurso.id)}))


def Asistencia(request):
    asistencia = HoraSalida.objects.filter(id_hora_entrada__idhorario__iduser_id = request.user.id)
    contexto = {'asistencia':asistencia}
    return render(request, 'asistencias.html',contexto)


###apartado del Administrador

def Admin_Cursos(request):
    cursos = Curso.objects.all()
    contexto = {'cursos':cursos}
    return render(request, 'administrador/cursos.html', contexto)

def Admin_Asistencias(request):
    asistencias = HoraSalida.objects.all()
    contexto = {'asistencias':asistencias}
    return render(request, 'administrador/asistencias.html', contexto)

def Admin_User(request):
    user = User.objects.filter(~Q(id = 1))
    contexto = {'user':user}
    return render(request, 'administrador/user.html', contexto)

class AñadirUsuario(CreateView):
    model = User
    template_name = "administrador/registrar_user.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('Control:Admin_User')

def Admin_Horario(request):
    horarios = Horario.objects.all()
    contexto = {'horarios':horarios}
    return render(request, 'administrador/horarios.html', contexto)

def Admin_Horario_Add(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()

            return HttpResponseRedirect(reverse('Control:Admin_Horario'))
    else:
        form = HorarioForm()
    contexto = {'form':form}
    return render(request, 'administrador/add_horarios.html', contexto)

def Admin_Cursos_Add(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('Control:Admin_Cursos')
    else:
        form = CursoForm()
    contexto = {'form':form}
    return render(request, 'administrador/add_cursos.html', contexto)

def Admin_Dar_Baja(request, idu):
    usr = User.objects.filter(id=idu)
    if usr[0].is_active == True:
        User.objects.filter(id=idu).update(is_active=False)
    return HttpResponseRedirect(reverse('Control:Admin_User'))

def Admin_Dar_Alta(request, idu):
    usr = User.objects.filter(id=idu)
    if usr[0].is_active == False:
        User.objects.filter(id=idu).update(is_active=True)
    return HttpResponseRedirect(reverse('Control:Admin_User'))

class PDFPrueba(View):
    def get(self, request, *args, **kwargs):
        asistencias = HoraSalida.objects.all()
        contexto = {'asistencias':asistencias}
        pdf = render_pdf('administrador/reporte.html', contexto)
        return HttpResponse(pdf, content_type="application/pdf")
