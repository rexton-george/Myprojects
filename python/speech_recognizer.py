import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=3)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def voice_assistant():
    speak('how can i help you!')
    while True:
        command = listen()

        if "hello" in command:
            speak("Hi there! how can i help you")

        elif "how are you" in command:
            speak("I'm doing well, thank you for asking.")

        elif "r e x t o n" in command:
            speak("Hi Rexton. its greate to hear your voice again. here are the some details i know about you. you are a second year computer science engineering student at n p r college of engineering and technology")

        elif "tell me about npr cet" in command:
            speak("The N P R College of Engineering and Technology is dedicated to extend value-added and contemporary education in the diverse disciplines of Engineering and Technology. Affiliated to the Anna University, the College has been conferred with the ISO 9001: 2008 Certified Institution in its very first year.")

        elif"thank you" in command:
            speak("your welcome.")
            
        elif "bye-bye" in command:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    voice_assistant()
