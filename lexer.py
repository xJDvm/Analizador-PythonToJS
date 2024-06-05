# Importa la librería os, que permite interactuar con el sistema operativo
import os

# Función que recorre recursivamente todos los archivos y directorios en una ruta dada
def recorrer_directorios(ruta):
    # Recorre la lista de nombres en la ruta dada
    for nombre in os.listdir(ruta):
        # Crea una ruta completa combinando la ruta base y el nombre del archivo/directorio
        ruta_completa = os.path.join(ruta, nombre)
        
        # Verifica si la ruta completa es un directorio
        if os.path.isdir(ruta_completa):
            # Si es un directorio, imprime el nombre del directorio
            print(f"Directorio: {ruta_completa}")
            # Llama a la función recursivamente para recorrer el subdirectorio
            recorrer_directorios(ruta_completa)
        else:
            # Si es un archivo, imprime el nombre del archivo
            print(f"Archivo: {ruta_completa}")

# Especifica la ruta inicial desde donde se comenzará a recorrer
ruta_inicial = "/ruta/a/tu/directorio"

# Llama a la función para comenzar a recorrer desde la ruta inicial
recorrer_directorios(ruta_inicial)