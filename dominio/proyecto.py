class Proyecto:
    """Representa un proyecto de desarrollo o innovación gestionado en la empresa"""
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.__nombre = nombre
        self.__descripcion = descripcion 
        self.__fecha_inicio = fecha_inicio 

    def registrar_proyecto(self):
        print("Proyecto registrado")
        print("Nombre:", self.__nombre)
        print("Descripcion:", self.__descripcion)
        print("Fecha de inicio:", self.__fecha_inicio)
