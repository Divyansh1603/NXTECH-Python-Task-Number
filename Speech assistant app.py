import speech_recognition as sr 

r=sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data =''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry I didn't get that")
        except sr.RequestError:
            print("Sorry, My speech service is down")
        return voice_data

def respond(voice_data):
    if 'What is your name' in voice_data:
        print('My name is Trex')

print("How can I help you")
voice_data = record_audio()
respond(voice_data)
