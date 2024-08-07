from conexion import Conexion
import time
from os import system
import getpass
import os

conexion = Conexion()
cursor = conexion.conexion.cursor()
cursor1 = conexion.conexion.cursor()
class Personaje:
    
    def fetch_options(table_name):
        cursor.execute(f"SELECT id, nombre FROM {table_name}")
        uso = cursor.fetchall()
        return uso 

    def fetch_habilidades(raza):
        
        cursor.execute("SELECT h.id, h.nombre FROM habilidades h JOIN raza r ON h.raza_id = r.id WHERE r.id = %s", (raza,))
        habilidades = cursor.fetchall() 
        return habilidades

    def fetch_poderes(raza):
        
        cursor.execute("SELECT p.id, p.nombre FROM poderes p JOIN raza r ON p.raza_id = r.id WHERE r.id = %s", (raza,))
        poderes = cursor.fetchall()
        return poderes 
        
    def elegir_opcion(mensaje, opciones):
        
        print(mensaje)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion[1]}")
        eleccion = int(input("Elige una opción: ")) - 1
        while eleccion < 0 or eleccion >= len(opciones):
            eleccion = int(input("Opción no válida. Elige una opción: ")) - 1
        return opciones[eleccion]

    def elegir_habilidades(raza):
        print("Elige dos habilidades básicas:")
        habilidades = Personaje.fetch_habilidades(raza)
        habilidad1 = Personaje.elegir_opcion("Elige la primera habilidad básica:", habilidades)
        habilidad2 = Personaje.elegir_opcion("Elige la segunda habilidad básica:", habilidades)
        while habilidad1 == habilidad2:
            print("No puedes elegir la misma habilidad dos veces.")
            habilidad2 = Personaje.elegir_opcion("Elige la segunda habilidad básica:", habilidades)
        
        return  [habilidad1[1], habilidad2[1]]

    def elegir_equipamiento():
        equipamientos = Personaje.fetch_options("equipamientos")
        return Personaje.elegir_opcion("Elige un equipamiento:", equipamientos)

    def elegir_poder(raza):
        poderes = Personaje.fetch_poderes(raza)
        return Personaje.elegir_opcion("Elige un poder especial:", poderes)

    def crear_personaje():
        """Crear personaje"""
        nombre = input("Nombre del personaje: ")

        razas = Personaje.fetch_options("raza")
        raza = Personaje.elegir_opcion("Elige una raza:", razas)
        system('cls')
        
        """Elegir habilidades, equipamiento y poder"""
        habilidades = Personaje.elegir_habilidades(raza[0])
        equipamiento = Personaje.elegir_equipamiento()
        poder = Personaje.elegir_poder(raza[0])
        system('cls')
        
        """Estado del jugador"""
        estado = "vivo"

        """Resumen personaje"""
        personaje = {
            "nombre": nombre,
            "raza": raza[1],
            "habilidades": habilidades,
            "equipamiento": equipamiento[1],
            "poder": poder[1],
            "estado": estado
        }
        
        Personaje.guardar_personaje_db(personaje)
        system('cls')
        return personaje

    def guardar_personaje_db(personaje):
        raza_id_query = "SELECT id FROM raza WHERE nombre = %s"
        cursor.execute(raza_id_query, (personaje['raza'],))
        raza_id = cursor.fetchall()

        habilidades_id_query = "SELECT id FROM habilidades WHERE nombre = %s"
        cursor.execute(habilidades_id_query, (personaje['habilidades'][0],))
        habilidad1_id = cursor.fetchall()
        
        cursor.execute(habilidades_id_query, (personaje['habilidades'][1],))
        habilidad2_id = cursor.fetchall()
        
        habilidad_id = [habilidad1_id, habilidad2_id]

        equipamiento_id_query = "SELECT id FROM equipamientos WHERE nombre = %s"
        cursor.execute(equipamiento_id_query, (personaje['equipamiento'],))
        equipamiento_id = cursor.fetchall()

        poder_id_query = "SELECT id FROM poderes WHERE nombre = %s"
        cursor.execute(poder_id_query, (personaje['poder'],))
        poder_id = cursor.fetchall()

        estado_id_query = "SELECT id FROM estados WHERE nombre = %s"
        cursor.execute(estado_id_query, (personaje['estado'],))
        estado_id = cursor.fetchall()

        cursor.execute(
            "INSERT INTO personaje (nombre, raza_id, habilidad_id, equipamiento_id, poderes_id, estados_id) VALUES (%s, %s, %s, %s, %s, %s)",
            (personaje['nombre'], raza_id, habilidad_id, equipamiento_id, poder_id, estado_id)
        )
        conexion.conexion.commit()

    def mostrar_personajes():
        cursor.execute("SELECT * FROM personaje")
        personajes = cursor.fetchall()

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
                mostrar_personaje(personajes[eleccion])

    def mostrar_personaje( personaje):
        print(f"\nResumen del personaje:")
        print(f"  Nombre: {personaje[1]}")
        print(f"  Raza ID: {personaje[2]}")
        print(f"  Habilidad ID: {personaje[3]}")    
        print(f"  Equipamiento ID: {personaje[4]}")
        print(f"  Poder ID: {personaje[5]}")
        print(f"  Estado ID: {personaje[6]}")

    def eliminar_personaje():
        cursor.execute("SELECT * FROM personaje")
        personajes = cursor.fetchall()

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
                cursor.execute("DELETE FROM personaje WHERE id = %s", (personaje_a_eliminar[0],))
                conexion.conexion.commit()
                print(f"Personaje {personaje_a_eliminar[1]} eliminado.")
                
    def agregarEquipamiento(): 
        pass
    
    def eliminarEquipamiento(): 
        pass
                         