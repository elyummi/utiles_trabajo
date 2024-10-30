import pyautogui
from time import sleep

#Programa principal
modo = "b"

if modo == "a":
    sleep(1)
    for _ in range(1000):
        sleep(0.1)
        posicion_mouse = pyautogui.position()
        print(posicion_mouse)

elif modo == "b":
    sleep(3)
    for _ in range(5000):
        #(59,180), change Slave ID
        #(314,181), change start adress
        #(400,178), change nº of coils
        #(376,237), send
        #(684,390), checkbox
        #Setup
        setup = "n"
        if setup == "s":
            pyautogui.doubleClick(279, 183)  # box numeros start adress
            pyautogui.typewrite("0")  # set to 0
            pyautogui.doubleClick(354, 182)  # box numeros coils
            pyautogui.typewrite("1")  # set to 0

        pyautogui.click(1138, 605) #Send
        sleep(0.5)
        # pyautogui.click(684, 390)  # Checkbox
        #Start adress
        # for i in range(65535):
        #     pyautogui.click(376, 237)  # Send
        #     sleep(1)
        #     pyautogui.click(684, 390)  # Checkbox
        #     pyautogui.doubleClick(279, 183)  # box numeros start adress
        #     pyautogui.typewrite(str(i))  # set to 0
        #     # Coil (10 para irr)
        #     for i in range(65535):
        #         pyautogui.click(376, 237)  # Send
        #         sleep(1)
        #         pyautogui.click(684, 390)  # Checkbox
        #         pyautogui.click(396,180)  # Coils
        # pyautogui.click(59,180) #Slave ID
