from conexion import Conexion
import time
from os import system
conexion = Conexion()
cursor = conexion.conexion.cursor()

class GameMaster: 
    
    def listarJugadores():
        cursor.execute("select p.nombre, r.nombre, p.nivel, e.nombre from ((personaje p join raza r on p.raza_id = r.id) join estados e on p.estado_id = e.id) where e.nombre = %s",('vivo',))
        mostrar = cursor.fetchall()
        if mostrar == []:
            print('No existen datos')
            time.sleep(5)
            system('cls')
        else:
            print(mostrar)
    
    def completarPersonajes():
        sentencia = "select * from personaje"
        cursor.execute(sentencia)
        personajes = cursor.fetchall()
        print('Personajes:')
        for personaje in personajes:
            print(personaje)
        id = int(input('Ingrese el id del personaje a completar: '))
        sentencia = "select * from personaje where id = %s"
        cursor.execute(sentencia, (id,))
        personaje = cursor.fetchone()
        print('Personaje seleccionado:')
        print(personaje)
        print('Completar personaje:')
        nombre = input('Ingrese el nombre del personaje: ')
        raza = input('Ingrese la raza del personaje: ')
        habilidad = input('Ingrese la habilidad del personaje: ')
        equipamiento = input('Ingrese el equipamiento del personaje: ')
        poder = input('Ingrese el poder del personaje: ')
        estado = input('Ingrese el estado del personaje: ')
        sentencia = "update personaje set nombre = %s, raza = %s, habilidad = %s, equipamiento = %s, poder = %s, estado = %s where id = %s"
        cursor.execute(sentencia, (nombre, raza, habilidad, equipamiento, poder, estado, id))
        conexion.conexion.commit()
        print('Personaje completado')
        time.sleep(2)
        system('cls')

    
    def agregarPoder():
        sentencia = "select * from poderes"
        cursor.execute(sentencia)
        poderes = cursor.fetchall()
        print('Poderes:')
        for poder in poderes:
            print(poder)
            
        nombre = input('Ingrese el nombre del poder: ')
        descripcion = input('Ingrese la descripción del poder: ')
        sentencia = "insert into poderes (nombre, descripcion) values (%s, %s)"
        cursor.execute(sentencia, (nombre, descripcion))
        conexion.conexion.commit()
        print('Poder agregado')
        time.sleep(2)
        system('cls')

        
        
        
    def eliminarPoder():
        sentencia = "select * from poderes"
        cursor.execute(sentencia)
        poderes = cursor.fetchall()
        print('Poderes:')
        for poder in poderes:
            print(poder)

        id = int(input('Ingrese el id del poder a eliminar: '))
        sentencia = "delete from poderes where id = %s"
        confirmacion = input('¿Está seguro que desea eliminar el poder? (s/n): ')
        if confirmacion == 's':
            cursor.execute(sentencia, (id,))
            conexion.conexion.commit()
            print('Poder eliminado')
            time.sleep(2)
            system('cls')
        elif confirmacion == 'n':
            print('Operación cancelada')
            time.sleep(2)
            system('cls')
        else:
            print('Opción no válida')
            time.sleep(2)
            system('cls')
        
        
        
        
    def editarPoder():
        sentencia = "select * from poderes"
        cursor.execute(sentencia)
        poderes = cursor.fetchall()
        print('Poderes:')
        for poder in poderes:
            print(poder)
            
        id = int(input('Ingrese el id del poder a editar: '))
        sentencia= "select * from poderes where id = %s"
        cursor.execute(sentencia, (id,))
        res=cursor.fetchone()
        if res is None:
            print('El poder no existe')
            time.sleep(2)
            system('cls')
        else:
            nombre = input('Ingrese el nuevo nombre del poder: ')
            descripcion = input('Ingrese la nueva descripción del poder: ')
            sentencia = "update poderes set nombre = %s, descripcion = %s where id = %s"
            cursor.execute(sentencia, (nombre, descripcion, id))
            conexion.conexion.commit()
            print('Poder actualizado')
            time.sleep(2)
            system('cls')
        
    
    
    
    def agregarHabilidad():
        sentencia = "select * from habilidades"
        cursor.execute(sentencia)
        habilidades = cursor.fetchall()
        print('Habilidades:')
        for habilidad in habilidades:
            print(habilidad)
            
        nombre = input('Ingrese el nombre de la habilidad: ')
        descripcion = input('Ingrese la descripción de la habilidad: ')
        sentencia = "insert into habilidades (nombre, descripcion) values (%s, %s)"
        cursor.execute(sentencia, (nombre, descripcion))
        conexion.conexion.commit()
        print('Habilidad agregada')
        time.sleep(2)
        system('cls')
        
        
        
        
    def eliminarHabilidad():
        sentencia = "select * from habilidades"
        cursor.execute(sentencia)
        habilidades = cursor.fetchall()
        print('Habilidades:')
        for habilidad in habilidades:
            print(habilidad)
            
        id = int(input('Ingrese el id de la habilidad a eliminar: '))
        sentencia = "delete from habilidades where id = %s"
        confirmacion = input('¿Está seguro que desea eliminar la habilidad? (s/n): ')
        if confirmacion == 's':
            cursor.execute(sentencia, (id,))
            conexion.conexion.commit()
            print('Habilidad eliminada')
            time.sleep(2)
            system('cls')
        elif confirmacion == 'n':
            print('Operación cancelada')
            time.sleep(2)
            system('cls')
        else:
            print('Opción no válida')
            time.sleep(2)
            system('cls')
        
        
        
        
    def editarHabilidad():
        sentencia = "select * from habilidades"
        cursor.execute(sentencia)
        habilidades = cursor.fetchall()
        print('Habilidades:')
        for habilidad in habilidades:
            print(habilidad)

        id = int(input('Ingrese el id de la habilidad a editar: '))
        nombre = input('Ingrese el nuevo nombre de la habilidad: ')
        descripcion = input('Ingrese la nueva descripción de la habilidad: ')
        sentencia = "update habilidades set nombre = %s and descripcion = %s where id = %s"
        cursor.execute(sentencia, (nombre, descripcion, id))
        conexion.conexion.commit()
        print('Habilidad actualizada')
        time.sleep(2)
        system('cls')
        
        
    def agregarEquipamiento(): 
        sentencia = "select * from equipamiento"
        cursor.execute(sentencia)
        equipamientos = cursor.fetchall()
        print('Equipamientos:')
        for equipamiento in equipamientos:
            print(equipamiento)
            
        nombre = input('Ingrese el nombre del equipamiento: ')
        descripcion = input('Ingrese la descripción del equipamiento: ')
        sentencia = "insert into equipamiento (nombre, descripcion) values (%s, %s)"
        cursor.execute(sentencia, (nombre, descripcion))
        conexion.conexion.commit()
        print('Equipamiento agregado')
        time.sleep(2)
        system('cls')
    
    
    
    def eliminarEquipamiento():
        sentencia = "select * from equipamiento"
        cursor.execute(sentencia)
        equipamientos = cursor.fetchall()
        print('Equipamientos:')
        for equipamiento in equipamientos:
            print(equipamiento)
            
        id = int(input('Ingrese el id del equipamiento a eliminar: '))
        sentencia = "delete from equipamiento where id = %s"
        
        confirmacion = input('¿Está seguro que desea eliminar el equipamiento? (s/n): ')
        if confirmacion == 's':
            cursor.execute(sentencia, (id,))
            conexion.conexion.commit()
            print('Equipamiento eliminado')
            time.sleep(2)
            system('cls')
        elif confirmacion == 'n':
            print('Operación cancelada')
            time.sleep(2)
            system('cls')
        else:
            print('Opción no válida')
            time.sleep(2)
            system('cls')
        
    def editarEquipamiento():
        sentencia = "select * from equipamiento"
        cursor.execute(sentencia)
        equipamientos = cursor.fetchall()
        print('Equipamientos:')
        for equipamiento in equipamientos:
            print(equipamiento)
            
        id = int(input('Ingrese el id del equipamiento a editar: '))
        nombre = input('Ingrese el nuevo nombre del equipamiento: ')
        descripcion = input('Ingrese la nueva descripción del equipamiento: ')
        sentencia = "update equipamiento set nombre = %s and descripcion = %s where id = %s"
        cursor.execute(sentencia, (nombre, descripcion, id))
        conexion.conexion.commit()
        print('Equipamiento actualizado')
        time.sleep(2)
        system('cls')
    
    
    def agregarRaza():
        sentencia = "select id, nombre from raza"
        cursor.execute(sentencia)
        razas = cursor.fetchall()
        print('Razas:')
        for raza in razas:
            print(raza)
        
        nombre = input('Ingrese el nombre de la raza: ')
        descripcion = input('Ingrese la descripción de la raza: ')
        sentencia = "insert into raza (nombre, descripcion) values (%s, %s)"
        cursor.execute(sentencia, (nombre, descripcion))
        conexion.conexion.commit()
        print('Raza agregada')
        time.sleep(2)
        system('cls')
        
        
        
        
    def eliminarRaza():
        sentencia = "select id, nombre from raza"
        cursor.execute(sentencia)
        razas = cursor.fetchall()
        print('Razas:')
        for raza in razas:
            print(raza)
        
        id = int(input('Ingrese el id de la raza a eliminar: '))
        sentencia = "delete from raza where id = %s"
        confirmacion = input('¿Está seguro que desea eliminar la raza? (s/n): ')
        if confirmacion == 's':
            cursor.execute(sentencia, (id,))
            conexion.conexion.commit()
            print('Raza eliminada')
            time.sleep(2)
            system('cls')
        elif confirmacion == 'n':
            print('Operación cancelada')
            time.sleep(2)
            system('cls')
        else:
            print('Opción no válida')
            time.sleep(2)
            system('cls')
    
    
    
    def editarRaza(): 
        sentencia = "select id, nombre from raza"
        cursor.execute(sentencia)
        razas = cursor.fetchall()
        print('Razas:')
        for raza in razas:
            print(raza)
        
        id = int(input('Ingrese el id de la raza a editar: '))
        nombre = input('Ingrese el nuevo nombre de la raza: ')
        descripcion = input('Ingrese la nueva descripción de la raza: ')
        sentencia = "update raza set nombre = %s and descripcion =%s where id = %s"
        cursor.execute(sentencia, (nombre, id))
        conexion.conexion.commit()
        print('Raza actualizada')
        time.sleep(2)
        system('cls')
        

    def agregarEstado():
        sentencia = "select id, nombre from estado"
        cursor.execute(sentencia)
        estados = cursor.fetchall()
        print('Estados:')
        for estado in estados:
            print(estado)
            
        estado = input('Ingrese el estado a agregar: ')
        sentencia = "insert into estado (nombre) values (%s)"
        cursor.execute(sentencia, (estado,))
        conexion.conexion.commit()
        print('Estado agregado')
        time.sleep(2)
        system('cls')
    
    
    def eliminarEstado():
        sentencia = "select id, nombre from estado"
        cursor.execute(sentencia)
        estados = cursor.fetchall()
        print('Estados:')
        for estado in estados:
            print(estado)
            
        id = int(input('Ingrese el id del estado a eliminar: '))
        sentencia = "delete from estado where id = %s"
        if id == 1:
            print('No se puede eliminar el estado "vivo')
            time.sleep(2)
            system('cls')
        elif id == 2:
            print('No se puede eliminar el estado "Muerto"')
            time.sleep(2)
            system('cls')
        else:
            cursor.execute(sentencia, (id,))
            conexion.conexion.commit()
            print('Estado eliminado')
            time.sleep(2)
            system('cls')
    

    def cambiarEstado(id, estado):
        sentencia = "update personaje set estado = %s where id = %s"
        cursor.execute(sentencia, (estado, id))
        conexion.conexion.commit()
        print('Estado actualizado')
        time.sleep(2)
        system('cls')
    
    
    def subirNivel(id, nivel):
        sentencia= "select nivel from personaje where id = %s"
        cursor.execute(sentencia, (id,))
        nivelActual = cursor.fetchone()[0]
        
        if nivel > nivelActual:
            sentencia = "update personaje set nivel = %s where id = %s"
            cursor.execute(sentencia, (nivel, id))
            conexion.conexion.commit()
            print('Nivel actualizado')
        else:
            print('El nivel ingresado es menor al actual')
        time.sleep(2)
        system('cls')