class Departamento:
    """Representa un departamento de la empresa EcoTech Solutions y su gerente asociado"""
    def __init__(self, nombre, gerente_asociado):
        self.__nombre = nombre  
        self.__gerente_asociado = gerente_asociado 

    def registrar_departamento(self):
        print("Departamento registrado")
        print("Nombre:", self.__nombre)
        print("Gerente asociado:", self.__gerente_asociado)
