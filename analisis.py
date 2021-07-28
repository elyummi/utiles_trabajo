#Parte 2: analisis de los datos

#TODO:
#Crear un programa de limpieza (el previo a este) más robusto
#Juntar ambos programas en uno único
#Guardar los resultados del analisis, para no tener que calcularlos cada vez que ejecutamos el progama
#Permitir leer estos resultados guardados por nosotros para poder crear graficos o hacer otros calculos
#Guardar los resultados útiles, sensibilidad final, por ejemplo, en un archivo txt
#Permitir parametrizacion por el usuario, con un json, por ejemplo
#HARD - Conseguir un programa que funciones en ventanda de windows
#EPIC - Conseguir que el programa cree el informe

#Librerias
import os
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
from datetime import datetime

#Filepaths names
filename_date_format = "%d-%m-%Y_%H-%M-%S"
csv_analizar_path = "limpio_2.csv"

graph_folder = "graficos"
graph_file_extension = ".png"
sensibility_plot_filename = "/" + "sensibility_plot_"
irradiance_plot_filename = "/" + "irradiance_plot_"

results_folder = "results"
results_file_extension = "txt"
results_filename = "/" + "resultados_"

analisis_folder = "analisis"
analisis_file_extension = "" #<------------------------------
analisis_filename = "/" + "analisis"


#Variables
data_values_list = []
reference_values_list = []
sensibility_list = []
irrandiance_list = []
series_results = {}
#Factor del patron Hukseflux en (W*m^-2)/mV
factor_calibracion_referencia = 61.34969
#Sensibilidad del patron Hukseflux mV/(W*m^-2)
sensibilidad_referencia = 1/factor_calibracion_referencia
user_series_number = 200
series_size = 100
#Irrandiancia minima valida (W/m2)
irradiancia_min = 600

#Funciones

def create_folders(graph_folder,results_folder,analisis_folder):
    '''Comprueba si existen, y en caso contrario crea, las carpetas donde se almacena la informacion
    creada por el programa'''
    #Esta linea lee las variables locales de la funcion y obtiene .values(), sus valores
    folder_list = locals().values()
    for folder in folder_list:
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Carpeta ",folder," no encontrada. Creando carpeta.")
        else:
            print("Carpeta ",folder," encontrada.")
    print("------------------------------")

def check_series_number(user_series_number, series_size,max_data_values):
    '''Comprueba cuantas series del tamaño introducido por el usuario existen en los datos. Si la cantidad
    disponible de series es menor que la que el usuario desea, se envia un mensaje por pantalla con el
    número maximo de series que se pueden realizar. El programa continúa con normalidad utilizando este
    nuevo número de series.'''
    if series_size>max_data_values:
        print("Especial")
        #Caso especial: el tamaño de 1 unica serie es mayor que el total de valores disponibles
        series_number = 1
        series_size = max_data_values-1
        final_series = 0
        print("Valores a analizar: ", (series_number) * series_size + final_series)
    elif user_series_number*series_size<= max_data_values:
        series_number = user_series_number
        series_size = series_size
        final_series = 0
        print("Valores a analizar: ", (series_number) * series_size + final_series)
    else:
        #Caso general
        series_number = max_data_values//(series_size)
        final_series = max_data_values%(series_size)
        if final_series != 0:
            series_number += 1
        print("Valores a analizar: ", (series_number-1)*series_size+final_series)
    print("Número de series: ", series_number)
    print("Tamaño de las series: ", series_size)
    print("Tamaño de la ultima serie: ",final_series)
    return series_number,series_size,final_series


