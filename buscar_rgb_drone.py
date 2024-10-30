"""Programa para buscar la gemelas de las ir/rgb de termografia com drone."""

import os
import shutil
import csv

# Variables
# Tipo de archico que queremos buscar (ir, rgb)
tipo_archivo = "rgb"
# Path del archivo csv con los nombres de los archivos que queremos buscar
# Lo podemos poner con una ventana
path_csv_archivos_buscar = r"C:\Users\daniel.villoslada\PycharmProjects\buscar_rgb_drone\pruebas\lista.txt"
# Lista donde van los nombres de los archivos que queremos
lista_archivos_buscar = []

# Lista para salida de resultados
# Temporal hasta que implementemos el copiar
lista_archivos_encontrados = []
# Aqui anotamos si hay algun archivo que no se ha encontrado
lista_archivos_no_encontrados = []

# Carpetas
# Lista con las carpetas donde queremos buscar los archivos, puedes ser varias
lista_carpetas_buscar = [r"02-04-2024", r"03-04-2024", r"04-04-2024", r"04-06-2024", r"05-04-2024",
                         r"05-06-2024",
                         r"06-04-2024", r"06-06-2024", r"07-06-2024", r"08-04-2024", r"09-04-2024", r"10-04-2024",
                         r"10-06-2024",
                         r"11-04-2024", r"11-06-2024", r"12-04-2024", r"12-06-2024", r"14-06-2024", r"15-04-2024",
                         r"16-04-2024",
                         r"17-04-2024", r"17-06-2024", r"18-04-2024", r"18-06-2024", r"19-06-2024", r"21-05-2024",
                         r"22-05-2024",
                         r"23-05-2024", r"24-05-2024", r"27-05-2024", r"28-05-2024"]

string_completar_path_carpeta_buscar = (r"C:\Users\daniel.villoslada\ApplusGlobal\Enertis Teams SSTT (Chile) - "
                                        r"Documentos\OPERACIONES\CAMPO\2024\8-SOCL.3001701.01-COBRA-TERMO "
                                        r"DRONE-BELMONTE II\1 GENERADA\02 Termografia a pie - defectos\Imagens IR")

# Carpeta donde se van a incluir los archivos encontrados
carpeta_salida = (r"C:\Users\daniel.villoslada\ApplusGlobal\Enertis Teams SSTT (Chile) - "
                  r"Documentos\OPERACIONES\CAMPO\2024\8-SOCL.3001701.01-COBRA-TERMO DRONE-BELMONTE II\1 GENERADA\02 "
                  r"Termografia a pie - defectos\Imagen IR seleccionada")

# Principal

##Version para imagenes de drone DJI
modo_dji = "n"
if modo_dji == "s":
    # Leemos el csv y sacamos los nombres de los archivos que queremos
    with open(path_csv_archivos_buscar, "r") as csv_archivos_buscar:
        for archivo in csv_archivos_buscar.readlines():
            lista_archivos_buscar.append(archivo.rstrip().replace("ir", str(tipo_archivo)))
        # print(lista_archivos_buscar)

    # Buscamos los archivos
    for archivo in lista_archivos_buscar:
        print("Archivo buscado: ", str(archivo))
        encontrado = 0
        for carpeta_busqueda in lista_carpetas_buscar:
            # print("Carpeta de busqueda: ", carpeta_busqueda)
            for root, dir, files in os.walk(carpeta_busqueda):
                # print(root, dir)
                if str(archivo) in files:
                    path_archivo_original = os.path.join(root, str(archivo))
                    path_archivo_copiado = str(carpeta_salida) + "\\" + str(archivo)
                    lista_archivos_encontrados.append(str(archivo))
                    shutil.copyfile(path_archivo_original, path_archivo_copiado)
                    encontrado = 1
                    break
        if encontrado == 0:
            if (str(archivo) not in lista_archivos_no_encontrados and
                    str(archivo) not in lista_archivos_encontrados):
                lista_archivos_no_encontrados.append(str(archivo))
            print("Archivo no encontrado: ", str(archivo))

    # Actualizamos la lista, para cuando hacemos la busqueda en varias carpetas
    for archivo in lista_archivos_no_encontrados:
        if str(archivo) in lista_archivos_encontrados:
            lista_archivos_no_encontrados.remove(str(archivo))
    # print(lista_archivos_encontrados)
    # print(lista_archivos_no_encontrados)

    with open("no_econtrados.txt", 'w', newline='') as csv_lista_no_encontrados:
        wr = csv.writer(csv_lista_no_encontrados, delimiter='\n')
        wr.writerow(lista_archivos_no_encontrados)

    print("Programa terminado")

##Version para imagenes de Fluke
modo_general = "s"
if modo_general == "s":
    # Leemos el csv y sacamos los nombres de los archivos que queremos
    with open(path_csv_archivos_buscar, "r") as csv_archivos_buscar:
        for archivo in csv_archivos_buscar.readlines():
            lista_archivos_buscar.append(archivo.strip("\n"))
        print(lista_archivos_buscar)

    # Buscamos los archivos
    for archivo in lista_archivos_buscar:
        # print(lista_archivos_buscar)
        print("Archivo buscado: ", str(archivo))
        encontrado = 0
        for carpeta_busqueda in lista_carpetas_buscar:
            carpeta_busqueda = string_completar_path_carpeta_buscar + "\\" + carpeta_busqueda
            # print("Carpeta de busqueda: ", carpeta_busqueda)
            for root, dir, files in os.walk(carpeta_busqueda):
                # print("Buscando aqui", root, dir)
                # print("Files", files)

                if str(archivo) in files:
                    path_archivo_original = os.path.join(root, str(archivo))
                    # print("path_archivo_original", path_archivo_original)
                    path_archivo_copiado = str(carpeta_salida) + "\\" + str(archivo)
                    print("path_archivo_copiado", path_archivo_copiado)
                    lista_archivos_encontrados.append(str(archivo))
                    shutil.copyfile(path_archivo_original, path_archivo_copiado)
                    encontrado = 1
                    break
        if encontrado == 0:
            if (str(archivo) not in lista_archivos_no_encontrados and
                    str(archivo) not in lista_archivos_encontrados):
                lista_archivos_no_encontrados.append(str(archivo))
            print("Archivo no encontrado: ", str(archivo))

    # Actualizamos la lista, para cuando hacemos la busqueda en varias carpetas
    for archivo in lista_archivos_no_encontrados:
        if str(archivo) in lista_archivos_encontrados:
            lista_archivos_no_encontrados.remove(str(archivo))
    # print(lista_archivos_encontrados)
    # print(lista_archivos_no_encontrados)

    with open("no_econtrados.txt", 'w', newline='') as csv_lista_no_encontrados:
        wr = csv.writer(csv_lista_no_encontrados, delimiter='\n')
        wr.writerow(lista_archivos_no_encontrados)

    print("Programa terminado")
