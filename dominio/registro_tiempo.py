class RegistroTiempo:
    """Controla el registro de horas y actividades realizadas por los empleados."""
    def __init__(self, fecha, horas_trabajadas, descripcion_tarea):
        self.__fecha = fecha  
        self.__horas_trabajadas = horas_trabajadas 
        self.__descripcion_tarea = descripcion_tarea 

    def registrar_tiempo(self):
        print("Registro de tiempo guardado")
        print("Fecha:", self.__fecha)
        print("Horas trabajadas:", self.__horas_trabajadas)
        print("Descripcion de tarea:", self.__descripcion_tarea)
