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
    VARON = 0
    MUJER = 1
    
class Tipo(Enum):
    INVESTIGADOR = 0  # si es investigador suponemos tambien que es titular
    ASOCIADO = 1
    TITULAR = 2

# -----------------------
# CLASES
# ----------------------- 
class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self._dni = dni
        self._direccion = direccion
        self._sexo = sexo
        
    @abstractmethod
    def devuelveDatos(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, num_matricula):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas_matriculadas = []
        self._num_matricula = num_matricula
    
    def devuelveDatos(self):
        if len(self.asignaturas_matriculadas) == 0:
            self.asignaturas_matriculadas = 'Ninguna asignatura matrilada' # caso de no tener ninguna asignatura en la lista
            return "\n\tNombre: "+self.nombre+"\n\tDNI: "+self._dni+" \n\tDireccion: "+self._direccion+" \n\tSexo: "+str(self._sexo.name)+" \n\tAsignaturas matriculadas: "+ self.asignaturas_matriculadas + '\n\tNumero de matricula: '+ str(self._num_matricula)
        else:
            return "\n\tNombre: "+self.nombre+"\n\tDNI: "+self._dni+" \n\tDireccion: "+self._direccion+" \n\tSexo: "+str(self._sexo.name)+" \n\tAsignaturas matriculadas: "+', '.join(map(str, self.asignaturas_matriculadas)) + '\n\tNumero de matricula: '+ str(self._num_matricula)

    
    
    def matricularAsignatura(self, asignatura):
        for a in self.asignaturas_matriculadas:
            if (a == asignatura):
                print ("Asignatura "+asignatura+" ya esta asignada")
                return
        self.asignaturas_matriculadas.append(asignatura.nombre)

class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento, id, tipo):
        super().__init__(nombre, dni, direccion, sexo)
        self.departamento = departamento
        self._id = id
        self.tipo = tipo
        
    def cambiarDepartamento(self, departamento):
        self.departamento = departamento
    
    def devuelveDatos(self):
        return "\nNombre: "+self.nombre+" \n\tDNI: "+self._dni+" \n\tDireccion: "+self._direccion+" \n\tSexo: "+str(self._sexo)+" \n\tDepartamento: "+str(self.departamento) + '\n\tID: ' + str(self._id) + '\n\tTipo de profesor: ' + str(self.tipo.name)
    
class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, id, tipo, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento, id, tipo)
        self.area_investigacion = area_investigacion

    def devuelveDatos(self):
        return "\nNombre: "+self.nombre+" \n\tDNI: "+self._dni+"\n\tDireccion: "+self._direccion+"\n\t Sexo: "+str(self._sexo.name)+" \n\tDepartamento: "+str(self.departamento.name)+" \n\tArea de Investigacion: "+self.area_investigacion+ '\n\tID: ' + str(self._id) + '\n\tTipo de profesor: ' + str(self.tipo.name)
    
class ProfesorAsociado(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, id, tipo):
        super().__init__(nombre, dni, direccion, sexo, departamento, id , tipo)
        self.asignaturas_impartidas = []     
    
    def devuelveDatos(self):
        if len(self.asignaturas_impartidas) == 0:
            self.asignaturas_impartidas = 'Ninguna asignatura impartida' # caso de no tener ninguna asignatura en la lista
            return "\nNombre: "+self.nombre+" \n\tDNI: "+self._dni+" \n\tDireccion: "+self._direccion+" \n\tSexo: "+str(self._sexo.name)+" \n\tDepartamento: "+str(self.departamento.name)+" \n\tAsignaturas impartidas: "+self.asignaturas_impartidas  + '\n\tId: '+ str(self._id) + '\n\tTipo de profesor: ' +  str(self.tipo.name)
        
        return "\nNombre: "+self.nombre+" \n\tDNI: "+self._dni+" \n\tDireccion: "+self._direccion+" \n\tSexo: "+str(self._sexo.name)+" \n\tDepartamento: "+str(self.departamento.name)+" \n\tAsignaturas impartidas: "+', '.join(map(str, self.asignaturas_impartidas)) + '\n\tId: ' + str(self._id) + '\n\tTipo de profesor: ' + str(self.tipo.name)

    def impartirAsignatura(self, asignatura):
        for a in self.asignaturas_impartidas:
            if (a == asignatura):
                print ("Asignatura "+asignatura+" ya esta asignada")
                return
        self.asignaturas_impartidas.append(asignatura.nombre)

