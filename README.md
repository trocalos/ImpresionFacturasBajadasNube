# ImpresionFacturasBajadasNube
Programa para imprimir las facturas que me bajo de mi correo electrónico en formato pdf

EXPLICACIÓN SENCILLA DEL PROGRAMA DE IMPRESIÓN DE FACTURAS

Este programa se encarga de gestionar la impresión de facturas almacenadas en un directorio específico de tu computadora. La idea principal es que, al ejecutar el programa, este revisará todas las facturas pendientes de imprimir y las enviará automáticamente a la impresora.

Después de cada impresión, el programa te pedirá que confirmes si la factura se imprimió correctamente. Si confirmas que sí, el programa registrará esta factura en un archivo llamado CSV y moverá el archivo de factura a otro directorio, indicando que ya ha sido impresa.

El programa también lleva un registro de todas las facturas que ha impreso anteriormente, para evitar imprimir duplicados. Si intentas imprimir una factura que ya ha sido procesada en el pasado, el programa te informará y no realizará ninguna acción.

En resumen, este programa automatiza el proceso de imprimir facturas, asegurándose de que cada una se imprima una sola vez y llevando un registro ordenado de todas las impresiones realizadas.

ESQUEMA DEL PROGRAMA DE IMPRESIÓN DE FACTURAS

1. **Importaciones**:
   - Se importan los módulos necesarios para la ejecución del programa.

2. **Definición de Funciones**:
   - `imprimir_factura(ruta)`: Intenta imprimir un archivo PDF. Devuelve `True` si tiene éxito o `False` en caso contrario.
   - `obtener_respuesta(archivo)`: Solicita al usuario confirmación sobre si un archivo se imprimió correctamente.
   - `factura_ya_impresa(nombre_factura, ruta_csv)`: Verifica si una factura ya ha sido impresa consultando el archivo CSV.
   - `obtener_ultimo_numero(ruta_csv)`: Obtiene el último número registrado en el CSV para mantener una numeración incremental.

3. **Variables de Ruta**:
   - Se definen las rutas de los directorios de facturas pendientes de imprimir, facturas ya impresas y el archivo CSV de registro.

4. **Verificación de CSV**:
   - Si el archivo CSV no existe, se crea y se añaden las cabeceras correspondientes.

5. **Proceso Principal**:
   a. Se recorren todos los archivos en el directorio de facturas pendientes de imprimir.
   b. Por cada archivo con extensión ".pdf":
      i. Se verifica si ya ha sido impreso consultando el archivo CSV.
      ii. Si no ha sido impreso:
         1. Se informa que se está enviando a la impresora.
         2. Se intenta imprimir.
         3. Se solicita confirmación al usuario sobre la impresión correcta.
         4. Si el usuario confirma:
            - Se informa al usuario sobre la espera de 5 segundos.
            - Se espera 5 segundos para liberar el archivo.
            - Se añade un registro en el CSV con el número, fecha y nombre del archivo.
            - Se mueve el archivo al directorio de facturas ya impresas.
      iii. Si ya ha sido impreso:
         - Se informa al usuario que el archivo ya ha sido impreso anteriormente.
