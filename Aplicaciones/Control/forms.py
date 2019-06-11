from django import forms
from Aplicaciones.Control.models import Categoria, Horario, HoraEntrada, HoraSalida, Curso
choice = (('M','Mañana'),('T','Tarde'),('N','Noche'))
seccion = (('A','A'),('B','B'),('C','C'))

class HorarioForm(forms.ModelForm):

	class Meta:
		model = Horario

		fields = [
			#'h_entrada',
            #'h_salida' ,
			'time_entrada',
			'time_salida',
            'actividad' ,
            'firma',
            'observaciones',
			'iduser',
            'idcurso',

		]

		labels = {
			#'h_entrada': '',
            #'h_salida':'' ,
			'time_entrada':'',
			'time_salida':'',
            'actividad':'' ,
            'firma':'',
            'observaciones':'',
			'iduser':'',
            'idcurso':'',

		}

		widgets = {
			'time_entrada':forms.DateTimeInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora Inicial'}),
			'time_salida':forms.DateTimeInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora Final'}),
			#'h_entrada': forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora de Entrada'}),
            #'h_salida':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora de Salida'}),
            'actividad':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Actividad'}),
            'firma':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firma Digital'}),
            'observaciones':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Observaciones'}),
			'iduser':forms.Select(attrs={'class':'form-control', 'required':'', 'placeholder':'Observaciones'}),
            'idcurso':forms.Select(attrs={'class':'form-control', 'required':'', 'placeholder':'Observaciones'}),
		}

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso

		fields = [
			'curso',
		    'año',
		    'turno',
		    'aula',
		    'seccion',
		    'idciclo',
		    'iduser',
		]
		labels = {
			'curso': '',
		    'año': '',
		    'turno': '',
		    'aula': '',
		    'seccion': '',
		    'idciclo': 'Ciclo',
		    'iduser': 'Docente',
		}
		widgets = {
			'curso': forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Curso'}),
		    'año': forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Año', 'type':'number'}),
		    'turno': forms.Select(attrs={'class':'form-control', 'required':'', 'placeholder':'Turno'}, choices=choice),
		    'aula': forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Aula'}),
		    'seccion': forms.Select(attrs={'class':'form-control', 'required':'', 'placeholder':'Sección'}, choices=seccion),
		    'idciclo': forms.Select(attrs={'class':'form-control', 'required':'', 'placeholder':'Ciclo'}),
		    'iduser': forms.Select(attrs={'class':'form-control', 'required':'', 'placeholder':'Docente'}),
		}


#class HoraEntradaForm(forms.ModelForm):

#	class Meta:
#		model = HoraEntrada

#		fields = [
#			'h_entrada',

#		]

#class CategoriaForm(forms.ModelForm):
#	class Meta:
#		model = Categoria
#
#		fields = [
#			'categoria',
#			'idcurso',
#		]
#		labels = {
#			'categoria':'',
#			'idcurso':'Curso',
#		}
#		widgets = {
#			'categoria':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Categoria'}),
#			'idcurso':forms.Select(attrs={'class':'form-control', 'required':'', 'placeholder':'Curso'}),
#		}
