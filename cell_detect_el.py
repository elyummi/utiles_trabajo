"""Python script to demonstrate Canny edge detection.
https://datacarpentry.org/image-processing/edge-detection.html
usage: python CannyEdge.py <filename> <sigma> <low_threshold> <high_threshold>
Para investigar:
https://scikit-image.org/docs/stable/auto_examples/applications/plot_coins_segmentation.html
"""
import datetime
import imageio.v3 as iio
import matplotlib.pyplot as plt
import skimage.feature
import cv2 # OpenCV
import numpy as np
import math

# listas, están en valores enteros, por eso luego se divide entre 10
list_sigma = [x for x in [*range(1, 13)]]
list_low_threshold = [x /10 for x in [*range(0, 11, 2)]]
list_high_threshold = [x /10 + 0.05 for x in [*range(0, 11, 2)]]

# read command-line arguments
filename = r"Muestra EL/COR_2076.jpg"
# filename = r"Muestra tracker/Tracker_1.JPG"
sigma = 3
low_threshold = 0.1
high_threshold = 0.9

# load and display original image as grayscale
img_original = iio.imread(uri=filename, mode="L")
# plt.imshow(image)
# plt.show()


# Imágenes con diferentes valores para detección de bordes
if "a" == "b":
    # Bucles para pruebas
    for sigma_value in list_sigma:
        for high_threshold_value in list_high_threshold:
            for low_threshold_value in list_low_threshold:
                print(f"Sigma: {sigma_value}")
                print(f"high_threshold_values: {high_threshold_value}")
                print(f"low_threshold_value: {low_threshold_value}")
                print("--------------------")
                if low_threshold_value < high_threshold_value:
                    # Esta es la parte que tarda
                    img_edges = skimage.feature.canny(
                        image=img_original,
                        sigma=sigma_value,
                        low_threshold=low_threshold_value,
                        high_threshold=high_threshold_value)
                    img_edges = skimage.util.img_as_ubyte(img_edges)
                    # display edges
                    # skimage.io.imshow(img_edges)
                    # skimage.io.show()
                    psnr = skimage.metrics.peak_signal_noise_ratio(img_original, img_edges)
                    blur_metric = skimage.measure.blur_effect(img_edges)
                    # Hacer que se muestren
                    hist_original = skimage.exposure.histogram(img_original)
                    hist_edge = skimage.exposure.histogram(img_edges)
                    print("PSNR (Peak signal to noise ratio): ", psnr)
                    print("Blur metric: ", blur_metric)
                    # print("Histograma original: ", hist_original)
                    # print("Histograma final: ", hist_edge)
                    print("--------------------")
                    skimage.io.imsave(f'Resultado\\image_S_{sigma_value}_LT_{low_threshold_value}_HT_{high_threshold_value}.png', img_edges)


if "a" == "b":
    # Para usarlo directamente
    edges = skimage.feature.canny(
        image=img_original,
        sigma=sigma,
        low_threshold=low_threshold,
        high_threshold=high_threshold,
    )

    # display edges
    skimage.io.imshow(edges)
    skimage.io.show()

