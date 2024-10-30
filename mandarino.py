#https://app.tangerino.com.br/Tangerino/pages/HomePage

import pyautogui
import time
import random

mes_seleccionado = "/10"
año_seleccionado = "/2024"
lista_dias_reserva = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16",
                      "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

lista_dias = ["01", "02"]


lista_horas_marcar = ["08:00", "12:00", "13:00", "18:00"]
lista_dias_marcar = []

posicion_fecha = [270, 329]
posicion_hora = [616, 333]
posicion_guardar_continuar = [429, 626]

for i in range(len(lista_dias)):
    # Completamos la fecha con el formato adequadito
    lista_dias_marcar.append(lista_dias[i] + mes_seleccionado + año_seleccionado)

if False:
    for i in range(10000):
        time.sleep(0.5)
        print(pyautogui.position())

# Tomamos aire
time.sleep(5)

# Y vamos allá
for dia in lista_dias_marcar:
    dia = str(dia)
    print("DIA:", dia)
    pyautogui.tripleClick(x=posicion_fecha[0], y=posicion_fecha[1])
    pyautogui.typewrite(dia, interval=0.2)
    time.sleep(1)
    for hora in lista_horas_marcar:
        print("DIA: ", dia, "hora", hora)
        # Añadimos numero aleatorio a la hora para hacerlo mas spicy
        hora = str(hora[:-1] + str(random.randint(0,5)))
        pyautogui.tripleClick(x=posicion_hora[0], y=posicion_hora[1])
        pyautogui.typewrite(hora, interval=0.2)
        time.sleep(1)
        pyautogui.leftClick(x=posicion_guardar_continuar[0], y=posicion_guardar_continuar[1])
        time.sleep(2)
    time.sleep(3)
