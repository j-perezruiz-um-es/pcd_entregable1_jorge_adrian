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

class Caracter(Enum):
    FB = 0
    OB = 1
    OP = 2
    TFG = 3

# -----------------------
# CLASES
# ----------------------- 
class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo : Enum = sexo
        
    @abstractmethod
    def devuelveDatos(self):
        pass
    
class Asignatura:
    def __init__(self, nombre, codigo, caracter, curso, cuatrimestre, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.caracter : Enum = caracter
        self.curso = curso
        self.cuatrimestre = cuatrimestre
        self.creditos = creditos

    def devuelveDatos(self):
        return "\n\tNombre: " + self.nombre + "\n\tCódigo: " + str(self.codigo) + "\n\tCaracter: " + str(self.caracter.name) + "\n\tCurso: " + str(self.curso) + "\n\tCuatrimestre: " + str(self.cuatrimestre) + "\n\tCréditos: " + str(self.creditos)

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas_matriculadas = []
    
    def devuelveDatos(self):
        return "\n\tNombre: "+self.nombre+"\n\tDNI: "+self.dni+"\n\tDireccion: "+self.direccion+"\n\tSexo: "+str(self.sexo.name)
    
    def matricularAsignatura(self, asignatura : Asignatura):
        for a in self.asignaturas_matriculadas:
            if (a == asignatura):
                print ("La asignatura "+asignatura.nombre+" ya esta matriculada")
                return
        self.asignaturas_matriculadas.append(asignatura)
    
    def desmatricularAsignatura(self, asignatura : Asignatura):
        for a in self.asignaturas_matriculadas:
            if (a == asignatura):
                self.asignaturas_matriculadas.remove(a)
                return
        print ("La asignatura "+asignatura.nombre+" no esta matriculada")
        
    def listadoAsignaturasMatriculadas(self):
        print ("LISTADO ASIGNATURAS MATRICULADAS POR", self.nombre.upper())
        for a  in self.asignaturas_matriculadas:
            print ("\t",a.devuelveDatos())
        print ()
    
class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.departamento : Enum = departamento
        
    def cambiarDepartamento(self, departamento):
        self.departamento = departamento
    
    def devuelveDatos(self):
        return "\n\tNombre: "+self.nombre+"\n\tDNI: "+self.dni+"\n\tDireccion: "+self.direccion+"\n\tSexo: "+str(self.sexo.name)+"\n\tDepartamento: "+str(self.departamento.name)
    
class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.area_investigacion = area_investigacion

    def devuelveDatos(self):
        return "\n\tNombre: " + self.nombre + "\n\tDNI: " + self.dni + "\n\tDireccion: " + self.direccion + "\n\tSexo: " + str(self.sexo.name) + "\n\tDepartamento: " + str(self.departamento.name) + "\n\tArea de Investigacion: " + self.area_investigacion

class ProfesorAsociado(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo , departamento):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.asignaturas_impartidas = []
    
    def devuelveDatos(self):
        datos = "\n\tNombre: " + self.nombre + "\n\tDNI: " + self.dni + "\n\tDireccion: " + self.direccion + "\n\tSexo: " + str(self.sexo.name) + "\n\tDepartamento: " + str(self.departamento.name) + "\n\tAsignaturas impartidas:\n"
        
        for asignatura in self.asignaturas_impartidas:
           datos += '\t\t' + asignatura.nombre + '\n'  
            
        return datos 
    
    def impartirAsignatura(self, asignatura : Asignatura):
        for a in self.asignaturas_impartidas:
            if (a == asignatura):
                print ("La asignatura "+asignatura.nombre+" ya esta impartida")
                return
        self.asignaturas_impartidas.append(asignatura)
    
    def quitarAsignatura(self, asignatura : Asignatura):
        for a in self.asignaturas_impartidas:
            if (a == asignatura):
                self.asignaturas_impartidas.remove(a)
                return
        print ("La asignatura "+asignatura.nombre+" no esta impartida")

    def listadoAsignaturasImpartidas(self):
        print ("LISTADO ASIGNATURAS IMPARTIDAS POR", self.nombre.upper())
        for a in self.asignaturas_impartidas:
            print ("\t",a.devuelveDatos())
        print ()

class ProfesorTitular(Investigador):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento, area_investigacion)
        self.asignaturas_impartidas = []
    
    def devuelveDatos(self):
        datos = "\n\tNombre: " + self.nombre + "\n\tDNI: " + self.dni + "\n\tDireccion: " + self.direccion + "\n\tSexo: " + str(self.sexo.name) + "\n\tDepartamento: " + str(self.departamento.name) + "\n\tAsignaturas impartidas:\n"
    
        for asignatura in self.asignaturas_impartidas:
            datos += "\t\t" + asignatura.nombre + "\n"
            
        return datos

    def impartirAsignatura(self, asignatura : Asignatura):
        for a in self.asignaturas_impartidas:
            if (a == asignatura):
                print ("La asignatura "+asignatura.nombre+" ya esta impartida")
                return
        self.asignaturas_impartidas.append(asignatura)
    
    def quitarAsignatura(self, asignatura : Asignatura):
        for a in self.asignaturas_impartidas:
            if (a == asignatura):
                self.asignaturas_impartidas.remove(a)
                return
        print ("La asignatura "+asignatura.nombre+" no esta impartida")

    def listadoAsignaturasImpartidas(self):
        print ("LISTADO ASIGNATURAS IMPARTIDAS POR", self.nombre.upper())
        for a in self.asignaturas_impartidas:
            print ("\t",a.devuelveDatos())
        print ()

