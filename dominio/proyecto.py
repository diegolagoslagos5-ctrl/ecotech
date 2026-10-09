class Proyecto:
    def __init__(self, nombre, descripcion_proyecto, fecha_de_inicio, miembro, presupuesto):
        self.nombre = nombre  # +publico
        self._descripcion_proyecto = descripcion_proyecto  # #protegido
        self._fecha_de_inicio = fecha_de_inicio  # #protegido
        self._miembro = miembro # #protegido
        self._presupuesto = presupuesto # #protegido

    def creacion_proyecto(self, conexion, cursor):
        try:
            cursor.execute("""
                INSERT INTO proyecto (nombre, descripcion_proyecto, fecha_de_inicio, miembro, presupuesto) 
                VALUES (%s, %s, %s, %s, %s)
            """, (self.nombre, self._descripcion_proyecto, self._fecha_de_inicio, self._miembro, self._presupuesto))
            conexion.commit()
            print(f"Proyecto '{self.nombre}' creado en la base de datos.")
        except Exception as e:
            print(f"Error crítico al intentar crear el proyecto: {e}")

    def edicion_proyecto(self, conexion, cursor, nuevo_nombre, nueva_descripcion, nueva_fecha):
        try:
            cursor.execute("""
                UPDATE proyecto 
                SET nombre = %s, descripcion_proyecto = %s, fecha_de_inicio = %s 
                WHERE nombre = %s
            """, (nuevo_nombre, nueva_descripcion, nueva_fecha, self.nombre))
            conexion.commit()
            
            self.nombre = nuevo_nombre
            self._descripcion_proyecto = nueva_descripcion
            self._fecha_de_inicio = nueva_fecha
            print("El proyecto ha sido editado correctamente.")
        except Exception as e:
            print(f"Error crítico al intentar editar el proyecto: {e}")

    def eliminacion_proyecto(self, conexion, cursor):
        try:
            cursor.execute("""
                DELETE FROM proyecto WHERE nombre = %s
            """, (self.nombre,))
            conexion.commit()
            print("Proyecto eliminado de la base de datos.")
        except Exception as e:
            print(f"Error crítico al intentar eliminar el proyecto: {e}")
