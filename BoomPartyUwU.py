"https://jklm.fun/"

import pyautogui
import time
import pyperclip
import cv2
import numpy as np
from PIL import Image
import unicodedata
import random


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
def rellenar(tiempoesp, realista, tiemporealista, timepoMove):
    tiempoMoveRan = random.uniform(timepoMove-0.05, timepoMove+0.05)

    time.sleep(tiempoesp)
    pyautogui.moveTo(posiciones[0], duration=tiempoMoveRan)
    time.sleep(tiempoesp)
    texto = seleccionar_y_copiar_texto()
    texto = texto.lower()
    time.sleep(tiempoesp)
    pyautogui.moveTo(posiciones[1], duration=tiempoMoveRan)
    pyautogui.click()
    time.sleep(tiempoesp)
    textA = DevPalabra(texto)
    if(realista):
        for i in range(len(textA)):
            time.sleep(random.uniform(tiemporealista-0.001, tiemporealista+0.001))
            pyautogui.write(reemplazar_ñ_y_quitar_acentos(textA[i]))
    else:
        pyautogui.write(reemplazar_ñ_y_quitar_acentos(textA))
    pyautogui.press('enter')
    print("Escrita: " + textA)
def reemplazar_ñ_y_quitar_acentos(texto):
    texto = texto.replace('ñ', 'n')
    texto_sin_acentos = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
    return texto_sin_acentos
import random
def DevPalabra(subcadena):
    global palabras_devueltas
    # Abre el archivo de texto y lee las palabras con la codificacion que requiera
    with open('diccionario.txt', 'r', encoding='utf-8') as f:
        diccionario = [line.strip() for line in f]
    palabras_posibles = [palabra for palabra in diccionario if palabra.startswith(subcadena) and palabra not in palabras_devueltas]
    if palabras_posibles:
        palabra_elegida = random.choice(palabras_posibles)
        palabras_devueltas.append(palabra_elegida)
        return palabra_elegida
    else:
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
        rellenar(0.1, realista, 0.007, 0.1)
    time.sleep(0.5)
