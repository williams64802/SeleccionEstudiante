def test_agregar_estudiante(self):
    resultado = self.sorteo.agregar_estudiante(apellidoPaterno="Acevedo", apellidoMaterno="Ponce",
                                               nombres="Miguel Angel ", elegible=True)
    self.assertEqual(resultado, True)


def test_agregar_estudiante_repetido(self):
    resultado = self.sorteo.agregar_estudiante(apellidoPaterno="Garcia", apellidoMaterno="Mateo",
                                               nombres="Miguel Angel", elegible=True)
    self.assertNotEqual(resultado, True)


# aca falta modificar
def test_verificar_almacenamiento_agregar_estudiante(self):
    self.sorteo.agregar_estudiante(apellidoPaterno="Acevedo", apellidoMaterno="Ponce", nombres="Miguel Angel",
                                   elegible=True)
    self.session = Session()
    estudiante = self.session.query(Estudiante).filter(Estudiante.nombres == "Miguel Angel").first()

    self.assertEqual("Miguel Angel", estudiante.nombres)


def test_agregar_estudiante_vacio(self):
    resultado = self.sorteo.agregar_estudiante(apellidoPaterno="", apellidoMaterno="", nombres="", elegible=True)
    self.assertFalse(resultado)