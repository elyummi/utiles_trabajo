#Programa para crear un .csv para luego importar a excel y que sea más facil hacer la trazabilidad

#Columnas del excel: Día ZONA FILA MESA SUBMESA POSICIÓN CÓDIGO [Orig EL image] !!REVISAR¡¡

#POR HACER: funcion que asigne un identificador a los modules que forman parte de la misma mesa, pero que
# estan a diferentes alguras y, si puede ser, que los ordene por filas/mesas

#Variables

lista_zonas = ["A","B","C","D"]
lista_tipo_mesa = ["14","28"]
lista_ordenadores = ["s","f"] #Para comprobar que se introduce un ordenador corrector
lista_alturas = ["H","L"] #High y Low

#Ubicacion de los archivos
file_path_saul = "saul_prueba.csv"
file_path_felix = "felix_prueba.csv"

#Funciones

def pedir_dia():
    #Solicita el día al usuario. Solo el día, ya que el mes sera febrero (2) y el año 2021
    while True:
        try:
            dia = int(input("Introduce el día: ")) #1,2,3,4...
        except ValueError:
            print("El día debe ser un número. Prueba otra vez.")
            continue
        try:
            mes = int(input("Introduce el mes: ")) #1,2,3,4...
        except ValueError:
            print("El mes debe ser un número. Prueba otra vez.")
            continue
        else:
            dia = str(dia)
            mes = str(mes)
            break

    dia_completo = dia + "/" + mes + "/2021"
    print("La fecha escogida es: ",dia_completo)
    return dia_completo

def pedir_info_posicion():
    #Solicita al usuario info sobre la posición de la foto. Zona (A,B,C,D),Fila, Mesa etc
    while True:
        zona = str(input("Zona: ")).upper() #A,B,C,D
        if zona in lista_zonas:
            break
        else:
            print("Las zonas son: ", lista_zonas)

    while True:
        try:
            fila = int(input("Numero de fila: ")) #1,2,3,4...
        except ValueError:
            print("Fila debe ser un número. Prueba otra vez.")
            continue
        else:
            fila = str(fila)
            break

    while True:
        try:
            mesa = int(input("Numero de mesa: ")) #1,2,3,4...
        except ValueError:
            print("Mesa debe ser un número. Prueba otra vez.")
            continue
        else:
            mesa = str(mesa)
            break

    while True:
        altura = str(input("Altura (H/L): ")).upper() #H, L
        if altura in lista_alturas:
            break
        else:
            print("La altura debe ser High (H) o Low (L): ")

    return zona,fila,mesa,altura



def pedir_tipo_mesa():
    # Solicita al usuario info el tipo de mesa, interior(14 modulos) o exterior(28 modulos)
    while True:
        tipo_mesa = str(input("¿Mesa de 14 o 28?: "))  # Si la mesa es exterior (de 7+7) o interior (de 14+14)
        if tipo_mesa in lista_tipo_mesa:
            break
        else:
            print("Las mesas deben ser de 14 o de 28")
    return tipo_mesa

#CAMBIAR PARA SAUL Y FELIX
def pedir_ordenador(file_path_dani,file_path_otro):
    #Pide al usuario el nombre del ordenador donde estan las fotos. Dani o ¿Saul?
    while True:
        ordenador = str(input("Ordenador de Saúl (s) o Felix (f): "))
        if ordenador in lista_ordenadores:
            break
        else:
            print("Escoge la opcion s/f.")
    if ordenador == "s":
        prefijo_foto = "SA_"
        print("Ordenador de Saúl, fotos con ", prefijo_foto)
        file_path_escogido = file_path_saul
    elif ordenador == "f":
        prefijo_foto = "FF_" #Esto queda asi de momento
        print("Ordenador de Felix, fotos con ", prefijo_foto)
        file_path_escogido = file_path_felix
    return prefijo_foto,file_path_escogido

def pasar_info_csv(lista_csv,file_path_escogido):
    #Solicita al usuario si quiere pasar los datos o volver a escribirlos
    #Coge la lista con las strings lista para pasar a un archivo y las añade al final del mismo
    confirmacion = input("¿Pasar los datos al archivo .csv? (s/n):")
    if confirmacion == "s":
        #Escribimos los datos en el csv
        with open(file_path_escogido,"a") as file:
            for fila_csv in lista_csv:
                file.write(fila_csv+"\n")
        file.close()
        print("ARCHIVO ACTUALIZADO")
        print("-------------------")

    elif confirmacion == "n":
        #Volvemos al inicio del programa
        print("Volviendo a inicio del programa.")
        print("--------------------------------")
    return confirmacion

