#OCR

import cv2
import easyocr
import os
import csv

image_path = r"C:\Users\daniel.villoslada\PycharmProjects\OCR\imagenes_prueba\01_IMG_20240604_135457.jpg"
# folder_path = r"C:\Users\daniel.villoslada\PycharmProjects\OCR\imagenes_prueba"
#folder_path = r"C:\Users\daniel.villoslada\ApplusGlobal\Enertis Teams SSTT (Chile) - Documentos\OPERACIONES\CAMPO\2024\8-SOCL.3001701.01-COBRA-TERMO DRONE-BELMONTE II\1 GENERADA\02 Termografia a pie - defectos\SN fotos"
folder_path = r"C:\Users\daniel.villoslada\ApplusGlobal\Enertis Teams SSTT (Chile) - Documentos\OPERACIONES\CAMPO\2024\41. SOCL.4286101.01-RE-ENERGISA - ROTURAS VIDRIO - MATUPA\1 GENERADA\1 VISUAL\Mapeamiento - Todas - MT - Afonso"

i = 0
lista_resultados = []

# for root, dir, file in os.walk(folder_path):
#     print(root)
#     print(dir)
#     print(file)

for root, dir, file_list in os.walk(folder_path):
    print("Iteracion: ", i)
    for file in file_list:
        print("Leyendo archivo")
        path_archivo = os.path.join(root, str(file))
        # path_archivo = image_path
        print(path_archivo)
        reader = easyocr.Reader(["es"], gpu=True)
        image = cv2.imread(path_archivo)

        try:
            result = reader.readtext(image, paragraph=False)
        except:
            result = [["Error, no es imagen", "Error, no es imagen"]]
        print("Archivo: ", file, "Resultado: ", result)
        lista_resultados.append(file)
        lista_resultados.append(result[0][1])
        print(lista_resultados)
    i += 1

with open("resultados.txt", 'w', newline='') as csv_salida:
    wr = csv.writer(csv_salida, delimiter='\n')
    wr.writerow(lista_resultados)