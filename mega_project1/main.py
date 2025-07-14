import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
from openai import OpenAI
# from gtts import gTTS
# import pygame

recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api = "fa246aea55354349938ba602c93869bc"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak_new(text):
#     tts = gTTS(text)
#     tts.save("temp.mp3")

#     pygame.mixer.init()

#     pygame.mixer.music.load("temp.mp3")

#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

def aiprocess(command):
        
    client = OpenAI(
        api_key="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",
    )

    completion =client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud. give short responses please."
            },
            {
                "role": "user",
                "content": command
            }
            ]

    )

    return completion.choices[0].message.content

def process_command(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c.lower():
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")

        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])

    else:
        #let OpenAI handle the request
        output = aiprocess(c)
        speak(output)




if __name__ == "__main__":
    speak("Initializing jarvis...")

    while True:
        #listen for the wake word "jarvis"
        #obtain audio from the microphone

        r = sr.Recognizer()
        

        print("Recognizing...")
      

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("ya")

                #listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command)

        except Exception as e:
            print("Error; {0}".format(e))

