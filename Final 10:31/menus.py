from GestionUsuario import GestionUsuario
from GestionAcceso import GestionAcceso

def menu_gestion_usuarios_accesos(gestion_usuario, gestion_acceso):
    while True:
        print("\n--- Gestión de Usuarios y Accesos ---")
        print("1. CRUD de Usuarios")
        print("2. Mostrar los Accesos (datos de accesos.ispc)")
        print("3. Mostrar los logs de intentos fallidos (datos de logs.txt)")
        print("4. Volver al Menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            menu_crud_usuarios(gestion_usuario)
        elif opcion == '2':
            gestion_acceso.mostrar_accesos()
        elif opcion == '3':
            gestion_acceso.mostrar_logs_intentos_fallidos()
        elif opcion == '4':
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

def menu_crud_usuarios(gestion_usuario):
    while True:
        print("\n--- CRUD de Usuarios ---")
        print("1. Agregar un nuevo usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario")
        print("4. Volver al menú anterior")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            username = input("Username: ")
            dni = input("DNI (solo números): ")
            password = input("Password: ")
            email = input("Email: ")
            gestion_usuario.agregar_usuario(username, dni, password, email)
        elif opcion == '2':
            id = int(input("ID del usuario a modificar: "))
            username = input("Nuevo Username (dejar en blanco para no cambiar): ")
            dni = input("Nuevo DNI (dejar en blanco para no cambiar): ")
            password = input("Nuevo Password (dejar en blanco para no cambiar): ")
            email = input("Nuevo Email (dejar en blanco para no cambiar): ")
            gestion_usuario.modificar_usuario(id, username or None, dni or None, password or None, email or None)
        elif opcion == '3':
            identifier = input("Username o Email del usuario a eliminar: ")
            gestion_usuario.eliminar_usuario(identifier)
        elif opcion == '4':
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

def submenu_mostrar_datos_acceso(gestion_acceso):
    while True:
        print("\n--- Menú datos de acceso ---")
        print("1. Mostrar los Accesos.")
        print("2. Mostrar los logs de intentos fallidos.")
        print("3. Volver al Menú anterior.")
        print("4. Volver al Menú principal.")
        print("5. Salir del sistema.")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestion_acceso.mostrar_accesos()
        elif opcion == '2':
            gestion_acceso.mostrar_logs_intentos_fallidos()
        elif opcion == '3':
            return  # volver al menú anterior
        elif opcion == '4':
            return  # volver al menú principal
        elif opcion == '5':
            exit()
        else:
            print("Opción inválida. Intente de nuevo.")

def menu_ingreso(gestion_usuario, gestion_acceso):
    while True:
        print("\n--- Ingreso al Sistema ---")
        username = input("Ingrese su username: ")
        password = input("Ingrese su password: ")
        
        if gestion_acceso.ingresar_usuario(username, password):
            break  # Salir si el ingreso fue exitoso
        else:
            continuar = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()
            if continuar != 's':
                break
