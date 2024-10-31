import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# Función para crear gráficos
def crear_graficos(df, anio):
    # Gráfico de barras sobre lluvias anuales
    suma_anual = df.sum()
    plt.figure(figsize=(10, 6))
    suma_anual.plot(kind='bar')
    plt.title(f'Lluvias Anuales en el año {anio}.')
    plt.xlabel('Mes')
    plt.ylabel('Lluvia (mm)')
    plt.xticks(rotation=45)
    plt.show()


    # Grafico de dispersión mm de lluvia, eje x meses, eje y días.
    for mes in range(12):
        plt.scatter([df.columns[mes]] * len(df.index), df.index + 1, label=f'Mes {mes + 1}', alpha=0.5, s=df.iloc[:, mes] * 2),  # Multiplicamos por 2 para que los mm pequeños se visualicen.

    # Configurar el gráfico de dispersión
    plt.ylabel('Día (1-31)')
    plt.xlabel('Mes')
    plt.xticks(rotation=45, ha='right')
    plt.title(f'Gráfico de Dispersión de Lluvias para el año {anio}.')
    # Configurar la leyenda fuera del gráfico
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Ajusto la posición.
    plt.tight_layout()  # Ajusta el layout para evitar que se corten los elementos

    plt.show()

    # Gráfico circular
    plt.figure(figsize=(8, 8))
    plt.pie(suma_anual, labels=suma_anual.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Distribución de Lluvias por Mes para el año {anio}')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def crear_grafico_circular_mes(df, mes_elegido):
    """
    Gráfico circular que abarca todos los días del mes elegido.
    """
    # Datos del mes elegido
    data = df[mes_elegido].dropna().values  # Eliminar NaN
    dias = df[mes_elegido].dropna().index + 1  # Los índices son los días del mes

    if len(data) == 0:
        print(f"No hay datos válidos para el mes de {mes_elegido}.")
        return

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

    def func(pct, allvals):
        absolute = int(np.round(pct / 100. * np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute:d} mm)"

    # Crear gráfico circular
    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                       textprops=dict(color="w"))

    # Crear etiquetas para la leyenda
    porcentajes_y_mm = [f'Día {dias[i]}: {val:.1f} mm\n({val / np.sum(data) * 100:.1f}%)'
                        for i, val in enumerate(data)]

    # Añadir la leyenda
    ax.legend(wedges, porcentajes_y_mm, title="Días del Mes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")
    plt.title(f'Distribución de Lluvias por día durante el mes de {mes_elegido} del año {anio}.')
    plt.axis('equal')  # Para que el gráfico sea circular

    plt.show()


# Función para crear registros pluviales aleatorios
def crear_registros_pluviales(anio):
    meses = []
    for mes in range(12):
        dias = 31 if mes in [0, 2, 4, 6, 7, 9, 11] else 30 if mes != 1 else random.choice([28, 29])
        mes_datos = [round(np.random.rand() * 101, 2) for _ in range(dias)] # Multiplico por 101 para cambiar el rango de [0,1) a [0,101)
        meses.append(mes_datos)

    columnas = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre','Diciembre']
    df = pd.DataFrame(meses).T
    df.columns = columnas
    df.rename(index=lambda x: x + 1, inplace=True)
    return df

# Crear archivos CSV para los años 2000 a 2019 para tener registros precargados.
for anio in range(2000, 2020):
    nombre_archivo = f"registroPluvial{anio}.csv"
    if not os.path.exists(nombre_archivo):  # Solo crea si no existe
        df = crear_registros_pluviales(anio)
        df.to_csv(nombre_archivo, index=False)
        print(f"Archivo creado: {nombre_archivo}")

# Generar lista de archivos disponibles para saber disponibilidad.
archivos_disponibles = [f"registroPluvial{anio}.csv" for anio in range(2000, 2020) if os.path.exists(f"registroPluvial{anio}.csv")]

print("\nArchivos disponibles:")
for archivo in archivos_disponibles:
    print(archivo)

print('*' * 50, '\n Menú')
print('*' * 50)

# Inicializo la variable anio para poder declararla global dentro de las 2 funciones y siguientes y no tener que pasarla como parámetro.
anio = None

# Función para procesar años.
def procesar_anio():
    while True:
        try:
            # La declaro global para poder usarla en porcesar_mes
            global anio
            # Solicito el año
            anio = int(input("Ingrese el año para cargar los registros pluviales (número entero): "))
            nombre_archivo = f"registroPluvial{anio}.csv"
            global df
            if os.path.exists(nombre_archivo):
                # Leer el archivo CSV
                df = pd.read_csv(nombre_archivo)
                # Aplanar el DataFrame
                df_s = df.stack()
                print(f"Registros pluviales del año {anio}.\n")
                print(f"La precipitación máxima del año {anio} fue de: {df_s.max()}mm, la mínima fue de: {df_s.min()}mm y la media para el año {anio} fue de {round(df_s.mean(),2)}mm.\n")
                crear_graficos(df, anio)
                break
            elif not os.path.exists(nombre_archivo):
                # Si no existe, generar datos aleatorios
                print(f"No se encontraron registros para el año {anio}. Generando datos aleatorios...\n")
                df = crear_registros_pluviales(anio)
                df.to_csv(nombre_archivo, index=False)
                # Aplanar el DataFrame
                df_s = df.stack()
                print(f"Datos aleatorios generados y guardados en {nombre_archivo}:\n")
                print(f"Registros pluviales del año {anio}.\n")
                print(f"La precipitación máxima del año {anio} fue de: {df_s.max()}mm, la mínima fue de: {df_s.min()}mm y la media para el año {anio} fue de {round(df_s.mean(),2)}mm.\n")
                crear_graficos(df, anio)
                break
        except  ValueError:
            print("Año inválido. Por favor, ingrese un formato válido.")
  
def procesar_mes():
    # Ver si al usuario le interesa analizar un mes particular.
    global df
    global anio
    print(f"¿Le interesaria analizar un mes en paraticular para el año {anio}?\n")
    while True:
        mes_elegido = input("Ingrese el nombre del mes (o 'NO' para salir): ").strip().lower().capitalize()

        # Validar entrada
        if mes_elegido in  ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre','Diciembre']:
            print(f"Registros pluviales para el mes {mes_elegido}:")
            print(df.loc[:, mes_elegido])  # Mostrar los registros del mes elegido.
            print(f"La precipitación máxima del mes de {mes_elegido} fue de {df.loc[:, mes_elegido].max()}mm.\n")
            print(f"La precipitación mínima del mes de {mes_elegido} fue de {df.loc[:, mes_elegido].min()}mm.\n")
            print(f"La precipitación media del mes de {mes_elegido} fue de {round(df.loc[:, mes_elegido].mean(),2)}mm.\n")
            crear_grafico_circular_mes(df, mes_elegido)
            return  # Salir del bucle después de procesar un mes válido
        elif mes_elegido == "No":
            print("Gracias por su consulta, vuelva cuando quiera.")
            return  # Salir del bucle después de procesar un mes válido.
        else:
            print("Mes inválido. Por favor, ingrese un mes válido o 'NO'.")

if __name__ == "__main__":
    # Código de prueba o ejemplos de uso
    procesar_anio()
    procesar_mes()