class ProfesorTitular(Investigador):
    def __init__(self, nombre, dni, direccion, sexo, departamento, id, tipo, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento, id, tipo, area_investigacion)
        self.asignaturas_impartidas = [] 
    
    def devuelveDatos(self):
        if len(self.asignaturas_impartidas) == 0:
            self.asignaturas_impartidas = 'Ninguna asignatura impartida' # caso de no tener ninguna asignatura en la lista
            return "\nNombre: "+self.nombre+" \n\tDNI: "+self._dni+" \n\tDireccion: "+self._direccion+" \n\tSexo: "+str(self._sexo.name)+" \n\tDepartamento: "+str(self.departamento.name)+" \n\tArea de Investigacion: "+self.area_investigacion+" \n\tAsignaturas impartidas: "+ self.asignaturas_impartidas + '\n\tId: ' + str(self._id) + '\n\tTipo de profesor: ' + str(self.tipo.name)

        return "\nNombre: "+self.nombre+" \n\tDNI: "+self._dni+" \n\tDireccion: "+self._direccion+" \n\tSexo: "+str(self._sexo.name)+" \n\tDepartamento: "+str(self.departamento.name)+" \n\tArea de Investigacion: "+self.area_investigacion+" \n\tAsignaturas impartidas: "+', '.join(map(str, self.asignaturas_impartidas)) + '\n\tId: ' + str(self._id) + '\n\tTipo de profesor: ' + str(self.tipo.name)
    
    def impartirAsignatura(self, asignatura):
        for a in self.asignaturas_impartidas:
            if (a == asignatura):
                print ("Asignatura "+asignatura+" ya esta asignada")
                return
        self.asignaturas_impartidas.append(asignatura.nombre)
        
class Asignatura():
    def __init__(self, nombre, precio, creditos, curso, codigo):
        self.nombre = nombre
        self.precio = precio
        self.creditos = creditos
        self.curso = curso
        self.codigo = codigo 
    def devuelveDatos(self):
        return  '\n\t'+ self.nombre + '\n\t____________\n' + '\n\tPrecio: ' + str(self.precio) + '\n\tCreditos: ' + str(self.creditos) + '\n\tCurso: ' + self.curso + '\n\tCodigo de la asignatura: ' + str(self.codigo)


class Universidad:
    def __init__(self):
        self._estudiantes = []
        self._miembros = []
        self.asignaturas = []
    
    def anadirEstudiante(self, estudiante):
        for e in self._estudiantes:
            if (e._dni == estudiante._dni):
                print("El estudiante con DNI <"+estudiante.dni+"> ya existe")
                return
        self._estudiantes.append (estudiante)
    
    def eliminarEstudiante(self, dni):
        for e in self._estudiantes:
            if (e._dni == dni):
                self._estudiantes.remove(e)
                return
        print ("El estudiante con DNI <"+dni+"> no exite")
        
    def anadirMiembroDepartamento(self, miembro):      
        for m in self._miembros:
            if (m._dni == miembro._dni):
                print("El miembro de departamento con DNI <"+miembro._dni+"> ya existe")
                return
        self._miembros.append(miembro)
    
    def eliminarMiembroDepartamento(self, dni):
        for m in self._miembros:
            if (m._dni == dni):
                self._miembros.remove(m)
                return
        print ("El estudiante con DNI <"+dni+"> no exite")
        
    def añadirAsignatura(self, asignatura):
        for a in self.asignaturas:
            if (a.codigo == asignatura.codigo):
                print("La asignatura con codigo <"+asignatura.codigo+"> ya existe")
                return
        self.asignaturas.append(asignatura)
        
    def eliminarAsignatura(self, codigo):
        for a in self.asignaturas:
            if codigo == a.codigo:
                self.asignaturas.remove(a)
                return
        print('La asignatura con codigo<'+codigo+'> no existe')
        

    def listadoEstudiantes(self):
        print ("\nLISTADO ESTUDIANTES")
        for e in self._estudiantes:
            print ("\t",e.devuelveDatos())
        print ()
    
    def listadoMiembrosDepartamento(self):
        print ("\nLISTADO MIEMBROS DE DEPARTAMENTO")
        for m in self._miembros:
            print ("\t",m.devuelveDatos())
        print ()
        
    def listadoAsignaturas(self):
        print('\nLISTADO ASIGNATURAS')
        for a in self.asignaturas:
            print('\t',a.devuelveDatos())
        print ()