class Universidad:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        
        # En cada lista defino a que clase pertenece para que en el caso de que se equivoquen al introducir los datos, salte el aviso
        self._estudiantes : Estudiante = []
        self._asignaturas : Asignatura = []
        self._asociados : ProfesorAsociado = []
        self._titulares : ProfesorTitular = []
        self._investigadores : Investigador = []
        self._miembros : MiembroDepartamento = []
        
    def anadirInvestigador(self, investigador : Investigador):
        for i in self._investigadores:
            if i.dni == investigador.dni:
                print("El investigador con DNI <"+investigador.dni+"> ya exite")
                return
        self._investigadores.append(investigador)
        self._miembros.append(investigador)
        
    def eliminarInvestigador(self, investigador : Investigador):
        for i in self._investigadores:
            if (i.dni == investigador.dni):
                self._investigadores.remove(i)
                self._miembros.remove(i)
                return
        print("El investigador con DNI <"+investigador.dni+"> no exite")
    
    def listadoInvestigadores(self):
        print ("LISTADO INVESTIGADORES")
        for i in self._investigadores:
            print ("\t",i.devuelveDatos())
        print ()
        
    def anadirProfesorTitular(self, profesor : ProfesorTitular):
        for pt in self._titulares:
            if pt.dni == profesor.dni:
                print("El profesor titular con DNI <"+profesor.dni+"> ya exite")
                return
        self._titulares.append(profesor)
        self._miembros.append(profesor)
        
    def eliminarProfesorTitular(self, profesor : ProfesorTitular):
        for pt in self._titulares:
            if (pt.dni == profesor.dni):
                self._titulares.remove(pt)
                self._miembros.remove(pt)
                return
        print("El profesor titular con DNI <"+profesor.dni+"> no exite")
    
    def listadoProfesoresTitulares(self):
        print ("LISTADO PROFESORES TITULARES")
        for pt in self._titulares:
            print ("\t",pt.devuelveDatos())
        print ()
    
    def anadirProfesorAsociado(self, profesor : ProfesorAsociado):
        for pa in self._asociados:
            if pa.dni == profesor.dni:
                print("El profesor asociado con DNI <"+profesor.dni+"> ya exite")
                return
        self._asociados.append(profesor)
        self._miembros.append(profesor)
        
    def eliminarProfesorAsociado(self, profesor : ProfesorAsociado):
        for pa in self._asociados:
            if (pa.dni == profesor.dni):
                self._asociados.remove(pa)
                self._miembros.remove(pa)
                return
        print("El profesor asociado con DNI <"+profesor.dni+"> no existe")
    
    def listadoProfesoresAsociados(self):
        print ("LISTADO PROFESORES ASOCIADOS")
        for pa in self._asociados:
            print ("\t",pa.devuelveDatos())
        print ()
    
    def anadirAsignatura(self, asignatura : Asignatura):  
        for a in self._asignaturas:
            if (a.nombre == asignatura.nombre):
                print("La asignatura "+asignatura.nombre+" ya existe")
                return
        self._asignaturas.append (asignatura)
    
    def eliminarAsignatura(self, asignatura : Asignatura):
        for a in self._asignaturas:
            if (a.codigo == asignatura.codigo):
                self._asignaturas.remove(a)
                return
        print("La asignatura "+asignatura.nombre+" no existe")

    def listadoAsignaturas(self):
        print ("LISTADO ASIGNATURAS")
        for a in self._asignaturas:
            print ("\t",a.devuelveDatos())
        print ()

    def anadirEstudiante(self, estudiante : Estudiante):
        for e in self._estudiantes:
            if (e.dni == estudiante.dni):
                print("El estudiante con DNI <"+estudiante.dni+"> ya existe")
                return
        self._estudiantes.append (estudiante)
    
    def eliminarEstudiante(self, estudiante : Estudiante):
        for e in self._estudiantes:
            if (e.dni == estudiante.dni):
                self._estudiantes.remove(e)
                return
        print ("El estudiante con DNI <"+estudiante.dni+"> no esta en la universidad")
        
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
#### Universidad ####

