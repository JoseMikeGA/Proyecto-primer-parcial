import speech_recognition as sr
import RPi.GPIO as GPIO
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

in1 = 24
in2 = 23
en = 25
temp1=1 

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(in1, GPIO.LOW)
GPIO.setup(in2, GPIO.LOW)
p=GPIO.PWM(en,1000)

p.start(25)

r = sr.Recognizer()
speech = sr.Microphone(device_index=0)


def record_audio(ask = False):
    with speech as source:
        if ask:
            linx_speak(ask)
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = " "
        try:
            voice_data = r.recognize_google(audio, language = 'es-MX')
            print(voice_data)

        except sr.UnknownValueError:
            linx_speak("Disculpa, no entendi lo que me dijiste")

        except sr.RequestError as e:
            linx_speak("Disculpa, mi servidor se ah caido; {0}".format(e))
        return voice_data

def linx_speak(audio_string):
    tts = gTTS(text = audio_string, lang="es")
    r = random.randint(1, 20000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    
    if "hora" in voice_data:
        linx_speak(ctime())
    
    if "luz" in voice_data:
        linx_speak("led encendido")
        GPIO.output(17, True)
    
    if "no" in voice_data:
        linx_speak("led apagado")
        GPIO.output(17, False)
    
    if "girar" in voice_data:
        linx_speak("Girar motor")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
    
    if "alto" in voice_data:
        linx_speak("Parar motor")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

    if "salir" in voice_data:
        linx_speak("Hasta la vista baby")
        exit() 

        
time.sleep(1)
linx_speak("Hola, que te gustaria hacer")
while 1:
    voice_data = record_audio()
    respond(voice_data)