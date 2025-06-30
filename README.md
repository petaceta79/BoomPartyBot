# 💣 BoomPartyUwU - Bot para JKLM.fun (BombParty)

Este es un bot automatizado para jugar al juego [BombParty](https://jklm.fun/) en la plataforma JKLM.fun. Utiliza Selenium para interactuar con la página web, identificando las sílabas requeridas y escribiendo automáticamente palabras que las contienen, usando un diccionario personalizado.

Se puede utilizar para ganar partidas haciéndote pasar por humano o para ponerlo en modo instantáneo como rival y jugar tú solo.

---

## 🚀 Características

- Se conecta automáticamente a una sala de BombParty en JKLM.fun.
- Detecta cuándo es tu turno y escribe una palabra válida que contiene la sílaba dada.
- Soporta dos modos:
  - **Modo instantáneo**: escribe la palabra de forma inmediata.
  - **Modo realista**: escribe la palabra letra por letra con una pausa configurable, simulando un humano.

## 📦 Requisitos

- Python 3.x
- Google Chrome
- [Chromedriver](https://chromedriver.chromium.org/downloads) compatible con tu versión de Chrome
- Selenium

Instalación de dependencias:

```bash
pip install selenium
```

## 📁 Estructura  
Asegúrate de tener un archivo llamado `diccionario.txt` en el mismo directorio que el script. Este archivo debe contener **una palabra por línea (en minúsculas)**, tal como aqui [diccionario.txt](diccionario.txt), que el bot usará para buscar coincidencias.

## 🕹️ Uso

1. Abre una terminal y ejecuta el script:

   ```bash
   python boomparty.py
   ```
Asegúrate de haber instalado las dependencias necesarias antes de ejecutar el script.

Selecciona el modo de juego:

- `1` para modo instantáneo  
- `2` para modo realista (te pedirá los segundos entre cada tecla)

Entra manualmente en una sala de BombParty en [https://jklm.fun/](https://jklm.fun/), luego vuelve a la terminal y presiona **Enter**.

El bot comenzará a funcionar automáticamente cuando inicie tu turno.
