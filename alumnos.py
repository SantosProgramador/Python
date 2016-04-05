from .personas import Persona

class Alumnos(Persona):

	def __init__(self, nombre, apellidos, edad, asignaturas):
		super().__init__(nombre, apellidos, edad)
		self.asignaturas = asignaturas

	def __str__(self):
		#return self.nombre+" "+self.apellidos+", "+str(self.edad)+" =>"+self.asignaturas
		return super().__str__()+" => "+self.asignaturas