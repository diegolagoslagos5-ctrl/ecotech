class Asignacion:
    def __init__(self, fecha, horas_trabajadas, tareas_realizadas):
        self.fecha = fecha                  # +publico
        self.horas_trabajadas = horas_trabajadas  # +publico
        self.tareas_realizadas = tareas_realizadas # +publico

    def registro_horas_trabajadas(self, conexion, cursor, horas: int):
        try:
            self.horas_trabajadas += horas
            cursor.execute("""
                UPDATE asignacion 
                SET horas_trabajadas = %s 
                WHERE fecha = %s AND tareas_realizadas = %s
            """, (self.horas_trabajadas, self.fecha, self.tareas_realizadas))
            conexion.commit()
            
            print(f"Se han registrado {horas} horas. Total: {self.horas_trabajadas}.")
        except Exception as e:
            print(f"Error al registrar horas en la base de datos: {e}")
