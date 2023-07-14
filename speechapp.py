import speech_recognition as sr
import pyttsx3
import webbrowser
import time

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the name of the voice assistant
assistant_name = "TREX"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble recognizing your speech. Please try again later.")
        return ""

def process_query(query):
    if "hello" in query:
        speak(f"Hello! How can I assist you, {assistant_name} speaking?")
    elif "what is your name" in query:
        speak(f"I am {assistant_name}. How can I assist you?")
    elif "search" in query:
        speak("What can I search for you?")
        search_query = listen()
        if search_query:
            search_url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
            webbrowser.open(search_url)
    elif "find location" in query:
        while True:
            speak("Sure, which location do you want to find?")
            location_query = listen()
            if location_query:
                url = "https://www.google.com/maps/search/" + location_query.replace(" ", "+")
                webbrowser.open(url)
                break
            else:
                speak("I'm sorry, I didn't get that. Could you please repeat the location?")
    elif "play song" in query:
        speak("Sure, what song would you like to listen to?")
        song_query = listen()
        if song_query:
            spotify_search_url = f"https://open.spotify.com/search/{song_query.replace(' ', '%20')}"
            webbrowser.open(spotify_search_url)
            speak("I've opened Spotify for you. Please select and play the song manually.")
        else:
            speak("I'm sorry, I didn't catch the song name. Could you please repeat?")
    elif "exit" in query:
        speak("Goodbye!")
        exit()
    else:
        time.sleep(1)  # Delay before asking for clarification
        speak("I'm sorry, I didn't understand your command.")

# Main loop
time.sleep(1)
while True:
    query = listen().lower()
    process_query(query)
