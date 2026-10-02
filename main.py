from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.proyecto import Proyecto
from dominio.registro_tiempo import RegistroTiempo

def main():
    empleado1 = Empleado(1, "Diego Lagos", "Concepción", 987654321, "diego@mail.com", "2024-01-01", 850000.0)
    dep1 = Departamento("Desarrollo Sostenible", empleado1._nombre)
    
    print("Datos del Sistema EcoTech")
    empleado1.registrar_empleado()
    print("-" * 20)
    dep1.registrar_departamento()
    
    print("-" * 20)
    print(empleado1) 

if __name__ == "__main__":
    main()