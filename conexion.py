import mysql.connector
from mysql.connector import Error
import hashlib
import getpass

class Conexion:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='juegorol'
            )
            if self.conexion.is_connected():
                print('Conexión exitosa a la base de datos')
                
        except Error as ex:
            print('Error al conectar con la base de datos: {0}'.format(ex))
           

    def encriptarPwd(self, pwd) -> str:
        hashObject = hashlib.md5(pwd.encode('utf-8'))
        pwd = hashObject.hexdigest()
        return pwd

    def crearUsuario(self):
        print('Para empezar crearemos un usuario')
        usuario = input('Ingrese un nombre de usuario: ')
        clave = getpass.getpass('Ingrese una contraseña: ')
        clave = self.encriptarPwd(clave)
        estado = 'desconectado'

        try:
            cursor = self.conexion.cursor()
            cursor.execute("INSERT INTO usuario (usuario, clave, estado) VALUES (%s, %s, %s)", (usuario, clave, estado))
            self.conexion.commit()
            print('Usuario creado exitosamente')
        except Error as ex:
            print('Error al crear el usuario: {0}'.format(ex))
        finally:
            cursor.close()





