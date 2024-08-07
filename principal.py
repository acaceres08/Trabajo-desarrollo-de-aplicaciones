from beautifultable import BeautifulTable
from GameMaster import GameMaster
from Personaje import Personaje
from conexion import Conexion
import time
from os import system
import getpass
import os

class Proyecto:
    
    def menu():
        menu = BeautifulTable()
        menu.column_headers = ['===== INICIO DEL SISTEMA =====']
        menu.rows.append(['1.- Registrarse'])
        menu.rows.append(['2.- Iniciar Sesión'])
        menu.rows.append(['3.- Salir'])
        menu.columns.alignments = BeautifulTable.ALIGN_LEFT
        print(menu) 

    def menuPrincipal():
        menu1 = BeautifulTable()
        menu1.column_headers = ['===== OPCIÓN DE USUARIO =====']
        menu1.rows.append(['1.- Jugador'])
        menu1.rows.append(['2.- Game Master'])
        menu1.rows.append(['3.- Salir'])
        menu1.columns.alignment = BeautifulTable.ALIGN_LEFT
        print(menu1)

    def menuUsuario():
        menuU = BeautifulTable()
        menuU.column_headers = ['===== MENU JUGADOR =====']
        menuU.append_row(['1.- Crear personaje'])
        menuU.append_row(['2.- Listar personajes creados'])
        menuU.append_row(['3.- Modificar equipamiento'])
        menuU.append_row(['4.- Desconectar'])
        menuU.append_row(['5.- Salir'])
        menuU.columns.alignment = BeautifulTable.ALIGN_LEFT
        print(menuU)
        
    def menuUsuario1():
        menuU1 = BeautifulTable()
        menuU1.column_headers = ['===== MODIFICAR EQUIPAMIENTO =====']
        menuU1.append_row(['1.- Agregar equipamiento'])
        menuU1.append_row(['2.- Eliminar equipamiento'])
        menuU1.append_row(['3.- Salir'])

    def menuGameMaster():
        menuG = BeautifulTable()
        menuG.column_headers= ['===== MENU GAME MASTER =====']
        menuG.append_row(['1.- Listar jugadores'])
        menuG.append_row(['2.- Completar personajes'])
        menuG.append_row(['3.- Editar datos'])
        menuG.append_row(['4.- Desconectar'])
        menuG.append_row(['5.- Salir'])
        menuG.columns.alignment = BeautifulTable.ALIGN_LEFT 
        print(menuG)

    def menuGameMaster2():
        menuG2=BeautifulTable()
        menuG2.column_headers = ['===== EDITAR DATOS =====']
        menuG2.append_row(['1.- Editar poderes'])
        menuG2.append_row(['2.- Editar habilidades'])
        menuG2.append_row(['3.- Editar equipamiento'])
        menuG2.append_row(['4.- Editar raza'])
        menuG2.append_row(['5.- Editar estados'])
        menuG2.append_row(['6.- Subir nivel de un jugador'])
        menuG2.append_row(['7.- Volver'])
        menuG2.columns.alignment = BeautifulTable.ALIGN_LEFT
        print(menuG2)

    def menuGameMaster3():
        menuG3 = BeautifulTable()
        menuG3.column_headers = ['===== EDITAR EQUIPAMIENTO =====']
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
        menuG7.append_row(['1.- Editar raza'])
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
        cursor = conexion.conexion.cursor()
        intentos = 3

    
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            Proyecto.menu()
            opcion = input('Ingrese una opción: ')
            
            if opcion == '1':
                Proyecto.user()
                
            elif opcion == '2':
                usuario = input('Ingrese su nombre de usuario: ')
                clave = getpass.getpass('Ingrese su contraseña: ')
                clave_encriptada = conexion.encriptarPwd(clave)

                cursor.execute("SELECT usuario FROM usuario WHERE usuario = %s", (usuario,))     
                nombre=cursor.fetchone()
                cursor.execute("SELECT clave FROM usuario WHERE usuario = %s", (usuario,))
                pwd=cursor.fetchone()
                user = nombre[0]
                contra = pwd[0]
                
                if usuario == user and contra == clave_encriptada:
                    print('Credenciales correctas. ¡Bienvenido!')  
                    cursor.execute("UPDATE usuario SET enlinea = 1 WHERE usuario = %s;",(user,)) 
                    conexion.conexion.commit()
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')

                    while True:
                        Proyecto.menuPrincipal()
                        opcion_principal = input('Ingrese una opción: ')
                        
                        cursor.execute("SELECT tipo FROM usuario WHERE usuario = %s", (user,))
                        tipo = cursor.fetchone()
                        tipo = tipo[0]

                        if opcion_principal == '1' and tipo != 'master':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Bienvenido Jugador')
                            cursor.execute("UPDATE usuario SET tipo = %s WHERE usuario = %s",('jugador', user))
                            conexion.conexion.commit()
                            Proyecto.menuUsuario()
                            eleccion = input('Seleccione la acción a realizar: ')
                            system('cls')
                            if eleccion == '1':
                                print('Iniciaremos la creación de su personaje')
                                Personaje.crear_personaje()
                            elif eleccion == '2':
                                print('Estos son tus personajes creados')
                                Personaje.mostrar_personajes()
                            elif eleccion == '3':
                                print('Ingresaste a la edición del equipamiento')
                                system('cls')
                                Proyecto.menuUsuario1()
                                el = input('Ingrese una opción: ')
                                if el == '1':
                                    system('cls')
                                    Jugador.agregarEquipamiento()
                                elif el == '2':
                                    system('cls')
                                    Jugador.eliminarEquipamiento()
                                elif el == '3':
                                    print('Volviendo a la pantalla anterior')
                                    system('cls')
                                    return
                                else:
                                    print('Opción no válida')
                                    system('cls')
                                    
                            elif eleccion == '4':
                                print ('Desconectando usuario')
                                return 
                            
                            elif eleccion == '5':
                                print('Apagando sistema')
                                break
                                
                            else:
                                print ('Opción ingresada no es válida')

                        elif opcion_principal == '2'and tipo != 'jugador':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Bienvenido Game Master')
                            cursor.execute("UPDATE usuario SET tipo = %s WHERE usuario = %s",('master', user))
                            conexion.conexion.commit()
                            Proyecto.menuGameMaster()
                            elegir = input('Ingrese una opción: ')
                            
                            system('cls')
                            if elegir == '1':
                                GameMaster.listarJugadores()
                                system('cls')
                                
                            elif elegir == '2':
                                GameMaster.completarPersonajes()
                                system('cls')
                                
                            elif elegir == '3':
                                Proyecto.menuGameMaster2()
                                var = input('Ingrese su opción: ')
                                system('cls')
                                
                                if var == '1':
                                    Proyecto.menuGameMaster4()
                                    var1 = input('Indique que desea hacer en la tabla poderes: ')
                                    system('cls')
                                    if var1 == '1':
                                        GameMaster.agregarPoder()
                                    if var1 == '2':
                                        GameMaster.editarPoder() 
                                    if var1 == '3':
                                        GameMaster.eliminarPoder
                                    if var1 == '4': return
                                    else: print('Opción ingresada no válida')
                                    
                                elif var == '2':
                                    Proyecto.menuGameMaster5()
                                    var1 = input('Indique que desea hacer en la tabla habilidades: ')
                                    system('cls')
                                    if var1 == '1':
                                        GameMaster.agregarHabilidad()
                                    if var1 == '2':
                                        GameMaster.editarHabilidad() 
                                    if var1 == '3':
                                        GameMaster.eliminarHabilidad
                                    if var1 == '4': return
                                    else: print('Opción ingresada no válida')
                                    
                                elif var == '3':
                                    Proyecto.menuGameMaster3()
                                    var1 = input('Indique que desea hacer en la tabla equipamientos: ')
                                    system('cls')
                                    if var1 == '1':
                                        GameMaster.agregarEquipamiento()
                                    if var1 == '2':
                                        GameMaster.editarEquipamiento() 
                                    if var1 == '3':
                                        GameMaster.eliminarEquipamiento
                                    if var1 == '4': return
                                    else: print('Opción ingresada no válida')
                                    
                                elif var == '4':
                                    Proyecto.menuGameMaster6()
                                    var1 = input('Indique que desea hacer en la tabla raza: ')
                                    system('cls')
                                    if var1 == '1':
                                        GameMaster.agregarRaza()
                                    if var1 == '2': 
                                        GameMaster.editarRaza() 
                                    if var1 == '3':
                                        GameMaster.eliminarRaza()
                                    if var1 == '4': return
                                    else: print('Opción ingresada no válida')
                                    
                                elif var == '5':
                                    Proyecto.menuGameMaster7()
                                    var1 = input('Indique que desea hacer en la tabla estados: ')
                                    system('cls')
                                    if var1 == '1':
                                        GameMaster.agregarEstado()
                                    if var1 == '2':
                                        GameMaster.editarEstado() 
                                    if var1 == '3':
                                        GameMaster.eliminarEstado()
                                    if var1 == '4': return
                                    else: print('Opción ingresada no válida')
                                    
                                elif var == '6':
                                    GameMaster.subirNivel()
                                elif var == '7':
                                    return
                                
                            elif elegir == '4':
                                print('Desconectando usuario')
                                
                            elif elegir == '5':
                                print('Saliendo del sistema')
                                break
                            
                            else:
                                print('Opción no válida')

                        elif opcion_principal == '3':
                            confirmacion = input('¿Está seguro que desea salir? (si/no): ')
                            if confirmacion.lower() == 'si':
                                print('Saliendo del programa...')
                                break
                            elif confirmacion.lower() == 'no':
                                print('Cancelando salida.')
                            else:
                                print('Opción no válida.')
                                
                        elif opcion_principal == '1' and tipo == 'master':
                            print('Usuario ya definido como Game Master por lo que no puede ser Jugador \n Favor de ingresar otro usuario')
                            time.sleep(5)
                            system('cls')
                            
                        elif opcion_principal == '2' and tipo == 'jugador':
                            print('Usuario ya definido como Jugador por lo que no puede ser Game Master \n Favor de ingresar otro usuario')
                            time.sleep(5)
                            system('cls')
                            
                        else:
                            print('Opción no válida. Por favor, ingrese una opción válida.')
                            time.sleep(5)

                    break

                else:
                    intentos -= 1
                    print(f'Credenciales incorrectas. Intentos restantes: {intentos}')
                    if intentos <= 0:
                        print('Has agotado tus intentos. Saliendo del programa...')
                        break

            elif opcion == '3':
                print('Saliendo del programa...')
                break

            else:
                print('Opción no válida. Por favor, ingrese una opción válida.')
