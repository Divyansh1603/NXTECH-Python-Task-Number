import speech_recognition as sr 
import webbrowser
import time
import playsound
import random
import os
from gtts import gTTS
from time import ctime

r=sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            trex_speak(ask)
        audio = r.listen(source)
        voice_data =''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            trex_speak("Sorry I didn't get that")
        except sr.RequestError:
            trex_speak("Sorry, My speech service is down")
        return voice_data
    
def trex_speak(audio_string):
    tts= gTTS(text=audio_string, lang='en')
    r = random.randint(1,100)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if 'what is your name' in voice_data:
        trex_speak('My name is Trex')

    if 'what time is it' in voice_data:
        trex_speak(ctime())

    if 'search' in voice_data:
       search = record_audio('what do you want to search for')
       url = "https://google.com/search?q=" + search
       webbrowser.get().open(url)
       trex_speak('here is what i found for ' + search)

    if 'find location' in voice_data:
       location = record_audio('what is the location?')
       url = "https://google.nl/maps/place/" + location + "/&amp;"
       webbrowser.get().open(url)
       trex_speak('here is the location of ' + location)

    if 'exit' in voice_data:
        exit()
    

time.sleep(1)
trex_speak("How can I help you")
while 1:
    voice_data = record_audio()
    respond(voice_data)

