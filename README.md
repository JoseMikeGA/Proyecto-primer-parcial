# Asistente virtual

#### Poyecto Realizado por: Palma Morales Fatima Daniela Margarita y Gómez Acosta José Miguel

Este proyecto muestra el uso de SpeechRecognition 3.8.1 para crear un asistente virtual utilizando el lenguaje Python e implementandolo en una Raspberry Pi 3 para el control de motor y LED.
Para este proyecto utilizamos el **IDE Visual Studio Code** , dentro del cual creamos un entorno virtual con Python, ademas  de la instalacion de multiples librerias. 
Para la parte del Hardware se utilizo una Raspberry Pi 3, a la cual se le conectaron un LED y un modulo L298N para el control del motor. **Todo se realizo dentro de la Raspberry Pi**.

## Entorno virtual

Para este proyecto se ocupo generar un entorno virtual con Python en la carpeta donde se va a trabajar. Para crear nuestro entorno virtual debemos ingresar los siguientes comandos en la terminal.

```
python3 -m venv venv
source venv/bin/activate
```

Despues de generar el entorno virtual debera aparecer la palabra **(venv)** a lado de la direccion donde estamos trabajando, por ejemplo:

```(venv) C:\Users\Miguel Gomez\Document\Programacion avanzada\Proyecto Primer Parcial>```

Ya por ultimo, para tener nuestro entorno virtual listo, seleccionamos el interprete de python con nuestro entorno virtual **venv**.


## Librerias 

Para este proyecto se necesito de instalar las siguientes librerias dentro del entorno virtual, cabe destacar que para que la instalacion se efectue dentro del entorno virtual, estas deben de hacerse con el comando 
**pip**.

```
pip install speechrecognition
pip install pyttsx3
pip install pyaudio
pip install playsound
pip install PyObjC
pip install gTTS
pip install RPi.GPIO
pip install vext
pip install vext.gi
sudo apt-get install -y flac
sudo apt-get install alsa-tools alsa-utils 
sudo apt-get install gstreamer-1.0
```


## Programas

El codigo de ```linx_assistant.py```  
