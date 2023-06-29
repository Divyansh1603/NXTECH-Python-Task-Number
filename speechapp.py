import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import openai

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
openai.api_key = "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"

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
        speak("Sure, which location do you want to find?")
        location_query = listen()
        if location_query:
            url = "https://www.google.com/maps/search/" + location_query.replace(" ", "+")
            webbrowser.open(url)
    elif "what is your name" in query:
        speak(f"I am {assistant_name}. How can I assist you?")
    elif "solve problem" in query:
        speak("Sure, please provide the problem statement or question.")
        problem = listen()
        if problem:
            response = solve_problem(problem)
            speak(response)
    else:
        time.sleep(1)  # Delay before asking for clarification
        speak("I'm sorry, I didn't understand your command. Could you please repeat or provide more information?")

def solve_problem(problem):
    # Generate a solution using ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=problem,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0,
        timeout=15,
    )
    solution = response.choices[0].text.strip()
    return solution

# Main loop
time.sleep(1)
while True:
    query = listen().lower()
    process_query(query)
