import pickle
from usuario import Usuario

class gestionUsuario:
    def __init__(self):
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        try:
            with open('usuarios.ispc', 'rb') as file:
                usuarios = pickle.load(file)
                if isinstance(usuarios, list):  # Cambiado a lista
                    return usuarios
                else:
                    return []
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Error al cargar datos de usuarios: {e}, creando una nueva lista.")
            return []

    def agregar_usuario(self, username, DNI, password, email):
        if username in (user.get_username() for user in self.usuarios) or \
           email in (user.get_email() for user in self.usuarios):
            print("El usuario o el email ya existen.")
            return False

        try:
            DNI = int(DNI)
        except ValueError:
            print("El DNI debe ser un número.")
            return False

        nuevo_usuario = Usuario(len(self.usuarios) + 1, username, DNI, password, email)
        self.usuarios.append(nuevo_usuario)
        
        # Ordenar la lista por DNI
        self.usuarios.sort(key=lambda user: user.get_DNI())
        
        self.guardar_usuarios()
        print("Usuario agregado exitosamente.")
        return True
    
    def guardar_usuarios(self):
        with open('usuarios.ispc', 'wb') as file:
            pickle.dump(self.usuarios, file)

    def modificar_usuario(self, id, username=None, DNI=None, password=None, email=None):
        for usuario in self.usuarios:
            if usuario.get_id() == id:
                if username:
                    usuario.set_username(username)
                if DNI is not None:
                    try:
                        DNI = int(DNI)
                        usuario.set_DNI(DNI)
                    except ValueError:
                        print("El DNI debe ser un número.")
                        return False
                if password:
                    usuario.set_password(password)
                if email:
                    usuario.set_email(email)
                self.guardar_usuarios()
                print("Usuario modificado exitosamente.")
                return True
        print("Usuario no encontrado.")
        return False

    def eliminar_usuario(self, identifier):
        for user in self.usuarios:
            if user.get_username() == identifier or user.get_email() == identifier:
                self.usuarios.remove(user)  # Remover el objeto de la lista
                self.guardar_usuarios()
                print("Usuario eliminado exitosamente.")
                return True
        print("Usuario no encontrado.")
        return False

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        print("\n--- Lista de Usuarios ---")
        for user in self.usuarios:
            print(f"ID: {user.get_id()}, Username: {user.get_username()}, DNI: {user.get_DNI()}, Email: {user.get_email()}")
