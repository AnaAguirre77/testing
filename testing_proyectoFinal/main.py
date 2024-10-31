import sys
from gestionUsuario import gestionUsuario
from gestionAcceso import gestionAcceso
from menus import menu_gestion_usuarios_accesos
from menus import menu_ingreso
from data_analisys import procesar_mes, procesar_anio

def main():
    gestion_usuario = gestionUsuario()
    gestion_acceso = gestionAcceso(gestion_usuario)
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Usuarios y Accesos de la Aplicación.")
        print("2. Ingresar al sistema.")
        print("3. Análisis de datos de registros pluviales.")
        print("4. Salir del sistema.")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            menu_gestion_usuarios_accesos(gestion_usuario, gestion_acceso)
        elif opcion == '2':
            menu_ingreso(gestion_usuario, gestion_acceso)
        elif opcion == '3':
            procesar_anio()
            procesar_mes()
        elif opcion == '4':
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
