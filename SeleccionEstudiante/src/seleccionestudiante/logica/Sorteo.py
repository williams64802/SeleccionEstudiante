from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.declarative_base import engine, Base, session

class Sorteo():

    def __init__(self):
        Base.metadata.create_all(engine)

    def _init_(self):
        Base.metadata.create_all(engine)

    def agregar_asignatura(self, nombreAsignatura):
        if (nombreAsignatura == ""):
            return False

        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombreAsignatura=nombreAsignatura)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False

    def agregar_estudiante(self, apellidoPaterno, apellidoMaterno, nombres, elegible):
        if (apellidoPaterno == ""):
            return False
        if (nombres == ""):
            return False


        busqueda = session.query(Estudiante).filter(Estudiante.apellidoPaterno == apellidoPaterno,
                                                    Estudiante.apellidoMaterno == apellidoMaterno,
                                                    Estudiante.nombres == nombres,
                                                    Estudiante.elegible == elegible).all()
        if len(busqueda) == 0:
            estudiante = Estudiante(apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno, nombres=nombres,
                                    elegible=elegible)
            session.add(estudiante)
            session.commit()
            return True
        else:
            return False