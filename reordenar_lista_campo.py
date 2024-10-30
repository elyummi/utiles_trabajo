import csv

lista_escribir = []
planta = "inicio"
ufv = "inicio"
mesa = "inicio"
modulo = "inicio"
output = "salida.csv"
modulo_old = ""
with open(output, "w", newline='', encoding='utf-8') as output_file:
    with open(r"Registro todos dani.txt", encoding='utf-8') as file:

        for line in file.readlines():
            line = line.replace("\n", "")
            lista_escribir = []

            if len(line) > 0:
                match line[0]:
                    case "M":
                        planta = line
                    case "U":
                        ufv = line
                    case "E":
                        mesa = line
                    case int():
                        modulo = line
                    case _:
                        modulo = line

                if modulo == modulo_old:
                    pass
                elif "AB" in modulo:
                    lista_escribir.extend([planta, ufv, mesa, str(modulo[:-2])+"A"])
                    string_escribir = ",".join(lista_escribir)
                    wr = csv.writer(output_file, delimiter=',')
                    wr.writerow(lista_escribir)
                    lista_escribir = []

                    lista_escribir.extend([planta, ufv, mesa, str(modulo[:-2])+"B"])
                    string_escribir = ",".join(lista_escribir)
                    wr = csv.writer(output_file, delimiter=',')
                    wr.writerow(lista_escribir)

                    modulo_old = modulo

                else:
                    lista_escribir.extend([planta, ufv, mesa, modulo])
                    string_escribir = ",".join(lista_escribir)


                    wr = csv.writer(output_file, delimiter=',')
                    wr.writerow(lista_escribir)
                    modulo_old = modulo

            #print(planta, ufv, mesa, modulo)