# Connected component labelling
# https://stackoverflow.com/questions/59150197/how-to-identify-distinct-objects-in-image-in-opencv-python
if "a" == "b":
    # Load the image in grayscale
    input_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    # resize_image = cv2.resize(input_image, (0, 0), fx=0.1, fy=0.1)
    ready_image = input_image#resize_image

    # Threshold your image to make sure that is binary
    thresh_type = cv2.THRESH_BINARY + cv2.THRESH_OTSU
    _, binary_image = cv2.threshold(ready_image, 0, 255, thresh_type)

    # Distintos tipos de filtros para la imagen
    # Para modulos EL, valores sobre 150 (treshold1) funcionan bien, aunque para nada perfecto
    thresh_value = 150

    ret, thresh1 = cv2.threshold(ready_image, thresh_value, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(ready_image, thresh_value, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(ready_image, thresh_value, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(ready_image, thresh_value, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(ready_image, thresh_value, 255, cv2.THRESH_TOZERO_INV)

    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [ready_image, thresh1, thresh2, thresh3, thresh4, thresh5]

    binary_image = thresh1 #Aqui indicamos que filtro queremos usar, de todos los disponibles
    binary_image = cv2.resize(binary_image, (0, 0), fx=0.15, fy=0.15)

    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    # plt.show()

    # Perform connected component labeling
    n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image, connectivity=4)
    print("Total de centroides: ", len(centroids))

    # Create false color image
    colors = np.random.randint(0, 255, size=(n_labels , 3), dtype=np.uint8)
    colors[0] = [0, 0, 0]  # for cosmetic reason we want the background black
    false_colors = colors[labels]

    # false_colors = cv2.resize(false_colors, (0, 0), fx = 0.15, fy = 0.15)
    cv2.imshow('binary', binary_image)
    cv2.imshow('false_colors', false_colors)
    cv2.waitKey(0)

    false_colors_draw = false_colors.copy()
    for centroid in centroids:
        cv2.drawMarker(false_colors_draw, (int(centroid[0]), int(centroid[1])),
                       color=(255, 255, 255), markerType=cv2.MARKER_CROSS)
    cv2.imshow('false_colors_centroids', false_colors_draw)
    cv2.waitKey(0)

    min_area = 100
    false_colors_draw = false_colors.copy()
    for i, centroid in enumerate(centroids[1:], start=1):
        area = stats[i, 4]
        if area > min_area:
            cv2.drawMarker(false_colors_draw, (int(centroid[0]), int(centroid[1])),
                           color=(255, 255, 255), markerType=cv2.MARKER_CROSS)

if "a" == "a":
    # window size for the Gaussian Smoothing (larger values will make the corners less localized)
    blockSize = 12
    # kernel size for the Sobel Operators
    ksize = 3
    # hyperparameter for the Harris Corner Response (smaller values allow more features to be detected)
    k = 0.025
    # convert image to grayscale float

    # compute Harris Corner responses
    # R = cv2.cornerHarris(gray_1.astype(np.float32), blockSize, ksize, k)

    # Load the image in grayscale
    # input_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    input_image = cv2.imread(filename)
    input_image = cv2.resize(input_image, (0, 0), fx=0.1, fy=0.1)
    ready_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    plt.figure()
    plt.subplot(141)
    plt.imshow(input_image)
    plt.subplot(142)
    plt.imshow(ready_image)
    # Detección de esquinas
    dst = cv2.cornerHarris(ready_image, 12, 3, 0.025)

    # result is dilated for marking the corners, not important
    # dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    # Si el valor en dst es mayor que el un percentage del máximo, entonces pinta esos pixeles en la imagen original
    coef_corner = 0.1  # Para indicar que punto son esquinas
    input_image[dst > coef_corner * dst.max()] = [255, 0, 0]
    # print(input_image)

    plt.subplot(143)
    plt.imshow(input_image)
    # plt.show()

    height, width, channels = input_image.shape

    coord_centro_imagen = [height/2, width/2]
    lista_puntos_lejanos = [[[0, 0], 0], [[0, 0], 1000000]]
    lista_puntos_encontrados = []
    punto_menor_x = [100000000, 0]
    punto_mayor_x = [0, 0]
    punto_menor_y = [0, 100000000]
    punto_mayor_y = [0, 0]
    # Idea: buscar las esquinas alejadas del centro, y esas serán las esquinas del módulo
    print("Empezando búsqueda pixels")
    for x in range(0, height):
        for y in range(0, width):
            # print(x, y)
            pixel = input_image[x, y]
            # print(input_image[x, y])
            # if (pixel & [255, 0, 0]).all():
            if pixel[0] == 255:
                lista_puntos_encontrados.append([x, y])
                # print("PIXEL", x, y, pixel)
                x0 = 0  # coord_centro_imagen[0]
                y0 = 0  # coord_centro_imagen[1]
                distancia_centro_pixel = math.sqrt((x - x0)**2 + (y - y0)**2)
                # print(distancia_centro_pixel)
                if distancia_centro_pixel > lista_puntos_lejanos[0][1]:
                    lista_puntos_lejanos[0] = [[x, y], distancia_centro_pixel]
                elif distancia_centro_pixel < lista_puntos_lejanos[1][1]:
                    lista_puntos_lejanos[1] = [[x, y], distancia_centro_pixel]

    #Buscamos los puntos con mayor y menor x, y mayor y menor y, los anotamos
    for punto in lista_puntos_encontrados:
        if punto[0] < punto_menor_x[0]:
            punto_menor_x = punto
        elif punto[0] > punto_mayor_x[0]:
            punto_mayor_x = punto
        if punto[0] < punto_menor_y[1]:
            punto_menor_y = punto
        elif punto[0] > punto_mayor_y[1]:
            punto_mayor_y = punto

    print([punto_menor_x, punto_mayor_x, punto_menor_y, punto_mayor_y])
    #Dibujamos la forma con los 4 puntos
    # Polygon corner points coordinates
    vertices_poligono = np.array([[punto_menor_x, punto_mayor_x, punto_menor_y, punto_mayor_y]], np.int32)
    vertices_poligono = vertices_poligono.reshape((-1, 1, 2))

    input_image = cv2.polylines(input_image, pts=[vertices_poligono], isClosed=False, thickness=3, color=(0, 0, 255))

    # input_image[lista_puntos_lejanos[0][0]] = [0, 0, 255]
    # input_image[lista_puntos_lejanos[1][0]] = [0, 0, 255]

    # Dibujamos un rectángulo
    start_point = [lista_puntos_lejanos[1][0][1], lista_puntos_lejanos[1][0][0]]
    end_point = [lista_puntos_lejanos[0][0][1], lista_puntos_lejanos[0][0][0]]
    rectangle_color = (0, 255, 0)
    thickness = 3

    # Draw a rectangle with blue line borders of thickness of 2 px
    input_image = cv2.rectangle(input_image, start_point, end_point, rectangle_color, thickness)

    plt.subplot(144)
    plt.imshow(input_image)
    plt.show()

    # # find centroids
    # ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

