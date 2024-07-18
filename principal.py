from beautifultable import BeautifulTable
from GameMaster import GameMaster
from Personaje import Personaje
from conexion import Conexion
import time
from os import system
import getpass
import os



def menu():
    menu = BeautifulTable()
    menu.column_headers = ['==== INICIO DEL SISTEMA ====']  
    menu.rows.append(['1.- Conectar'])
    menu.rows.append(['2.- Salir'])
    menu.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu)  

def menuPrincipal():
    menu1 = BeautifulTable()
    menu1.column_headers = ['==== MENÚ ====']
    menu1.rows.append(['1.- Jugador'])
    menu1.rows.append(['2.- Game Master'])
    menu1.rows.append(['3.- Salir'])
    menu1.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu1)

def menuUsuario():
    menuU = BeautifulTable()
    menuU.column_headers = ['==== MENU JUGADOR ====']
    menuU.append_row(['1.- Crear personaje'])
    menuU.append_row(['2.- Listar personajes creados'])
    menuU.append_row(['3.- Modificar equipamiento'])
    menuU.append_row(['4.- Salir'])
    menuU.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menuU)

def menuGameMaster():
    menuG = BeautifulTable()
    menuG.column_headers= ['==== MENU GAME MASTER']
    menuG.append_row(['1.- Listar jugadores'])
    menuG.append_row(['2.- Completar personajes'])
    menuG.append_row(['3.- Editar datos'])
    menuG.append_row(['4.- Salir'])
    menuG.columns.alignment = BeautifulTable.ALIGN_LEFT 
    print(menuG)

def menuGameMaster2():
    menuG2=BeautifulTable()
    menuG2.column_headers = ['==== EDITAR DATOS ====']
    menuG2.append_row(['1.- Editar equipamiento'])
    menuG2.append_row(['2.- Editar poderes'])
    menuG2.append_row(['3.- Editar habilidades'])
    menuG2.append_row(['4.- Editar estados'])
    menuG2.append_row(['5.- Editar raza'])
    menuG2.append_row(['6.- Subir nivel de un jugador'])
    menuG2.append_row(['7.- Volver'])
    menuG2.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menuG2)

def menuGameMaster3():
    menuG3 = BeautifulTable()
    menuG3.column_headers = ['===== EDITAR EQUIPAMIENTO ====']
    menuG3.append_row(['1.- Agregar equipamento'])
    menuG3.append_row(['2.- Modificar equipamento'])
    menuG3.append_row(['3.- Eliminar equipamento'])
    menuG3.append_row(['4.- Volver'])
    menuG3.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menuG3)

def menuGameMaster4():
    menuG4 = BeautifulTable()
    menuG4.column_headers = ['===== EDITAR PODERES =====']
    menuG4.append_row(['1.- Agregar poder'])
    menuG4.append_row(['2.- Modificar poder'])
    menuG4.append_row(['3.- Eliminar poder'])
    menuG4.append_row(['4.- Volver'])
    menuG4.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menuG4)

def menuGameMaster5():
    menuG5 = BeautifulTable()
    menuG5.column_headers = ['===== EDITAR HABILIDADES =====']
    menuG5.append_row(['1.- Agregar habilidad'])
    menuG5.append_row(['2.- Modificar habilidad'])
    menuG5.append_row(['3.- Eliminar habilidad'])
    menuG5.append_row(['4.- Volver'])
    menuG5.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menuG5)

def menuGameMaster6():
    menuG6 = BeautifulTable()
    menuG6.column_headers = ['===== EDITAR ESTADOS =====']
    menuG6.append_row(['1.- Agregar estado'])
    menuG6.append_row(['2.- Modificar estado'])
    menuG6.append_row(['3.- Eliminar estado'])
    menuG6.append_row(['4.- Volver'])
    menuG6.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menuG6)

def menuGameMaster7():
    menuG7 = BeautifulTable()
    menuG7.column_headers = ['===== EDITAR RAZAS =====']
    menuG7.append_row(['1.- Agregar raza'])
    menuG7.append_row(['2.- Eliminar raza'])
    menuG7.append_row(['3.- Volver'])
    menuG7.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menuG7)

def user():
    conexion = Conexion()
    conexion.crearUsuario()
    time.sleep(3)
    
def principal():
    conexion = Conexion()
    intentos = 3

    while True:
        menu()
        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            usuario = input('Ingrese su nombre de usuario: ')
            clave = getpass.getpass('Ingrese su contraseña: ')
            clave_encriptada = conexion.encriptarPwd(clave)

            cursor = conexion.conexion.cursor()
            nombre = cursor.execute("SELECT nombre, clave FROM usuario WHERE nombre = %s", (usuario))      
            nombre = nombre[0]
            pwd = nombre[1]
            if nombre == usuario and pwd == clave_encriptada:
                print('Credenciales correctas. ¡Bienvenido!')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')

                while True:
                    menuPrincipal()
                    opcion_principal = input('Ingrese una opción: ')

                    if opcion_principal == '1':
                        print('Bienvenido Jugador')
                        menuUsuario()

                    elif opcion_principal == '2':
                        print('Bienvenido Game Master')
                        menuGameMaster()

                    elif opcion_principal == '3':
                        confirmacion = input('¿Está seguro que desea salir? (si/no): ')
                        if confirmacion.lower() == 'si':
                            print('Saliendo del programa...')
                            break
                        elif confirmacion.lower() == 'no':
                            print('Cancelando salida.')
                        else:
                            print('Opción no válida.')

                    else:
                        print('Opción no válida. Por favor, ingrese una opción válida.')

                break

            else:
                intentos -= 1
                print(f'Credenciales incorrectas. Intentos restantes: {intentos}')
                if intentos <= 0:
                    print('Has agotado tus intentos. Saliendo del programa...')
                    break

        elif opcion == '2':
            print('Saliendo del programa...')
            break

        else:
            print('Opción no válida. Por favor, ingrese una opción válida.')

if __name__ == "__main__":
    user()
    principal()




