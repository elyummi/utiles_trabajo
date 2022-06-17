import pandas as pd
import os

#Variables
files_path = "todos_2"
lista_files = []
lista_buscados = ["4CJ9H2000171240322","4CJ9H2000166200322",
"0BZ017238940290322","0BZ017238942400322",
"0BZ017238946170322","0BZ017238947530322",
"0BZ017191171733421","0BZ017191171553421",
"0BZ017239260390322","0BZ017234931060222",
"4BZ0H2000098590222","4BZ0H2000096470222",
"0BZ017191171043421","0BZ017191171473421"]
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
