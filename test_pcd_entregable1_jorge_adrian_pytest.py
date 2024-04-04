from pcd_entregable1_jorge_adrian  import *
import pytest

# Test para la función matricularAsignatura de un estudiante
def test_matricularAsignatura():
    estudiante = Estudiante("Marta", "77888999C", "Calle Pinto", Sexo.M)
    asignatura = Asignatura("Trabajo fin de grado", 6618, Caracter.TFG, 4, 2, 12)
    
    estudiante.matricularAsignatura(asignatura)

    assert asignatura in estudiante.asignaturas_matriculadas

def test_matricularAsignatura_incorrecto():
    estudiante = Estudiante("Marta", "77888999C", "Calle Pinto", Sexo.M)
    asignatura = "Calculo"

    with pytest.raises(ErrorEnAsignatura):
        estudiante.matricularAsignatura(asignatura)

# Test para la función desmatricularAsignatura de un estudiante
def test_desmatricularAsignatura():
    estudiante = Estudiante("Marta", "77888999C", "Calle Pinto", Sexo.M)
    asignatura = Asignatura("Trabajo fin de grado", 6618, Caracter.TFG, 4, 2, 12)
    
    estudiante.matricularAsignatura(asignatura)
    
    estudiante.desmatricularAsignatura(asignatura)

    assert asignatura not in estudiante.asignaturas_matriculadas

def test_desmatricularAsignatura_incorrecto():
    estudiante = Estudiante("Marta", "77888999C", "Calle Pinto", Sexo.M)
    asignatura = "Informatica" 

    with pytest.raises(ErrorEnAsignatura):
        estudiante.desmatricularAsignatura(asignatura)

# Tests para la funcion cambiarDepartamento de un miembro de departamento
def test_cambiarDepartamento():
    miembro = Investigador("Antonio", "7654332E", "Calle Costa del Sol", Sexo.V, Departamento.DIS, "Area 4")
    departamento = Departamento.DITEC
    
    miembro.cambiarDepartamento(departamento)
    
    assert miembro.departamento == departamento

def test_cambiarDepartamento_incorrecto():
    miembro = Investigador("Antonio", "7654332E", "Calle Costa del Sol", Sexo.V, Departamento.DIS, "Area 4")
    departamento = "DITEC"
    
    with pytest.raises(ErrorEnDepartamento):
        miembro.cambiarDepartamento(departamento)

# Test para la función impartirAsignatura de un profesor
def test_impartirAsignatura():
    profesor = ProfesorAsociado("Paco", "66555444E", "Avenida Radiologo del Norte", Sexo.V, Departamento.DITEC)
    asignatura = Asignatura("Practicas externas", 6605, Caracter.OP, 4, 1, 7.5)
    
    profesor.impartirAsignatura(asignatura)

    assert asignatura in profesor.asignaturas_impartidas

def test_impartirAsignatura_incorrecto():
    profesor = ProfesorAsociado("Paco", "66555444E", "Avenida Radiologo del Norte", Sexo.V, Departamento.DITEC)
    asignatura = "Bases de datos"

    with pytest.raises(ErrorEnAsignatura):
        profesor.impartirAsignatura(asignatura)

# Test para la función quitarAsignatura de un profesor
def test_quitarAsignatura():
    profesor = ProfesorTitular("Ruben", "33222111F", "Calle del Señor exigente", Sexo.V, Departamento.DIS, "Area 2")
    asignatura = Asignatura("Redes de datos", 6597, Caracter.OB, 3, 2, 6)
    
    profesor.impartirAsignatura(asignatura)
    
    profesor.quitarAsignatura(asignatura)

    assert asignatura not in profesor.asignaturas_impartidas

def test_quitarAsignatura_incorrecto():
    profesor = ProfesorTitular("Ruben", "33222111F", "Calle del Señor exigente", Sexo.V, Departamento.DIS, "Area 2")
    asignatura = "Estadistica"

    with pytest.raises(ErrorEnAsignatura):
        profesor.quitarAsignatura(asignatura)

# Test para la función anadirInvestigador en una universidad
def test_anadirInvestigador():
    universidad = Universidad('Universidad de Murcia', 'Murcia')
    investigador = Investigador("Carmen", "1234568N", "Calle Sol", Sexo.V, Departamento.DIIC, "Area 2")
    
    universidad.anadirInvestigador(investigador)

    assert investigador in universidad._investigadores
    assert investigador in universidad._miembros

def test_anadirInvestigador_incorrecto():
    universidad = Universidad('Universidad de Murcia', 'Murcia')
    investigador = "Mario"

    with pytest.raises(ErrorEnInvestigador):
        universidad.anadirInvestigador(investigador)

# Test para la función eliminarInvestigador en una universidad
def test_eliminarInvestigador():
    universidad = Universidad('Universidad de Murcia', 'Murcia')
    investigador = Investigador("Pilar", "99888777D", "Calle Demonio del Sol", Sexo.M, Departamento.DIIC, "Area 1")
    
    universidad.anadirInvestigador(investigador)
    
    universidad.eliminarInvestigador(investigador)

    assert investigador not in universidad._investigadores
    assert investigador not in universidad._miembros

def test_eliminarInvestigador_incorrecto():
    universidad = Universidad('Universidad de Murcia', 'Murcia')
    investigador = "Celia"

    with pytest.raises(ErrorEnInvestigador):
        universidad.eliminarInvestigador(investigador)