def crear_info_mesa(num_ultima_foto,dia_completo,file_path_escogido):
    #Crea la info para la mesa completa en funcion de los datos pasador por el usuario en las otra funciones
    zona,fila,mesa,altura = pedir_info_posicion()
    tipo_mesa = pedir_tipo_mesa()
    lista_codigos = []
    lista_csv = []
    num_foto_temporal = num_ultima_foto #Guarda el numero de la ultima foto antes de modificarlo
    #Creamos los codigos en funcion de si la mesa es de interior o exterior
    print("Iniciando introducción de datos")
    if tipo_mesa == "14":
        for posicion in range(1,8):
            if posicion % 2 != 0:
                num_ultima_foto += 1
            nombre_foto = prefijo_foto+str(num_ultima_foto).zfill(5)
            codigo = zona+"-"+altura+"-"+zona+fila+"."+mesa+"-"+str(posicion)
            lista_codigos.append(codigo)
            fila_csv = dia_completo + "," + zona + "," + altura + "," + fila + "," + mesa + "," + str(posicion) +\
                       "," + codigo + "," + nombre_foto
            lista_csv.append(fila_csv)
        print("Comprueba la información: ")
        print("Inicio de la fila: ",lista_codigos[0])
        print("Final de la fila: ",lista_codigos[6])
    elif tipo_mesa == "28":
        for posicion in range(1,15):
            if posicion % 2 != 0:
                num_ultima_foto += 1
            nombre_foto = prefijo_foto+str(num_ultima_foto).zfill(5)
            codigo = zona+"-"+altura+"-"+zona+fila+"."+mesa+"-"+str(posicion)
            lista_codigos.append(codigo)
            fila_csv = dia_completo + "," + zona + "," + altura + "," + fila + "," + mesa + "," + str(posicion) +\
                       "," + codigo + "," + nombre_foto
            lista_csv.append(fila_csv)
        print("Comprueba la información: ")
        print("Inicio de la fila: ",lista_codigos[0])
        print("Final de la fila: ",lista_codigos[13])
    #leer_ultimo_num_foto(file_path_escogido) #Esta linea creo que no hace falta para nada
    confirmacion = pasar_info_csv(lista_csv,file_path_escogido)
    if confirmacion == "n":
        num_ultima_foto = num_foto_temporal
    return lista_codigos, lista_csv,num_ultima_foto

def mostrar_info(lista_codigos):
    #ESTA FUNCION ESTA SIN USAR
    # Muestra el codigo para varias fotos para comprobar que es correcto y pide confirmación al usuario
    print(lista_codigos)


def leer_ultimo_num_foto(file_path_escogido):
    #Lee el último número de foto para poder continuar la cuenta
    #num_ultima_foto es el int que indica el numero de foto
    #el string para colocar en el nombre de cada archivo de foto es: str(num_ultima_foto).zfill(5)
    try:
        with open(file_path_escogido,"r") as file:
            last_line = file.readlines()[-1]
            num_ultima_foto = int(last_line[-5:])
    except FileNotFoundError:
        num_ultima_foto = 0
        print("No se encuentra el archivo ",file_path_escogido)
        print("Empezando desde numero de foto: ",num_ultima_foto)
    return num_ultima_foto

def escoger_num_foto(num_ultima_foto):
    #Pregunta al usuario que numero de foto quiere y usa ese.
    print("Número de foto actual: ",num_ultima_foto)
    try:
        num_ultima_foto = int(input("Numero de foto deseado: ")) #1,2,3,4...
    except ValueError:
        print("El número de foto debe ser un número. Prueba otra vez.")
    print("Numero de foto escogido: ",num_ultima_foto)
    return num_ultima_foto


#Main program
prefijo_foto, file_path_escogido = pedir_ordenador(file_path_saul, file_path_felix)
num_ultima_foto = leer_ultimo_num_foto(file_path_escogido)
dia_completo = pedir_dia()
while True:
    print("Escoge una opción: ")
    opcion = input("Cerrar el programa (cerrar)|Cambiar ordenador (ordenador)|"
                   "Cambiar la fecha(fecha)|Cambiar número de foto(foto)|Seguir sin cambios(s): ")
    if opcion == "cerrar":
        break
    elif opcion == "ordenador":
        prefijo_foto, file_path_escogido = pedir_ordenador(file_path_saul, file_path_felix)
    elif opcion == "fecha":
        dia_completo = pedir_dia()
    elif opcion == "foto":
        num_ultima_foto = escoger_num_foto(num_ultima_foto)
    elif opcion == "s":
        lista_codigos, lista_csv,num_ultima_foto = crear_info_mesa(num_ultima_foto,dia_completo,file_path_escogido)
    else:
        print("Opcion incorrecta. Escoge entre (cerrar/ordenador/fecha/s)")