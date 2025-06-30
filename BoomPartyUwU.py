"https://jklm.fun/"


import unicodedata
import random
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options


# Variables 
palabras_devueltas = []

# Funciones---------------------------------------------
def arreglarWord(texto):
    texto = texto.replace('ñ', 'n')
    texto_sin_acentos = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
    return texto_sin_acentos
def DevPalabra(subcadena):
    global palabras_devueltas
    subcadena = subcadena.lower()
    # Abre el archivo de texto y lee las palabras con la codificacion que requiera
    with open('diccionario.txt', 'r', encoding='utf-8') as f:
        diccionario = [line.strip() for line in f]
    palabras_posibles = [palabra for palabra in diccionario if subcadena in palabra and palabra not in palabras_devueltas]
    if palabras_posibles:
        palabra_elegida = random.choice(palabras_posibles)
        palabras_devueltas.append(palabra_elegida)
        return palabra_elegida
    else:
        return "No se encontraron más palabras con " + subcadena


# Codigo---------------------------------------------
print("BoomPartyUwU by PetaZ")

options = Options()
driver = webdriver.Chrome(options=options)

driver.get("https://jklm.fun")


mode = 0
sec = 0
print("1: modo instantaneo, 2: modo realista")
while (mode != 1.0 and mode != 2.0):
    mode = float(input("Introduce el modo: "))
    if (mode == 2):
        sec = float(input("Segundos entre teclas (rec 0.05) : "))



print("para cerrar Control + C en la terminal")
input("Entra en la sala y dale Enter")


time.sleep(1)
print("Activo")


iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src*='bombparty']")
driver.switch_to.frame(iframe)  


while True:

    round_div = driver.find_element(By.CLASS_NAME, "round") # Cuando round no tenga hidden empieza

    while (round_div.get_attribute("hidden") == None):

        self_turn_div = driver.find_element(By.CLASS_NAME, "selfTurn") # Cuando selfTurn no tenga hidden nos toca
        
        if self_turn_div.get_attribute("hidden") == None:
            # Obtener el texto 
            syllable_div = driver.find_element(By.CLASS_NAME, "syllable") 
            syllable_text = syllable_div.text.strip()

            # Encontrar el input dentro de selfTurn 
            input_box = self_turn_div.find_element(By.TAG_NAME, "input")

            word = arreglarWord(DevPalabra(syllable_text)) # Obtener la palabra del diccionario

            if (mode == 1):
                input_box.send_keys(word + Keys.ENTER)
            else:
                time.sleep(sec*2)
                for letra in word:
                    input_box.send_keys(letra)
                    time.sleep(sec*random.randint(1, 2))
                input_box.send_keys(Keys.ENTER)
            

            print(syllable_text + " -> " + word)
            break


    time.sleep(0.1)

