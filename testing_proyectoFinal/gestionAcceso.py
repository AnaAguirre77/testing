import pickle
import os
from datetime import datetime
from acceso import Acceso
class gestionAcceso:
    def __init__(self, gestion_usuario):
        self.gestion_usuario = gestion_usuario 
        self.crear_archivo_accesos()
        self.accesos = self.cargar_accesos()
    def crear_archivo_accesos(self):
        if not os.path.isfile('accesos.ispc'):
            with open('accesos.ispc', 'wb') as file:
                pickle.dump([], file)
    def cargar_accesos(self):
        try:
            with open('accesos.ispc', 'rb') as file:
                data = pickle.load(file)
                return data if data is not None else []
        except FileNotFoundError:
            print("Archivo no encontrado, creando uno nuevo.")
            self.crear_archivo_accesos()
            return []
        except (pickle.UnpicklingError, EOFError) as e:
            print(f"Error al cargar datos de accesos: {e}")
            return []
    def guardar_accesos(self):
        with open('accesos.ispc', 'wb') as file:
            pickle.dump(self.accesos, file)
    def registrar_acceso(self, usuario, success, password=None):
        fecha_ingreso = datetime.now()
        acceso = Acceso(len(self.accesos) + 1, fecha_ingreso, None, usuario.get_username())
        self.accesos.append(acceso)
        self.guardar_accesos()
        if success:
            print(f"Acceso registrado para {usuario.get_username()}.")
        else:
            with open('logs.txt', 'a') as log_file:
                log_file.write(f"Intento fallido: {usuario.get_username()} - {datetime.now()} - Clave: {password}\n")
    def mostrar_accesos(self):
        if not self.accesos:
            print("No hay accesos registrados.")
            return
        
        print("\n--- Lista de Accesos ---")
        for acceso in self.accesos:
            print(f"ID: {acceso.get_id()}, Usuario: {acceso.get_usuarioLogueado()}, Fecha Ingreso: {acceso.get_fechaIngreso()}, Fecha Salida: {acceso.get_fechaSalida()}")
    def mostrar_logs_intentos_fallidos(self):
        try:
            with open('logs.txt', 'r') as log_file:
                logs = log_file.readlines()
                if not logs:
                    print("No hay intentos fallidos registrados.")
                    return
                
                print("\n--- Intentos Fallidos ---")
                for log in logs:
                    print(log.strip())
        except FileNotFoundError:
            print("No se encontró el archivo de logs.")
    def ingresar_usuario(self, username, password):
        for user in self.gestion_usuario.usuarios:  # Accede a la lista de usuarios
          if user.get_username() == username:  
            if user.get_password() == password: 
                self.registrar_acceso(user, success=True)
                print(f"Bienvenido {username}, has ingresado a la aplicación.")
                return True  
            else:
                self.registrar_acceso(user, success=False, password=password)
                print("Contraseña incorrecta.")
                return False  