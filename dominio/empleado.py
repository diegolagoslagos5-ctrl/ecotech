class Empleado:
    def __init__(self, id_unico, nombre, direccion, numero_telefono, direccion_correo_electronico, fecha_inicio_contrato, salario):
        self.__id_unico = id_unico 
        self._nombre = nombre  
        self.__direccion = direccion  
        self.__numero_telefono = numero_telefono 
        self.__direccion_correo_electronico = direccion_correo_electronico 
        self.__fecha_inicio_contrato = fecha_inicio_contrato 
        self.__salario = salario  

    def registrar_empleado(self):
        print("Empleado registrado")
        print("ID unico:", self.__id_unico)
        print("Nombre:", self._nombre)
        print("Direccion:", self.__direccion)
        print("Numero de telefono:", self.__numero_telefono)
        print("Correo electronico:", self.__direccion_correo_electronico)
        print("Fecha de inicio de contrato:", self.__fecha_inicio_contrato)
        print("Salario:", self.__salario)