def realizar_analisis(series_info,df_analizar):
    '''Recoge el archivo a analizar, el tamaño y número deseado para las series y devuelve los datos de
    sensibilidad pada cada valor, media de los valores de referencia, media de los valores a analizarm
    media de la sensibilidad, desviación típica de la sensibiliadad y media de la irradiancian'''
    cuarto = series_info[0]// 4
    print("#----------------Inicio del analisis----------------#")
    hora_inicio = datetime.now()
    print("Hora inicio: ", hora_inicio)
    print("Progreso:")
    for serie_actual in range(series_info[0]):
        data_values_list = []
        reference_values_list = []
        irrandiance_list = []
        inicio = serie_actual * series_info[1]
        fin = series_info[1] + inicio
        # Barra para indicar el progreso del analisis
        if serie_actual == round(cuarto*0.5):
            print("|====----------------------------|")
        elif serie_actual == cuarto:
            print("|========------------------------|")
        elif serie_actual == round(cuarto*1.5):
            print("|============--------------------|")
        elif serie_actual == 2*cuarto:
            print("|================----------------|")
        elif serie_actual == round(cuarto * 2.5):
            print("|====================------------|")
        elif serie_actual == 3*cuarto:
            print("|========================--------|")
        elif serie_actual == round(cuarto * 3.5):
            print("|============================----|")
        elif serie_actual == 4*cuarto:
            print("|================================|")

        if serie_actual+1 == series_info[0] and series_info[2] != 0:
            fin = series_info[2] + inicio -1
        for j in range(inicio, fin):
            # Leemos los valores de voltaje para la referencia y el piranometro a calibrar
            reference_values_list.append(df_analizar.at[j, "mV"])
            data_values_list.append(df_analizar.at[j, "mV.1"])
            # Calculamos la sensibilidad para cada par de valores
            sensibility_list.append(
                1 / (factor_calibracion_referencia * (df_analizar.at[j, "mV"]) / (df_analizar.at[j, "mV.1"])) * 1000)
            # Calculamos la irrandiancia para cada valor de la referencia
            irrandiance_list.append(df_analizar.at[j, "mV"] / sensibilidad_referencia)
        # Calculamos la media de los valores obtenidos anteriormente
        reference_values_mean = st.mean(reference_values_list)
        data_values_mean = st.mean(data_values_list)
        # Calculamos la sensibilidad a partir de los valores medios en µV/(W*m-2)
        sensibility_mean = 1 / (factor_calibracion_referencia * (reference_values_mean / data_values_mean)) * 1000
        # Calculamos la irradiancia media
        irrandiance_mean = st.mean(irrandiance_list)
        # Calculamos la desviación típica de las sensibilidades calculadas por pares
        sensibility_des_vest = st.stdev(sensibility_list)
        # Almacenamos los diferentes resultados de cada serie
        lista_resultados = [sensibility_list, reference_values_mean, data_values_mean,
                            sensibility_mean, sensibility_des_vest, irrandiance_mean]
        # Guardamos la serie con sus datos en un diccionario
        series_results[serie_actual] = lista_resultados
    hora_fin = datetime.now()
    tiempo_transcurrido = hora_fin - hora_inicio
    print("#----------------Analisis completado----------------#")
    print("Hora de finalización: ", hora_fin)
    print("Tiempo total: ", tiempo_transcurrido)
    return series_results

def realizar_analisis_final(series_results,irradiancia_min):
    '''Calculamos la sensibilidad definitiva a partir de los datos del diccionario obtenido
    con la funcion realizar_analisis'''
    final_sensibility_list = []
    for key, value in series_results.items():
        # Comprueba que la irradiancia es superior s la min (habitualmente consideramos 600W/m2)
        if value[5] > irradiancia_min:
            final_sensibility_list.append(value[3])
    # Comprobar el numero de series que existen
    final_sensibility = st.mean(final_sensibility_list)
    final_sensibility_des_vest = st.stdev(final_sensibility_list)
    print("Sensibilidad calculada: ", final_sensibility)
    print("Desviación típica: ", final_sensibility_des_vest)
    return final_sensibility,final_sensibility_des_vest,final_sensibility_list

