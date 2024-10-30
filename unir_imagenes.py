import cv2  # OpenCV
import os
# Variables
join_type = "h"  # h, horizontal; v, vertical

path_folder_images = r"Resultado/02"

# Ampliar si hace falta
format_list = [".jpg", ".png"]
image_list = []


# El tamaño de las imágenes tiene que ser el mismo, también la extension, si no da error al leerlas
# Podría colocar un filtro por tamaño de imagen, siendo el tamaño de referencia el de la primera foto
primera_iteracion = True
for root, dir, files in os.walk(path_folder_images):
    for file in files:
        print(file)
        extension = os.path.splitext(file)[1]
        if extension.lower() in format_list:
            img_path = os.path.join(root, file)
            img = cv2.imread(img_path)
            try:
                height, width, channel = img.shape
            except:
                print("Error de lectura de tamaño")
                height, width = 0, 0
            print(height, width)
            if primera_iteracion:
                original_height = height
                original_width = width
                print('Original width:  ', original_width)
                print('Original height: ', original_height)
                primera_iteracion = False
            if (height == original_height) & (width == original_width):
                image_list.append(img_path)
            else:
                print(f"Archivo {img_path} no cumple tamaño")
        else:
            print(f"Archivo {file} no cumple el formato")

# print(image_list)

# Leemos los paths de las imágenes y las cargamos a una lista
print("Cargando imagenes")
image_read_list = [cv2.imread(img_path) for img_path in image_list]

v_img = cv2.vconcat(image_read_list)
h_img = cv2.hconcat(image_read_list)

v_img = cv2.resize(v_img, (0, 0), fx=0.1, fy=0.1)
h_img = cv2.resize(h_img, (0, 0), fx=0.1, fy=0.1)

# cv2.imshow('Horizontal', h_img)
# cv2.imshow('Vertical', v_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Path y variable imagen
print("Guardando imagen vertical")
cv2.imwrite(r'Resultado\\v_image.png', v_img)
print("Guardando imagen horizontal")
cv2.imwrite(r'Resultado\\h_image.png', h_img)





