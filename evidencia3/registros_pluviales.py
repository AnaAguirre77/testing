import os
import random
import pandas as pd
import matplotlib.pyplot as plt

# Función para crear gráficos
def crear_graficos(df, anio):
    # Calcular la suma mensual asegurando que los días nulos (meses más cortos) no se incluyan.
    suma_anual = df.sum()  # Esto funciona porque suma columna por columna (es decir, por mes).
    
    # Gráfico de lluvias anuales
    plt.figure(figsize=(10, 6))
    suma_anual.plot(kind='bar')
    plt.title(f'Lluvias Anuales en {anio}')
    plt.xlabel('Mes')
    plt.ylabel('Lluvia (mm)')
    plt.xticks(rotation=0)
    plt.show()

    # Grafico de dispersión
    for mes in range(12):
        plt.scatter(df.index + 1, df.iloc[:, mes], label=f'Mes {mes + 1}')

    # Configurar el gráfico de dispersión
    plt.xlabel('Día (índice + 1)')
    plt.ylabel('Valores')
    plt.title('Gráfico de Dispersión')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Ajusto la posición.
    plt.tight_layout()  # Evitar que se corten los elementos

    plt.show()

    # Gráfico circular
    plt.figure(figsize=(8, 8))
    plt.pie(suma_anual, labels=suma_anual.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Lluvias por Mes')
    plt.axis('equal')
    plt.show()

# Función para crear registros pluviales aleatorios
def crear_registros_pluviales(anio):
    meses = []
    for mes in range(12):
        dias = 31 if mes in [0, 2, 4, 6, 7, 9, 11] else 30 if mes != 1 else random.choice([28, 29])
        mes_datos = [random.randint(0, 100) for _ in range(dias)]
        meses.append(mes_datos)

    df = pd.DataFrame(meses).T
    df.columns = [f'Mes {i + 1}' for i in range(12)]
    return df

# Crear archivos CSV para los años 2000 a 2019 para tener registros previos.
for anio in range(2000, 2020):
    nombre_archivo = f"registroPluvial{anio}.csv"
    if not os.path.exists(nombre_archivo):  # Solo crea si no existe
        df = crear_registros_pluviales(anio)
        df.to_csv(nombre_archivo, index=False)
        print(f"Archivo creado: {nombre_archivo}")

# Generar lista de archivos disponibles
archivos_disponibles = [f"registroPluvial{anio}.csv" for anio in range(2000, 2020) if os.path.exists(f"registroPluvial{anio}.csv")]

print("\nArchivos disponibles:")
for archivo in archivos_disponibles:
    print(archivo)

print('*' * 50, '\n Menú')
print('*' * 50)

# Solicito el año
anio = input("Ingrese el año para cargar los registros pluviales: ")
nombre_archivo = f"registroPluvial{anio}.csv"

if os.path.exists(nombre_archivo):
    # Leer el archivo CSV
    df = pd.read_csv(nombre_archivo)
    print(f"Registros pluviales del año {anio}:")
else:
    # Si no existe, generar datos aleatorios
    print(f"No se encontraron registros para el año {anio}. Generando datos aleatorios...")
    df = crear_registros_pluviales(anio)
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos aleatorios generados y guardados en {nombre_archivo}:")

# Solicitar mes y validar entrada
mes_elegido = int(input("Seleccione un mes (1-12): ")) - 1  # Ajusto para índice que empieza en 0
if 0 <= mes_elegido < 12:
    print(f"Registros pluviales para el mes {mes_elegido + 1}:")
    print(df.iloc[:, mes_elegido])  # Mostrar los registros del mes elegido

    # Llamar a la función de gráficos solo si el mes es válido
    crear_graficos(df, anio)
else:
    print("Mes inválido.")
