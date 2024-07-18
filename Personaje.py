import psycopg2

class Personaje:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=juegorol user=root password=password")
        self.cursor = self.conn.cursor()

    def fetch_options(self, table_name):
        self.cursor.execute(f"SELECT nombre FROM {table_name}")
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_habilidades(self, raza):
        self.cursor.execute("SELECT h.nombre FROM habilidades h JOIN raza r ON h.raza_id = r.id WHERE r.nombre = %s", (raza,))
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_poderes(self, raza):
        self.cursor.execute("SELECT p.nombre FROM poderes p JOIN raza r ON p.raza_id = r.id WHERE r.nombre = %s", (raza,))
        return [row[0] for row in self.cursor.fetchall()]

    def elegir_opcion(self, mensaje, opciones):
        print(mensaje)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        eleccion = int(input("Elige una opción: ")) - 1
        while eleccion < 0 or eleccion >= len(opciones):
            eleccion = int(input("Opción no válida. Elige una opción: ")) - 1
        return opciones[eleccion]

    def elegir_habilidades(self, raza):
        print("Elige dos habilidades básicas:")
        habilidades = self.fetch_habilidades(raza)
        habilidad1 = self.elegir_opcion("Elige la primera habilidad básica:", habilidades)
        habilidad2 = self.elegir_opcion("Elige la segunda habilidad básica:", habilidades)
        while habilidad1 == habilidad2:
            print("No puedes elegir la misma habilidad dos veces.")
            habilidad2 = self.elegir_opcion("Elige la segunda habilidad básica:", habilidades)
        return [habilidad1, habilidad2]

    def elegir_equipamiento(self):
        equipamientos = self.fetch_options("equipamientos")
        return self.elegir_opcion("Elige un equipamiento:", equipamientos)

    def elegir_poder(self, raza):
        poderes = self.fetch_poderes(raza)
        return self.elegir_opcion("Elige un poder especial:", poderes)

    def crear_personaje(self):
        """Crear personaje"""
        nombre = input("Nombre del personaje: ")

        razas = self.fetch_options("raza")
        raza = self.elegir_opcion("Elige una raza:", razas)

        """Elegir habilidades, equipamiento y poder"""
        habilidades = self.elegir_habilidades(raza)
        equipamiento = self.elegir_equipamiento()
        poder = self.elegir_poder(raza)

        """Estado del jugador"""
        estado = "Vivo"

        """Resumen personaje"""
        personaje = {
            "nombre": nombre,
            "raza": raza,
            "habilidades": habilidades,
            "equipamiento": equipamiento,
            "poder": poder,
            "estado": estado
        }
        
        self.guardar_personaje_db(personaje)
        
        return personaje

    def guardar_personaje_db(self, personaje):
        raza_id_query = "SELECT id FROM raza WHERE nombre = %s"
        self.cursor.execute(raza_id_query, (personaje['raza'],))
        raza_id = self.cursor.fetchone()[0]

        habilidades_id_query = "SELECT id FROM habilidades WHERE nombre = %s"
        self.cursor.execute(habilidades_id_query, (personaje['habilidades'][0],))
        habilidad1_id = self.cursor.fetchone()[0]
        self.cursor.execute(habilidades_id_query, (personaje['habilidades'][1],))
        habilidad2_id = self.cursor.fetchone()[0]

        equipamiento_id_query = "SELECT id FROM equipamientos WHERE nombre = %s"
        self.cursor.execute(equipamiento_id_query, (personaje['equipamiento'],))
        equipamiento_id = self.cursor.fetchone()[0]

        poder_id_query = "SELECT id FROM poderes WHERE nombre = %s"
        self.cursor.execute(poder_id_query, (personaje['poder'],))
        poder_id = self.cursor.fetchone()[0]

        estado_id_query = "SELECT id FROM estados WHERE nombre = %s"
        self.cursor.execute(estado_id_query, (personaje['estado'],))
        estado_id = self.cursor.fetchone()[0]

        self.cursor.execute(
            "INSERT INTO personaje (nombre, raza_id, habilidad_id, equipamiento_id, poderes_id, estados_id) VALUES (%s, %s, %s, %s, %s, %s)",
            (personaje['nombre'], raza_id, habilidad1_id, equipamiento_id, poder_id, estado_id)
        )
        self.conn.commit()

    def mostrar_menu(self):
        print("Menu:")
        print("1. Crear personaje")
        print("2. Mostrar personajes")
        print("3. Eliminar personaje")
        print("4. Salir")

    def mostrar_personajes(self):
        self.cursor.execute("SELECT * FROM personaje")
        personajes = self.cursor.fetchall()

        if not personajes:
            print("\nNo hay personajes creados.")
        else:
            print("\nLista de personajes:")
            for idx, personaje in enumerate(personajes, 1):
                print(f"{idx}. {personaje[1]} (Raza ID: {personaje[2]}, Estado ID: {personaje[6]})")
            
            eleccion = int(input("\nElige el número del personaje que deseas ver: ")) - 1
            if eleccion < 0 or eleccion >= len(personajes):
                print("Opción no válida.")
            else:
                self.mostrar_personaje(personajes[eleccion])

    def mostrar_personaje(self, personaje):
        print(f"\nResumen del personaje:")
        print(f"  Nombre: {personaje[1]}")
        print(f"  Raza ID: {personaje[2]}")
        print(f"  Habilidad ID: {personaje[3]}")    
        print(f"  Equipamiento ID: {personaje[4]}")
        print(f"  Poder ID: {personaje[5]}")
        print(f"  Estado ID: {personaje[6]}")

    def eliminar_personaje(self):
        self.cursor.execute("SELECT * FROM personaje")
        personajes = self.cursor.fetchall()

        if not personajes:
            print("\nNo hay personajes creados.")
        else:
            print("\nLista de personajes:")
            for idx, personaje in enumerate(personajes, 1):
                print(f"{idx}. {personaje[1]} (Raza ID: {personaje[2]}, Estado ID: {personaje[6]})")

            eleccion = int(input("\nElige el número del personaje que deseas eliminar: ")) - 1
            if eleccion < 0 or eleccion >= len(personajes):
                print("Opción no válida.")
            else:
                personaje_a_eliminar = personajes[eleccion]
                self.cursor.execute("DELETE FROM personaje WHERE id = %s", (personaje_a_eliminar[0],))
                self.conn.commit()
                print(f"Personaje {personaje_a_eliminar[1]} eliminado.")

    def juego(self):
        while True:
            self.mostrar_menu()
            eleccion = int(input("Elige una opción: "))
            
            if eleccion == 1:
                self.crear_personaje()
            elif eleccion == 2:
                self.mostrar_personajes()
            elif eleccion == 3:
                self.eliminar_personaje()
            elif eleccion == 4:
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    juego = Personaje()
    juego.juego()

                         