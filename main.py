import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime


# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice speed
engine.setProperty("rate", 170)


def speak(text):
    """Convert text to speech."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to the user's voice and convert it to text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            print("Recognizing...")
            query = recognizer.recognize_google(audio)

            print("You:", query)
            return query.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand you.")
            return ""

        except sr.RequestError:
            speak("Sorry, there is a problem with the speech recognition service.")
            return ""


def process_command(query):
    """Process the user's voice command."""

    if "hello" in query or "hi" in query:
        speak("Hello! How can I help you?")

    elif "how are you" in query:
        speak("I'm doing great. Thank you for asking!")

    elif "your name" in query:
        speak("I am your Python Voice Assistant.")

    elif "time" in query:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in query or "today" in query:
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif query.startswith("search"):
        search_query = query.replace("search", "", 1).strip()

        if search_query:
            speak(f"Searching the web for {search_query}")
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
        else:
            speak("What would you like me to search for?")

    elif "open google" in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in query or "quit" in query or "goodbye" in query:
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("I don't know that command. I can search the web for you.")
        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

    return True


def main():
    """Start the voice assistant."""

    speak("Hello! I am your voice assistant.")
    speak("You can ask me for the time, date, or search the web.")

    running = True

    while running:
        query = listen()

        if query:
            running = process_command(query)


if __name__ == "__main__":
    main()