u = Universidad('Universidad de Murcia', 'Murcia')

#### Asignaturas ####

a1 = Asignatura("Matemática discreta", 6573, Caracter.FB, 1, 1, 6)
a2 = Asignatura("Optimizacion I", 6579, Caracter.FB, 1, 2, 6)
a3 = Asignatura("Bases de datos I", 6583, Caracter.OB, 2, 1, 6)
a4 = Asignatura("Senyales y sistemas", 6589, Caracter.OB, 2, 2, 6)
a5 = Asignatura("Machine learning II", 6593, Caracter.OB, 3, 1, 6)
a6 = Asignatura("Redes de datos", 6597, Caracter.OB, 3, 2, 6)
a7 = Asignatura("Practicas externas", 6605, Caracter.OP, 4, 1, 7.5)
a8 = Asignatura("Trabajo fin de grado", 6618, Caracter.TFG, 4, 2, 12)

u.anadirAsignatura(a1)
u.anadirAsignatura(a2)
u.anadirAsignatura(a3)
u.anadirAsignatura(a4)
u.anadirAsignatura(a5)
u.anadirAsignatura(a6)
u.anadirAsignatura(a7)
u.anadirAsignatura(a8)
u.listadoAsignaturas()

u.eliminarAsignatura(a1)
u.listadoAsignaturas()

#### Estudiantes ####

e1 = Estudiante("Adrian", "11222333A", "Avenida Santa Monica", Sexo.V)
e2 = Estudiante("Jorge", "44555666B", "Calle Zarate", Sexo.V)
e3 = Estudiante("Marta", "77888999C", "Calle Pinto", Sexo.M)

e1.matricularAsignatura(a1)
e1.matricularAsignatura(a2)
e2.matricularAsignatura(a3)
e2.matricularAsignatura(a4)
e3.matricularAsignatura(a5)
e3.matricularAsignatura(a6)
e3.matricularAsignatura(a7)
e3.matricularAsignatura(a8)

e3.listadoAsignaturasMatriculadas()
e3.desmatricularAsignatura(a8)
e3.desmatricularAsignatura(a7)
e3.listadoAsignaturasMatriculadas()

