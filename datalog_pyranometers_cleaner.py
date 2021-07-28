#Programa para limpiar automaticamente log de . DONE
#Eliminar datos erroneos
#Permitir al usuario elegir que columnas quiere guardar, eliminar el resto
#Buscar la forma de que sea facil indicarle al programa donde se encuentran los csv que queremos limpiar

#Variables
#Valores en mV. Equivalente en mV de la irradiancia(600W/m2 <-> 7-8 mV)
irradiancia_min_defecto = 6
irradiancia_min = 7
#Columna (entrada del registrador), de la que queremos los datos (Entre 1 y 9). Columna 0 es la primera
columna_deseada = 1

#Librerias
import pandas as pd

#Funciones
def obtener_csv():
    '''Funcion para indicar al programa cual es el archivo csv que queremos limpiar'''
    return df_full


def limpiar_df(df_full,columna_deseada,irradiancia_min = irradiancia_min_defecto):
    '''Funcion que coge un csv con los datos en bruto del registrador, los formatea para poder trabajar,
    elimina las filas de la columna seleccionada con valores de irradiancia (en mV) indicados por el usuario
    y devuelve la informacion como otro csv
    '''
    print("Limpiando el archivo.")
    print("Eliminando valores menores de ", irradiancia_min, "mV.")
    #Recoge el csv importado, formatea los valores a int y elimina a en funcion de la irradiancia minima

    #Elimina las columnas que no necesitamos.
    try:
        df_full = df_full.drop(columns=["A1234567890"])
    except:
        pass
    try:
        df_full = df_full.drop(columns=["AO1234"])
    except:
        pass
    for i in range(1,10):
        #Pandas llama: nombre + .num, a la columnas con nombres repetidos
        if i is not columna_deseada:
            nombre_columna_eliminar = "mV."+str(i)
            try:
                df_full = df_full.drop(columns = [nombre_columna_eliminar])
            except:
                pass
    # Convierte los valores del csv en bruto del formato "+- valor" a int, para que python
    # pueda trabajar con ellos
    for index in range(len(df_full)):
        try:
            df_full.at[index, "mV"] = pd.to_numeric(df_full.loc[df_full.index[index], "mV"].strip(" +-"))
        except:
            #Si el numero esta delimitado por ",". conevertimos la "," en "." y probamos de nuevo
            #Esto puede pasar si el archivo csv no esta delimitado por ","
            df_full.at[index, "mV"] = pd.to_numeric(df_full.loc[df_full.index[index], "mV"].strip(" +-").replace(",","."))
    #Lo mismo pero para la columna deseada
    nombre_columna_deseada = "mV." + str(columna_deseada)
    for index in range(len(df_full)):
        try:
            df_full.at[index, nombre_columna_deseada] = pd.to_numeric(df_full.loc[df_full.index[index], nombre_columna_deseada].strip(" +-"))
        except:
            df_full.at[index, nombre_columna_deseada] = pd.to_numeric(df_full.loc[df_full.index[index], nombre_columna_deseada].strip(" +-").replace(",", "."))
    # Elimina los valores que son menores al valor irradiancia.min, especificado al inicio
    df_clean = df_full.drop(df_full[df_full.mV < irradiancia_min].index)
    #Da nuevos indices la primera columna, empezando desde 1
    for i in range(df_clean.shape[0]):
        df_clean.iloc[i,0] = i+1
    # Pasamos el DF limpio a csv. Salida a donde se ha ejecutado el programa
    df_clean.to_csv("limpio_2.csv", index=False)
    #Falta indicar aqui la ruta de salida del archivo
    print("Nuevo archivo listo. Ruta: ")
    return df_clean

##Extraemos la info del dataframe. Solo si se utiliza el archivo completo, desde la fila 1
#df_cabecera = df_full.iloc[:30] #Informacion que coloca el registrador
#df_datos = df_full.iloc[30:] #Incluye cabecera de datos (nombre y unidades, 2 filas)
#df_datos_exc = df_full.iloc[32:] #Solo los datos, sin cabecera

#----------------------MAIN-PROGRAM----------------------------------------------------

#Parte 1: abrir y limpiar el csv

#Path donde se encuentra el archivo a limpiar
path_csv_bruto = r"C:\Users\daniel.villoslada\PycharmProjects\pythonProject\datalog_bruto_2.csv"

#Crea un DF de pandas sin tener en cuenta las 30 primeras filas, ya que no contienen los datos que queremos
df_full = pd.read_csv(path_csv_bruto,skiprows = 30, sep = ";") #Dataframe de Pandas. Las 30 primeras filas dan problemas
#Limpiamos el csv
df_clean = limpiar_df(df_full,columna_deseada,irradiancia_min)
