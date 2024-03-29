from enum import Enum
from abc import ABCMeta, abstractmethod

# -----------------------
# EXCEPCIONES
# -----------------------
class ErrorEnSexo(Exception):
    pass

# -----------------------
# ENUMERADOS
# -----------------------
class Departamento(Enum):
    DIIC = 0
    DITEC = 1
    DIS = 2

class Sexo(Enum):
    V = 0
    M = 1

# -----------------------
# CLASES
# ----------------------- 
class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo
        
    @abstractmethod
    def devuelveDatos(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, asignaturas_matriculadas):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas_matriculadas = asignaturas_matriculadas
    
    def devuelveDatos(self):
        return "Nombre: "+self.nombre+" DNI: "+self.dni+" Direccion: "+self.direccion+" Sexo: "+str(self.sexo)+" Asignaturas matriculadas: "+', '.join(map(str, self.asignaturas_matriculadas))

class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.departamento = departamento
        
    def cambiarDepartamento(self, departamento):
        self.departamento = departamento
    
    def devuelveDatos(self):
        return "Nombre: "+self.nombre+" DNI: "+self.dni+" Direccion: "+self.direccion+" Sexo: "+str(self.sexo)+" Departamento: "+str(self.departamento)
    
class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.area_investigacion = area_investigacion

    def devuelveDatos(self):
        return "Nombre: "+self.nombre+" DNI: "+self.dni+" Direccion: "+self.direccion+" Sexo: "+str(self.sexo)+" Departamento: "+str(self.departamento)+" Area de Investigacion: "+self.area_investigacion
    
class ProfesorAsociado(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas_impartidas):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.asignaturas_impartidas = asignaturas_impartidas     
    
    def devuelveDatos(self):
        return "Nombre: "+self.nombre+" DNI: "+self.dni+" Direccion: "+self.direccion+" Sexo: "+str(self.sexo)+" Departamento: "+str(self.departamento)+" Asignaturas impartidas: "+', '.join(map(str, self.asignaturas_impartidas))

class ProfesorTitular(Investigador):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas_impartidas, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento, area_investigacion)
        self.asignaturas_impartidas = asignaturas_impartidas 
    
    def devuelveDatos(self):
        return "Nombre: "+self.nombre+" DNI: "+self.dni+" Direccion: "+self.direccion+" Sexo: "+str(self.sexo)+" Departamento: "+str(self.departamento)+" Area de Investigacion: "+self.area_investigacion+" Asignaturas impartidas: "+', '.join(map(str, self.asignaturas_impartidas))

class Universidad:
    def __init__(self):
        self._estudiantes = []
        self._miembros = []
    
    def anadirEstudiante(self, estudiante):
        for e in self._estudiantes:
            if (e.dni == estudiante.dni):
                print("El estudiante con DNI <"+estudiante.dni+"> ya existe")
                return
        self._estudiantes.append (estudiante)
    
    def eliminarEstudiante(self, dni):
        for e in self._estudiantes:
            if (e.dni == dni):
                self._estudiantes.remove(e)
                return
        print ("El estudiante con DNI <"+dni+"> no exite")
        
    def anadirMiembroDepartamento(self, miembro):      
        for m in self._miembros:
            if (m.dni == miembro.dni):
                print("El miembro de departamento con DNI <"+miembro.dni+"> ya existe")
                return
        self._miembros.append(miembro)
    
    def eliminarMiembroDepartamento(self, dni):
        for m in self._miembros:
            if (m.dni == dni):
                self._miembros.remove(m)
                return
        print ("El estudiante con DNI <"+dni+"> no exite")

    def listadoEstudiantes(self):
        print ("LISTADO ESTUDIANTES")
        for e in self._estudiantes:
            print ("\t",e.devuelveDatos())
        print ()
    
    def listadoMiembrosDepartamento(self):
        print ("LISTADO MIEMBROS DE DEPARTAMENTO")
        for m in self._miembros:
            print ("\t",m.devuelveDatos())
        print ()

# -----------------------
# SISTEMA DE GESTION
# ----------------------- 
u = Universidad()

e1 = Estudiante("Adrian", "11222333A", "Avenida Santa Monica", Sexo.V, ["Matematicas", "Informatica", "Bases de Datos"])
e2 = Estudiante("Jorge", "44555666B", "Calle Zarate", Sexo.V, ["Calculo I", "Estadistica"])
e3 = Estudiante("Marta", "77888999C", "Calle Pinto", Sexo.M, ["Biologia"])

m1 = Investigador("Pilar", "99888777D", "Calle Demonio del Sol", Sexo.M, Departamento.DIIC, "Area 1")
m2 = ProfesorAsociado("Paco", "66555444E", "Avenida Radiologo del Norte", Sexo.V, Departamento.DITEC, ["Matematicas", "Calculo I"])
m3 = ProfesorTitular("Ruben", "33222111F", "Calle del Señor exigente", Sexo.V, Departamento.DIS, ["Informatica"], "Area 2")

u.anadirEstudiante(e1)
u.anadirEstudiante(e2)
u.anadirEstudiante(e3)

u.anadirMiembroDepartamento(m1)
u.anadirMiembroDepartamento(m2)
u.anadirMiembroDepartamento(m3)

u.listadoEstudiantes()
u.listadoMiembrosDepartamento()

m2.cambiarDepartamento(Departamento.DIS)
u.listadoMiembrosDepartamento()

u.eliminarEstudiante("11222333A")
u.eliminarMiembroDepartamento("99888777D")
u.listadoEstudiantes()
u.listadoMiembrosDepartamento()


# -----------------------
# POSIBLES MEJORAS
# ----------------------- 
'''    
ESTUDIANTE    
        self.asignaturas_matriculadas = []
    
    def matricularAsignatura(self, asignatura):
        for a in self.asignaturas_matriculadas:
            if (a == asignatura):
                print ("Asignatura "+asignatura+" ya esta asignada")
                return
        self.asignaturas_matriculadas.append(asignatura)
'''

'''    
PROFESOR        
        self.asignaturas_impartidas = []
        
    def impartirAsignatura (self, asignatura):                          
        for a in self.asignaturas_impartidas:
            if (a == asignatura):
                print ("Asignatura "+asignatura+" ya esta asignada")
                return
        self.asignaturas_impartidas.append(asignatura)'''


# -----------------------
# DUDAS
# -----------------------
# VER QUE LOS QUE ESTEN EN FORMATO LISTA PONERLO COMO VARIABLE EN INIT O PONERLO COMO LISTA VACIA E IR ANYADIENDO CADA ASIGNATURA

# -----------------------
# UMLET
# -----------------------
# Crear Universidad, para añadir y eliminar miembros y estudiantes
# Son herencia de persona: miembros de departamento y estudiantes.
# Son herencia de miembros de departamento: profesor asociado e investigador
# Son herencia de investigador: profesor titular