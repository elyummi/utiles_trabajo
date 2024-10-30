#OCR

import os
import csv

image_path = r"C:\Users\daniel.villoslada\PycharmProjects\OCR\imagenes_prueba\01_IMG_20240604_135457.jpg"
# folder_path = r"C:\Users\daniel.villoslada\PycharmProjects\OCR\imagenes_prueba"
# folder_path = r"C:\Users\daniel.villoslada\ApplusGlobal\Enertis Teams SSTT (Chile) - Documentos\OPERACIONES\CAMPO\2024\8-SOCL.3001701.01-COBRA-TERMO DRONE-BELMONTE II\1 GENERADA\02 Termografia a pie - defectos\SN fotos"
# folder_path = r"C:\Users\daniel.villoslada\ApplusGlobal\Enertis Teams SSTT (Chile) - Documentos\OPERACIONES\CAMPO\2024\41. SOCL.4286101.01-RE-ENERGISA - ROTURAS VIDRIO - MATUPA\1 GENERADA\1 VISUAL\Mapeamiento - Todas - MT - Afonso"
folder_path = r"C:\Users\daniel.villoslada\ApplusGlobal\Enertis Teams SSTT (Chile) - Documentos\OPERACIONES\CAMPO\2024\41. SOCL.4286101.01-RE-ENERGISA - ROTURAS VIDRIO - MATUPA\1 GENERADA\1 VISUAL\01-Fotos mapeamiento dani"

i = 0
lista_resultados = []

# for root, dir, file in os.walk(folder_path):
#     print(root)
#     print(dir)
#     print(file)
output = r"salida_crear_elementos.csv"
with open(output, "w", newline='', encoding='utf-8') as output_file:
    for root, dir, file_list in os.walk(folder_path):
        print("Iteracion: ", i)
        for file in file_list:
            lista_salida = []
            path_archivo = os.path.join(root, str(file))
            usina = root.split("\\")[-3]
            ufv = root.split("\\")[-2]
            eixo = root.split("\\")[-1]
            imagen = file
            print(usina,",", ufv,",", eixo,",", imagen)
            lista_salida.extend([usina, ufv, eixo, imagen])
            print(lista_salida)

        # print(root, dir, "Total archivos: ", len(file_list))

            wr = csv.writer(output_file, delimiter=',')
            wr.writerow(lista_salida)
        i += 1
