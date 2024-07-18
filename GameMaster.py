import psycopg2
from psycopg2 import sql

class GameMaster:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=juegorol user=root password=password")
        self.cur = self.conn.cursor()

    def obtener_poderes(self):
        try:
            self.cur.execute("SELECT nombre FROM poderes")
            poderes = [row[0] for row in self.cur.fetchall()]
            return poderes
        except psycopg2.Error as e:
            print(f"Error al obtener poderes: {e}")
            return []

    def obtener_habilidades(self):
        try:
            self.cur.execute("SELECT nombre FROM habilidades")
            habilidades = [row[0] for row in self.cur.fetchall()]
            return habilidades
        except psycopg2.Error as e:
            print(f"Error al obtener habilidades: {e}")
            return []

    def actualizar_detalle(self, tipo, nombre, nuevo_detalle):
        try:
            self.cur.execute(
                sql.SQL("UPDATE {} SET descripcion = %s WHERE nombre = %s").format(sql.Identifier(tipo)),
                (nuevo_detalle, nombre)
            )
            self.conn.commit()
            print(f"Detalle actualizado correctamente para {nombre}.")
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error al actualizar detalle: {e}")

    def ver_personajes(self):
        try:
            self.cur.execute("SELECT * FROM personaje")
            personajes = self.cur.fetchall()
            for personaje in personajes:
                print(personaje)
        except psycopg2.Error as e:
            print(f"Error al ver personajes: {e}")

    def agregar_raza(self, nombre):
        try:
            self.cur.execute(
                "INSERT INTO raza (nombre) VALUES (%s)",
                (nombre,)
            )
            self.conn.commit()
            print(f"Raza '{nombre}' agregada correctamente.")
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error al agregar raza: {e}")

    def modificar_equipamiento(self, nombre, nuevo_nombre):
        try:
            self.cur.execute(
                "UPDATE equipamientos SET nombre = %s WHERE nombre = %s",
                (nuevo_nombre, nombre)
            )
            self.conn.commit()
            print(f"Equipamiento '{nombre}' modificado a '{nuevo_nombre}'.")
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error al modificar equipamiento: {e}")

    def agregar_estado(self, nombre):
        try:
            self.cur.execute(
                "INSERT INTO estados (nombre) VALUES (%s)",
                (nombre,)
            )
            self.conn.commit()
            print(f"Estado '{nombre}' agregado correctamente.")
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error al agregar estado: {e}")

    def mostrar_menu(self):
        print("\nMenú:")
        print("1. Ver poderes")
        print("2. Ver habilidades")
        print("3. Actualizar detalle de habilidad o poder")
        print("4. Ver todos los personajes")
        print("5. Agregar nueva raza")
        print("6. Modificar equipamiento")
        print("7. Agregar nuevo estado")
        print("8. Salir")

    def main(self):
        while True:
            self.mostrar_menu()
            opcion = input("Elige una opción: ")

            if opcion == "1":
                poderes = self.obtener_poderes()
                print("Poderes disponibles:", poderes)
            elif opcion == "2":
                habilidades = self.obtener_habilidades()
                print("Habilidades disponibles:", habilidades)
            elif opcion == "3":
                tipo = input("Ingrese tipo (habilidad/poder): ").lower()
                nombre = input("Ingrese el nombre: ")
                nuevo_detalle = input("Ingrese el nuevo detalle: ")
                self.actualizar_detalle(tipo, nombre, nuevo_detalle)
            elif opcion == "4":
                self.ver_personajes()
            elif opcion == "5":
                nombre_raza = input("Ingrese el nombre de la nueva raza: ")
                self.agregar_raza(nombre_raza)
            elif opcion == "6":
                nombre_equipamiento = input("Ingrese el nombre del equipamiento a modificar: ")
                nuevo_nombre = input("Ingrese el nuevo nombre del equipamiento: ")
                self.modificar_equipamiento(nombre_equipamiento, nuevo_nombre)
            elif opcion == "7":
                nombre_estado = input("Ingrese el nombre del nuevo estado: ")
                self.agregar_estado(nombre_estado)
            elif opcion == "8":
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    gm = GameMaster()
    gm.main()


