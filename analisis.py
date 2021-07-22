#Parte 2: analisis de los datos

#Librerias
import pandas as pd
import statistics as st

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
series_number = 10
series_size = 50

#Funciones

def realizar_analisis(series_number,series_size,df_analizar):
    '''fsfefsefsefefes'''
    for serie_actual in range(series_number):
        data_values_list = []
        reference_values_list = []
        inicio = serie_actual * series_size
        for j in range(inicio, series_size + inicio):
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
        # Añadir: sensibility_list
        lista_resultados = [reference_values_mean, data_values_mean,
                            sensibility_mean, sensibility_des_vest, irrandiance_mean]
        # Guardamos la serie con sus datos en un diccionario
        series_results[serie_actual] = lista_resultados
    return series_results

#Main
csv_analizar_path = "limpio.csv"
df_analizar = pd.read_csv(csv_analizar_path)
series_results = realizar_analisis(series_number,series_size,df_analizar)
print(series_results)