"https://jklm.fun/"

import pyautogui
import time
import pyperclip
import cv2
import numpy as np
from PIL import Image

# Variables 
palabras_devueltas = []

# Funciones---------------------------------------------
def optenerPosiciones(timepoEspera):
    posicones = []
    print("Opteniendo posicion texto")
    time.sleep(timepoEspera)
    posicones.append(pyautogui.position())
    print("ya")
    print("Opteniendo posicon escribir")
    time.sleep(timepoEspera)
    posicones.append(pyautogui.position())
    print("ya")
    return posicones
def seleccionar_y_copiar_texto():
    pyautogui.click(clicks=2)
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()
def rellenar(tiempoesp, realista, tiemporealista):
    time.sleep(tiempoesp)
    pyautogui.moveTo(posiciones[0])
    time.sleep(tiempoesp)
    texto = seleccionar_y_copiar_texto()
    texto = texto.lower()
    time.sleep(tiempoesp)
    pyautogui.moveTo(posiciones[1])
    pyautogui.click()
    time.sleep(tiempoesp)
    textA = DevPalabra(texto)
    if(realista):
        for i in range(len(textA)):
            time.sleep(tiemporealista)
            pyautogui.write(textA[i])
    else:
        pyautogui.write(textA)
    pyautogui.press('enter')
    print("Escrita: " + textA)
def DevPalabra(subcadena):
    global palabras_devueltas
    # Abre el archivo de texto y lee las palabras con la codificacion que requiera
    with open('diccionario.txt', 'r', encoding='utf-8') as f:
        diccionario = [line.strip() for line in f]
    for palabra in diccionario:
        # Comprueba si la subcadena está en la palabra y si la palabra no ha sido devuelta antes
        if subcadena in palabra and palabra not in palabras_devueltas:
            palabras_devueltas.append(palabra)
            return palabra
    return "No se encontraron más palabras con " + subcadena
def optenerPixColor(pos, timepos):
    print("Opteniendo pixel para saber cuando jugar")
    time.sleep(timepos)
    colorpixel = pyautogui.pixel(pos.x, pos.y)
    print("ya")
    return colorpixel
def CompJugar(pos, colorPixel):
    return (colorPixel != pyautogui.pixel(pos.x, pos.y))


# Codigo---------------------------------------------
print("BoomPartyUwU by PetaZ")

realista = False
print("Para realista pon 1 cualquier otro rápido")
if(input("") == "1"):
    realista = True

print("timepo antes de activarse")
tiempoActi = int(input())

time.sleep(1)
posiciones = optenerPosiciones(2)
colorPixel = optenerPixColor(posiciones[1], 0.1)

time.sleep(tiempoActi)
print("activo")

while True:
    if CompJugar(posiciones[1], colorPixel):
        rellenar(0.1, realista, 0.007)
    time.sleep(0.5)