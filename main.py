#Programa para limpiar automaticamente log de . DONE
#Eliminar datos erroneos
#Permitir al usuario elegir que columnas quiere guardar, eliminar el resto
#Buscar la forma de que sea facil indicarle al programa donde se encuentran los csv que queremos limpiar

#Variables
#Equivalente en mV de la irradiancia
irradiancia_min_defecto = 7
irradiancia_min = 11

#Librerias
import pandas as pd

#Funciones

def limpiar_df(df_full,irradiancia_min = irradiancia_min_defecto):
    print("empieza")
    #Recoge el csv importado, formatea los valores a int y elimina a en funcion de la irradiancia minima
    for index in range(len(df_full)):
        # Convierte los valores del csv en bruto del formato "+- valor" a int, para que python
        # Pueda trabajar con ellos
        df_full.at[index, "mV"] = pd.to_numeric(df_full.iloc[index, 3].strip(" +-"))
    # Elimina los valores que son menoses al valor irradiancia.min, especificado al inicio
    df_clean = df_full.drop(df_full[df_full.mV < irradiancia_min].index)
    print("done")
    return df_clean

##Extraemos la info del dataframe. Solo si se utiliza el archivo completo, desde la fila 1
#df_cabecera = df_full.iloc[:30] #Informacion que coloca el registrador
#df_datos = df_full.iloc[30:] #Incluye cabecera de datos (nombre y unidades, 2 filas)
#df_datos_exc = df_full.iloc[32:] #Solo los datos, sin cabecera

#MAIN
#Path donde se encuentra el archivo a limpiar
path_csv = r"C:\Users\daniel.villoslada\PycharmProjects\pythonProject\datalog_bruto.CSV"

#Crea un DF de pandas sin tener en cuenta las 30 primeras filas, ya que no contienen los datos que queremos
df_full = pd.read_csv(path_csv,skiprows = 30) #Dataframe de Pandas. Las 30 primeras filas dan problemas

#Limpiamos el csv
df_clean = limpiar_df(df_full,irradiancia_min)

#Pasamos el DF limpio a csv
df_clean.to_csv("limpio.csv", index = False)