class Informe:
    """Gestiona los datos y el contenido de los informes generados en el sistema"""
    def __init__(self, id_informe, fecha_generacion, contenido):
        self.__id_informe = id_informe 
        self.__fecha_generacion = fecha_generacion 
        self.__contenido = contenido 

    def registrar_informe(self):
        print("Informe registrado")
        print("ID informe:", self.__id_informe)
        print("Fecha de generacion:", self.__fecha_generacion)
        print("Contenido:", self.__contenido)
