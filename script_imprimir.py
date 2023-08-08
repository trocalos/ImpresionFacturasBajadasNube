import os
import shutil
import datetime
import csv
import win32api
import msvcrt
import time  # Añadir para usar el retraso

def imprimir_factura(ruta):
    try:
        win32api.ShellExecute(0, "print", ruta, None, ".", 0)
        return True
    except Exception as e:
        print(f"Error al imprimir el archivo {ruta}. Error: {e}")
        return False

def obtener_respuesta(archivo):
    print(f"Presiona 'S' si el fichero {archivo} se ha impreso correctamente o 'N' si no.")
    while True:
        if msvcrt.kbhit():
            tecla = msvcrt.getch().decode('utf-8').lower()
            if tecla in ['s', 'n']:
                return tecla

def factura_ya_impresa(nombre_factura, ruta_csv):
    with open(ruta_csv, mode='r', encoding='utf-8') as file:
        lector = csv.reader(file, delimiter=',', quotechar='"')
        for row in lector:
            if len(row) >= 3 and nombre_factura == row[2]:
                return True
        return False

def obtener_ultimo_numero(ruta_csv):
    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as file:
            lector = csv.reader(file, delimiter=',', quotechar='"')
            for row in lector:
                pass
            return int(row[0]) + 1
    except:
        return 1

ruta_sin_imprimir = "C:\\FacturasSinImprimir"
ruta_ya_impresas = "C:\\FacturasYaImpresas"
ruta_csv = "C:\\FacturasSinImprimir\\ListadoFacturasImpresas.csv"

# Verificar si el archivo CSV existe y, si no, crearlo con las cabeceras
if not os.path.exists(ruta_csv):
    with open(ruta_csv, mode='w', encoding='utf-8', newline='') as file:
        escritor = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow(['Número', 'Fecha', 'Nombre de Archivo'])

for archivo in os.listdir(ruta_sin_imprimir):
    if archivo.endswith(".pdf"):
        if not factura_ya_impresa(archivo, ruta_csv):
            archivo_ruta_completa = os.path.join(ruta_sin_imprimir, archivo)
            print(f"Enviando a la impresora el archivo {archivo}...")  # Informar al usuario
            if imprimir_factura(archivo_ruta_completa):
                respuesta = obtener_respuesta(archivo)
                if respuesta == 's':
                    print("Espera 5 segundos a que cualquier proceso que esté utilizando el archivo lo libere...")  # Informar al usuario
                    time.sleep(5)  # Espera 5 segundos
                    with open(ruta_csv, mode='a', encoding='utf-8', newline='') as file:
                        escritor = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        fecha_actual = datetime.datetime.now().strftime("%d-%m-%y")
                        numero = obtener_ultimo_numero(ruta_csv)
                        escritor.writerow([str(numero), fecha_actual, archivo])
                    shutil.move(archivo_ruta_completa, os.path.join(ruta_ya_impresas, archivo))
                elif respuesta == 'n':
                    print(f"El archivo {archivo} no se ha impreso correctamente.")
        else:
            print(f"El archivo {archivo} ya ha sido impreso anteriormente.")
