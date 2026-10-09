class Departamento:
    def __init__(self, nombre, gerente_id, departamento):
        self.nombre = nombre   # +publico
        self._gerente_id = gerente_id # #protegido
        self._departamento = departamento # #protegido

    def creacion_departamento(self, conexion, cursor):
        try:
            cursor.execute("""
                INSERT INTO departamento (nombre, departamento, gerente_id) 
                VALUES (%s, %s, %s)
            """, (self.nombre, self._departamento, self._gerente_id))
            conexion.commit()
            print(f"Departamento '{self.nombre}' creado exitosamente.")
        except Exception as e:
            print(f"Error crítico al intentar crear el departamento: {e}")

    def edicion_departamento(self, conexion, cursor, nuevo_nombre, nuevo_gerente_id):
        try:
            cursor.execute("""
                UPDATE departamento 
                SET nombre = %s, gerente_id = %s 
                WHERE departamento = %s
            """, (nuevo_nombre, nuevo_gerente_id, self._departamento))
            conexion.commit()
            
            self.nombre = nuevo_nombre
            self._gerente_id = nuevo_gerente_id
            print("Edición del departamento realizada exitosamente.")
        except Exception as e:
            print(f"Error al editar el departamento: {e}")

    def busqueda_departamento(self, cursor):
        try:
            cursor.execute("""
                SELECT id_departamento, nombre, departamento, gerente_id 
                FROM departamento WHERE nombre = %s FOR UPDATE
            """, (self.nombre,))
            resultado = cursor.fetchone()
            if resultado:
                print("Departamento encontrado:", resultado)
            else:
                print("El departamento no existe en la base de datos.")
        except Exception as e:
            print(f"Error en la búsqueda: {e}")

    def eliminacion_departamento(self, conexion, cursor):
        try:
            cursor.execute("""
                DELETE FROM departamento WHERE nombre = %s
            """, (self.nombre,))
            conexion.commit()
            print("Departamento eliminado.")
        except Exception as e:
            print(f"Error al eliminar el departamento: {e}")