# Test para la función anadirProfesorTitular en una universidad
def test_anadirProfesorTitular():
    universidad = Universidad('Universidad de Valencia', 'Valencia')
    titular = ProfesorTitular("Felix", "87654543Y", "Calle Cuenca", Sexo.V, Departamento.DIIC, "Area 4")
    
    universidad.anadirProfesorTitular(titular)

    assert titular in universidad._titulares
    assert titular in universidad._miembros

def test_anadirProfesorTitular_incorrecto():
    universidad = Universidad('Universidad de Valencia', 'Valencia')
    titular = "Raul"

    with pytest.raises(ErrorEnProfesorTitular):
        universidad.anadirProfesorTitular(titular)

# Test para la función eliminarProfesorTitular en una universidad
def test_eliminarProfesorTitular():
    universidad = Universidad('Universidad de Valencia', 'Valencia')
    titular = ProfesorTitular("Felix", "87654543Y", "Calle Cuenca", Sexo.V, Departamento.DIIC, "Area 4")
    
    universidad.anadirProfesorTitular(titular)
    
    universidad.eliminarProfesorTitular(titular)

    assert titular not in universidad._titulares
    assert titular not in universidad._miembros

def test_eliminarProfesorTitular_incorrecto():
    universidad = Universidad('Universidad de Valencia', 'Valencia')
    titular = "Juanpe"

    with pytest.raises(ErrorEnProfesorTitular):
        universidad.eliminarProfesorTitular(titular)
        
# Test para la función anadirProfesorAsociado en una universidad
def test_anadirProfesorAsociado():
    universidad = Universidad('Universidad de Valencia', 'Valencia')
    asociado = ProfesorAsociado("Laura", "9876554R", "Avenida España", Sexo.M, Departamento.DIS)
    
    universidad.anadirProfesorAsociado(asociado)

    assert asociado in universidad._asociados
    assert asociado in universidad._miembros

def test_anadirProfesorAsociado_incorrecto():
    universidad = Universidad('Universidad de Valencia', 'Valencia')
    asociado = "Jose Maria"

    with pytest.raises(ErrorEnProfesorAsociado):
        universidad.anadirProfesorAsociado(asociado)

# Test para la función eliminarProfesorAsociado en una universidad
def test_eliminarProfesorAsociado():
    universidad = Universidad('Universidad de Valencia', 'Valencia')
    asociado = ProfesorAsociado("Laura", "9876554R", "Avenida España", Sexo.M, Departamento.DIS)
    
    universidad.anadirProfesorAsociado(asociado)
    
    universidad.eliminarProfesorAsociado(asociado)

    assert asociado not in universidad._asociados
    assert asociado not in universidad._miembros

def test_eliminarProfesorAsociado_incorrecto():
    universidad = Universidad('Universidad de Valencia', 'Valencia')
    asociado = "Lola"

    with pytest.raises(ErrorEnProfesorAsociado):
        universidad.eliminarProfesorAsociado(asociado)
        
# Test para la función anadirAsignatura en una universidad
def test_anadirAsignatura():
    universidad = Universidad('Universidad de Cartagena', 'Murcia')
    asignatura = Asignatura("Redes de datos", 6597, Caracter.OB, 3, 2, 6)
    
    universidad.anadirAsignatura(asignatura)

    assert asignatura in universidad._asignaturas

def test_anadirAsignatura_incorrecto():
    universidad = Universidad('Universidad de Cartagena', 'Murcia')
    asignatura = "Tecnologia"

    with pytest.raises(ErrorEnAsignatura):
        universidad.anadirAsignatura(asignatura)

# Test para la función eliminarAsignatura en una universidad
def test_eliminarAsignatura():
    universidad = Universidad('Universidad de Cartagena', 'Murcia')
    asignatura = Asignatura("Redes de datos", 6597, Caracter.OB, 3, 2, 6)
    
    universidad.anadirAsignatura(asignatura)
    
    universidad.eliminarAsignatura(asignatura)

    assert asignatura not in universidad._asignaturas

def test_eliminarAsignatura_incorrecto():
    universidad = Universidad('Universidad de Cartagena', 'Murcia')
    asignatura = "Robotica"

    with pytest.raises(ErrorEnAsignatura):
        universidad.eliminarAsignatura(asignatura)
        
# Test para la función anadirEstudiante en una universidad
def test_anadirEstudiante():
    universidad = Universidad('Universidad de Murcia', 'Murcia')
    estudiante = Estudiante("Adrian", "11222333A", "Avenida Santa Monica", Sexo.V)

    universidad.anadirEstudiante(estudiante)

    assert estudiante in universidad._estudiantes

def test_anadirEstudiante_incorrecto():
    universidad = Universidad('Universidad de Murcia', 'Murcia')
    estudiante = "Luis"

    with pytest.raises(ErrorEnEstudiante):
        universidad.anadirEstudiante(estudiante)

# Test para la función eliminarEstudiante en una universidad
def test_eliminarEstudiante():
    universidad = Universidad('Universidad de Murcia', 'Murcia')
    estudiante = Estudiante("Adrian", "11222333A", "Avenida Santa Monica", Sexo.V)
    
    universidad.anadirEstudiante(estudiante)
    
    universidad.eliminarEstudiante(estudiante)

    assert estudiante not in universidad._estudiantes

def test_eliminarEstudiante_incorrecto():
    universidad = Universidad('Universidad de Murcia', 'Murcia')
    estudiante = "Pedro"

    with pytest.raises(ErrorEnEstudiante):
        universidad.eliminarEstudiante(estudiante)