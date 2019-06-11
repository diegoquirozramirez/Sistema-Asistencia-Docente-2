from Aplicaciones.Control.views import PDFPrueba, Admin_Dar_Alta,Admin_Dar_Baja,Admin_Cursos_Add,Admin_Horario_Add,Admin_Horario,AñadirUsuario, index, Cursos, HorarioEscuela, MarcarEntrada, MarcarSalida,Asistencia,Admin_Cursos, Admin_Asistencias, Admin_User
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name = "Control"
urlpatterns = [
    path('', login_required(index), name="index"),
    path('Cursos', login_required(Cursos), name="Cursos"),
    path('Cursos/HorarioEscuela/<idcur>', login_required(HorarioEscuela), name="HorarioEscuela"),
    path('Cursos/HorarioEscuela/MarcaEntrada/<idcur>/<idho>', login_required(MarcarEntrada), name="MarcarEntrada"),
    path('Cursos/HorarioEscuela/MarcarSalida/<idhe>', login_required(MarcarSalida), name="MarcarSalida"),
    path('Asistencia', login_required(Asistencia), name="Asistencia"),
    path('Administrador/Cursos', login_required(Admin_Cursos), name="Admin_Cursos"),
    path('Administrador/Asistencias', login_required(Admin_Asistencias), name="Admin_Asistencias"),
    path('Administrador/Usuarios', login_required(Admin_User), name="Admin_User"),
    path('Administrador/Usuarios/Registrar', login_required(AñadirUsuario.as_view()), name="AñadirUsuario"),
    path('Administrador/Horarios', login_required(Admin_Horario), name="Admin_Horario"),
    path('Administrador/Horarios/Añadir', login_required(Admin_Horario_Add), name="Admin_Horario_Add"),
    path('Administrador/Cursos/Añadir', login_required(Admin_Cursos_Add), name="Admin_Cursos_Add"),
    path('Administrador/Usuarios/DarBaja/<idu>', login_required(Admin_Dar_Baja), name="Admin_Dar_Baja"),
    path('Administrador/Usuarios/DarAlta/<idu>', login_required(Admin_Dar_Alta), name="Admin_Dar_Alta"),
    path('Administrador/Asistencias/ReportePDF', login_required(PDFPrueba.as_view()), name="PDFPrueba"),
]
