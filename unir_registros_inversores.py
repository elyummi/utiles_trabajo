#Creado por Daniel Villoslada Fontán
import os

string_eliminar = "date;time;id;POWAct (W);VDC (V);IDC (A);VAC1 (V);VAC2 (V);VAC3 (V);IAC1 (A);IAC2 (A);IAC3 (A);Fre (Hz);Temp (C);EAexp Act (kWh);Alarm"
folder_name = "INVERSORES"
csv_file_name = "Fronius_ModbusTCP_0000"
#Esta variable tendrá valores de 1 a 4
inversor_file_number_list = [1,2,3,4]

for num in inversor_file_number_list:
    print("Limpiando inversor ",str(num))

    search_file_name = csv_file_name + str(num)

    #Leemos el path de trabajo actual y extraemos los nombres de todos los archivos de el
    current_working_dir = os.getcwd()
    folder_path = current_working_dir + "/" + folder_name
    all_file_list = os.listdir(folder_path)

    output_text_list = []

    for file_name in all_file_list:
        if search_file_name in file_name:
            complete_file_name = folder_path + "/" + file_name
        #Abrimos cada archivo para lectura y extraemos toda la info
            with open(complete_file_name) as file:
                complete_file_no_first = file.readlines()
                for line in complete_file_no_first:
                    output_text_list.append(line)

    output_text = "\n".join(output_text_list).replace(string_eliminar,"").replace(" ","")
    final_output_text = string_eliminar + "\n" + output_text
    output_text_file_name = "output_inv_" + str(num) + ".csv"
    output_file = open(output_text_file_name, "w")
    output_file.write(final_output_text)
    output_file.close()
print("COMPLETADO")