def calculo_irradiancia(df_analizar,max_data_values,sensibilidad_referencia,final_sensibility):
    print(locals().keys())
    '''Calculamos la irradiancia en W/m2 para la referencia, usando su valor de sensibilidada, y para
    el piranometro a analizar, usando la sensibilidad calculada con el programa anteriormente. Devuelve
    ambas listas para ser ploteadas'''
    reference_irradiance_list = []
    data_irradiance_list = []
    time_values_list = []
    #Para representar en el grafico. Busca cual es el formato de fecha que coincide con el del archivo csv
    try:
        datetime.strptime(df_analizar.at[0, "Time"], '%Y/%m/%d %H:%M:%S')
        date_format = '%Y/%m/%d %H:%M:%S'
    except:
        datetime.strptime(df_analizar.at[0, "Time"], '%d/%m/%Y %H:%M')
        date_format = '%d/%m/%Y %H:%M'
    for j in range(max_data_values-1):
        time_values_list.append(datetime.strptime(df_analizar.at[j,"Time"], date_format))
        reference_irradiance_list.append(df_analizar.at[j,"mV"]/sensibilidad_referencia)
        data_irradiance_list.append(df_analizar.at[j,"mV.1"]/final_sensibility*1000)
    return reference_irradiance_list, data_irradiance_list,time_values_list

def save_analisis_data():
    return

def read_analisis_data():
    return

#Funciones para gráficos

def create_sensibility_plot(final_sensibility,final_sensibility_list,filename_date_format,graph_folder,sensibility_plot_filename,graph_file_extension):
    # Definimos el objeto de matplolib
    fig, (ax1, ax2) = plt.subplots(1, 2)
    print("Creando gráfico de sensibilidades")
    # Definimos valores a representar y parametros de visualizacion
    ax1.scatter(range(len(final_sensibility_list)), final_sensibility_list, marker=".", color="blue")
    ax1.axhline(final_sensibility, color="red")
    # Añadimos titulo y leyendas
    ax1.set(title="Sensibilidad por serie", xlabel="Serie", ylabel="Sensibilidad\n(µV/(W*m^2)")
    # Histograma de sensibilidades
    ax2.hist(final_sensibility_list, bins=5, edgecolor='black', rwidth=0.9)
    ax2.axvline(final_sensibility, color="red")
    # Guardamos el grafico como archivo png
    hora_filename = datetime.now().strftime(filename_date_format)
    sensibility_plot_filepath = graph_folder + sensibility_plot_filename + hora_filename + graph_file_extension
    plt.savefig(sensibility_plot_filepath, dpi=1000)
    plt.show()

def crear_irradiance_plot(time_values_list,irradiancia_referencia,irradiancia_data,filename_date_format,graph_folder,irradiance_plot_filename,graph_file_extension):
    # Grafico irradiancia
    fig, ax3 = plt.subplots()
    print("Creando gráfico de irradiancia")
    ax3.scatter(time_values_list, irradiancia_referencia, marker="x", color="green")
    ax3.scatter(time_values_list, irradiancia_data, marker=".", color="red")
    plt.title("Comparación de irradiancias")
    plt.xlabel("Time")
    plt.ylabel("Irradiancia en W/m^2")
    plt.ylim([600, 1500])
    hora_filename = datetime.now().strftime(filename_date_format)
    irradiance_plot_filepath = graph_folder + irradiance_plot_filename + hora_filename + graph_file_extension
    plt.savefig(irradiance_plot_filepath, dpi=1000)
    plt.show()


####-------------------------MAIN-------------------------####
create_folders(graph_folder,results_folder,analisis_folder)
df_analizar = pd.read_csv(csv_analizar_path)
print("Analizando archivo: ", csv_analizar_path)
#Valores disponibles en el csv de datos
max_data_values = df_analizar.iloc[-1,0]
print("Valores disponibles: ", max_data_values)

series_info = check_series_number(user_series_number,series_size,max_data_values)

series_results = realizar_analisis(series_info,df_analizar)

final_sensibility, final_sensibility_des_vest, final_sensibility_list = realizar_analisis_final(series_results,irradiancia_min)

irradiancia_referencia, irradiancia_data, time_values_list = calculo_irradiancia(df_analizar,max_data_values,sensibilidad_referencia,final_sensibility)

#GRAFICOS

create_sensibility_plot(final_sensibility,final_sensibility_list,filename_date_format,graph_folder,sensibility_plot_filename,graph_file_extension)
crear_irradiance_plot(time_values_list,irradiancia_referencia,irradiancia_data,filename_date_format,graph_folder,irradiance_plot_filename,graph_file_extension)