# -----------------------
# SISTEMA DE GESTION
# ----------------------- 
u = Universidad()

e1 = Estudiante("Adrian", "11222333A", "Avenida Santa Monica", Sexo.VARON, 12345)
e2 = Estudiante("Jorge", "44555666B", "Calle Zarate", Sexo.VARON, 45364)
e3 = Estudiante("Marta", "77888999C", "Calle Pinto", Sexo.MUJER, 45637)

m1 = Investigador("Pilar", "99888777D", "Calle Demonio del Sol", Sexo.MUJER, Departamento.DIIC, "Area 1", 12, Tipo.INVESTIGADOR)
m2 = ProfesorAsociado("Paco", "66555444E", "Avenida Radiologo del Norte", Sexo.VARON, Departamento.DITEC, 11, Tipo.ASOCIADO)
m3 = ProfesorTitular("Ruben", "33222111F", "Calle del Señor exigente", Sexo.VARON, Departamento.DIS, "Area 2", 10, Tipo.TITULAR)

a1 = Asignatura('Calculo I', 100, 6, 'Primer año', 20023)
a2 = Asignatura('Analisis', 100, 6, 'Segundo año', 20121)
a3 = Asignatura('Redes', 100, 6, 'Segundo año', 20123)
a4 = Asignatura('Inferencia', 100, 6, 'Segundo año', 20124)
a5 = Asignatura('ADA', 100, 6, 'Segundo año', 20125)

e1.matricularAsignatura(a1)
e1.matricularAsignatura(a2)
e1.matricularAsignatura(a3)
e2.matricularAsignatura(a5)
e2.matricularAsignatura(a4)
e2.matricularAsignatura(a1)


m2.impartirAsignatura(a1)
m2.impartirAsignatura(a5)
m2.impartirAsignatura(a4)

u.anadirEstudiante(e1)
u.anadirEstudiante(e2)
u.anadirEstudiante(e3)

# u.anadirMiembroDepartamento(m1)
u.anadirMiembroDepartamento(m2)
# u.anadirMiembroDepartamento(m3)

u.añadirAsignatura(a1)
u.añadirAsignatura(a2)
u.añadirAsignatura(a3)
u.añadirAsignatura(a4)
u.añadirAsignatura(a5)

u.listadoEstudiantes()
u.listadoMiembrosDepartamento()
u.listadoAsignaturas()

m2.cambiarDepartamento(Departamento.DIS)
u.listadoMiembrosDepartamento()

u.eliminarEstudiante("11222333A")
u.eliminarMiembroDepartamento("99888777D")
u.listadoEstudiantes()
u.listadoMiembrosDepartamento()





# -----------------------
# DUDAS
# -----------------------
# Averiguar porque da el error al devolver los datos de investigador o profesor titular
# Corregir error de cuando un estudiante no tiene asignaturas matriculadas, porque se imprime asi de raro habiendo un if.
# -----------------------
# POR HACER
# -----------------------
# Seguir haciendo las funciones en clase universidad
# Corregir el error que da

# POSIBLE MEJORA : poner la funcion cambiar_departamento en Universidad

# UMLET
# -----------------------
# Crear Universidad, para añadir y eliminar miembros y estudiantes
# Son herencia de persona: miembros de departamento y estudiantes.
# Son herencia de miembros de departamento: profesor asociado e investigador
# Son herencia de investigador: profesor titular