u.anadirEstudiante(e1)
u.anadirEstudiante(e2)
u.anadirEstudiante(e3)
u.listadoEstudiantes()
u.eliminarEstudiante(e2)
u.listadoEstudiantes()

#### Investigadores ####

investigador1 = Investigador("Pilar", "99888777D", "Calle Demonio del Sol", Sexo.M, Departamento.DIIC, "Area 1")
investigador2 = Investigador("Antonio", "7654332E", "Calle Costa del Sol", Sexo.V, Departamento.DIS, "Area 4")
investigador3 = Investigador("Carmen", "1234568N", "Calle Sol", Sexo.V, Departamento.DIIC, "Area 2")

u.anadirInvestigador(investigador1)
u.anadirInvestigador(investigador2)
u.anadirInvestigador(investigador3)
u.listadoInvestigadores()
u.eliminarInvestigador(investigador1)
u.listadoInvestigadores()



#### Profesores titulares ####

titular1 = ProfesorTitular("Ruben", "33222111F", "Calle del Señor exigente", Sexo.V, Departamento.DIS, "Area 2")
titular2 = ProfesorTitular("Felix", "87654543Y", "Calle Cuenca", Sexo.V, Departamento.DIIC, "Area 4")
titular3 = ProfesorTitular("Lucia", "09876543W", "Calle Correos", Sexo.M, Departamento.DITEC, "Area 1")

titular1.impartirAsignatura(a2)
titular1.impartirAsignatura(a1)
titular1.impartirAsignatura(a3)
titular2.impartirAsignatura(a8)
titular2.impartirAsignatura(a2)
titular2.impartirAsignatura(a1)
titular3.impartirAsignatura(a6)
titular3.impartirAsignatura(a5)
titular3.impartirAsignatura(a1)

titular1.listadoAsignaturasImpartidas()

u.anadirProfesorTitular(titular1)
u.anadirProfesorTitular(titular2)
u.anadirProfesorTitular(titular3)
u.listadoProfesoresTitulares()
u.eliminarProfesorTitular(titular3)
u.listadoProfesoresTitulares()

#### Profesores asociados ####

asociado1 = ProfesorAsociado("Paco", "66555444E", "Avenida Radiologo del Norte", Sexo.V, Departamento.DITEC)
asociado2 = ProfesorAsociado("Jorge", "1113276E", "Avenida Juan Carlos I", Sexo.V, Departamento.DIIC)
asociado3 = ProfesorAsociado("Laura", "9876554R", "Avenida España", Sexo.M, Departamento.DIS)


asociado1.impartirAsignatura(a1)
asociado1.impartirAsignatura(a6)
asociado1.impartirAsignatura(a4)
asociado2.impartirAsignatura(a3)
asociado2.impartirAsignatura(a4)
asociado2.impartirAsignatura(a2)
asociado3.impartirAsignatura(a6)
asociado3.impartirAsignatura(a2)
asociado3.impartirAsignatura(a1)

asociado1.listadoAsignaturasImpartidas()

u.anadirProfesorAsociado(asociado1)
u.anadirProfesorAsociado(asociado2)
u.anadirProfesorAsociado(asociado3)
u.listadoProfesoresAsociados()
u.eliminarProfesorAsociado(asociado3)
u.listadoProfesoresAsociados()


#### Miembros de departamento ####

u.listadoMiembrosDepartamento()
asociado3.cambiarDepartamento(Departamento.DIIC)
u.listadoMiembrosDepartamento()
u.eliminarProfesorAsociado(asociado1)
u.listadoMiembrosDepartamento()



#
#####################################

# -----------------------
# UMLET
# -----------------------
# Crear Universidad, para añadir y eliminar miembros y estudiantes
# Eliminar Profesor
# Son herencia de persona: miembros de departamento y estudiantes.
# Son herencia de miembros de departamento: profesor asociado e investigador
# Son herencia de investigador: profesor titular