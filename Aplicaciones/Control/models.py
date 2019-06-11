from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ciclo(models.Model):
    ciclo = models.CharField(max_length=4)
    def __str__(self):
        return '{}'.format(self.ciclo)


class Curso(models.Model):
    curso = models.CharField(max_length=50)
    año = models.IntegerField()
    turno = models.CharField(max_length=50)
    aula = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    idciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{} | {} | {}'.format(self.idciclo, self.curso,  self.iduser)

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    iduser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.categoria, self.iduser)

class Horario(models.Model):
    #h_entrada = models.CharField(max_length=50)
    #h_salida = models.CharField(max_length=50)
    time_entrada = models.TimeField(null=True, blank=True)#
    time_salida = models.TimeField(null=True, blank=True)#
    actividad = models.CharField(max_length=50)
    firma = models.CharField(max_length=50, blank=True)#
    observaciones = models.CharField(max_length=50)#
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)


    def __str__(self):
        return '{} | {} | {} | {}'.format(self.actividad, self.idcurso, self.time_entrada, self.time_salida)

class HoraEntrada(models.Model):
    cod_entrada = models.CharField(max_length=50, unique=True)
    h_entrada= models.DateTimeField(null=True, blank=True)
    f_entrada = models.CharField(null=True, blank=True, max_length=50)
    h_entrada_str = models.CharField(null=True, blank=True, max_length=50)
    idhorario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    #iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    #idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return '{} | {} | {}'.format(self.cod_entrada, self.h_entrada, self.idhorario)

class HoraSalida(models.Model):
    cod_salida = models.CharField(max_length=50, unique=True)
    h_salida= models.DateTimeField(null=True, blank=True)
    f_salida = models.CharField(null=True, blank=True, max_length=50)
    h_salida_str = models.CharField(null=True, blank=True, max_length=50)
    id_hora_entrada = models.ForeignKey(HoraEntrada, on_delete=models.CASCADE)
    #iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    #idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return '{} | {} '.format(self.h_salida, self.id_hora_entrada)
