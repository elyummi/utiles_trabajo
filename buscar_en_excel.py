import pandas as pd
import os

#Variables
files_path = "Batch 9"
lista_files = []
lista_buscados = ["4CJ9H2000171240322","0BZ017238940290322","0BZ017238946170322","0BZ017191171733421",
                  "0BZ017239260390322","4BZ0H2000098590222","0BZ017191171043421","0BZ017191430473421",
                  "0BZ017191400293421","0BZ017200000363821","0BZ017199963583821","0CR417203970774021",
                  "0BZ017200441553821","0BZ017200442763821","0BZ017200451013821","0CR417204660014021"]
i = 0

#Main
lista_files = os.listdir(files_path)

for file in lista_files:
    i += 1
    #print(i/len(lista_files))
    excel_pandas = pd.read_excel(files_path + "/" + file, header=1)
    excel_pandas_limpio = excel_pandas["Serial No."]
    excel_lista = excel_pandas_limpio.values.tolist()
    for buscado in lista_buscados:
        if buscado in excel_lista:
            print("ENCONTRADO: ",file,";",buscado)
