import speech_recognition as sr
import pyttsx3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import time

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the name of the voice assistant
assistant_name = "TREX"

# Spotify credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
redirect_uri = "YOUR_REDIRECT_URI"

# Create a Spotify client instance
scope = "user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

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
    elif "exit" in query:
        speak("Goodbye!")
        exit()
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
    elif "what is your name" in query:
        speak(f"I am {assistant_name}. How can I assist you?")
    elif "play song" in query:
        speak("Sure, what song would you like to listen to?")
        song_query = listen()
        if song_query:
            search_results = sp.search(q=song_query, limit=1, type="track")
            if search_results and search_results["tracks"]["items"]:
                track_uri = search_results["tracks"]["items"][0]["uri"]
                sp.start_playback(uris=[track_uri])
                speak(f"Now playing {song_query} on Spotify.")
            else:
                speak("Sorry, I couldn't find the requested song on Spotify.")
        else:
            speak("I'm sorry, I didn't catch the song name. Could you please repeat?")
    elif "pause" in query:
        sp.pause_playback()
        speak("Playback paused.")
    elif "resume" in query:
        sp.start_playback()
        speak("Playback resumed.")
    elif "next" in query:
        sp.next_track()
        speak("Playing next track.")
    elif "previous" in query:
        sp.previous_track()
        speak("Playing previous track.")
    else:
        time.sleep(1)  # Delay before asking for clarification
        speak("I'm sorry, I didn't understand your command. Could you please repeat or provide more information?")

# Main loop
time.sleep(1)
while True:
    query = listen().lower()
    process_query(query)
