import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser


info = ['who are you', 'hello', 'tell me about yourself', 'hey', 'hi', 'what is your name']
stopping = ['goodbye', 'bye', 'stop', 'thank you', 'quit']


def Wiki(command):
    speak('searching wikipedia')
    command = command.replace('wikipedia', '')
    wikiRes = wikipedia.summary(command, sentences= 3)
    speak("According to Wikipedia")
    print(wikiRes)
    speak(wikiRes)


def greet():
    time  = datetime.datetime.now().hour
    if time >= 0 and time < 12:
        speak("Good morning Sir.")
        curTime = 'morning'
    elif time >= 12 and time < 18:
        speak("Good afternoon Sir")
        curTime = 'afternoon'
    else:
        speak('Good evening Sir')
        curTime = 'evening'
    speak("pybot at your service")
    return curTime


def pybot(command):
    if command in info:
        speak("Hello sir, I am Pybot")
        speak("My creator is Shodhan Shetty, and i'm here to assist you.")
    elif command =="how are you":
        speak("I am good. Thank you for asking. Hope you are in a great health too.")
        speak('Dont forget to wear mask and sanitize yourself reguraly.')


def OpenBrowser(command):
    if 'instagram' in command:
        speak("Opening Instagram")
        print("Opening instagram...")
        webbrowser.open('https://www.instagram.com/')
        return speak("Opend Instagram Sucessfully")
    elif 'github' in command:
        speak("Opening Github")
        print("Opening github...")
        webbrowser.open('https://github.com/shodhanshetty14/')
        return speak("Opend Github Sucessfully")
    elif 'youtube' in command:
        speak("Opening Youtube")
        print("Opening youtube...")
        webbrowser.open('https://www.youtube.com/')
        return speak("Opend Youtube Sucessfully")
    elif 'spotify' in  command:
        speak("Opening Spotify")
        print("Opening Spotify...")
        webbrowser.open('https://www.spotify.com/')
        return speak("Opend Spotify Sucessfully")
    return speak("Can you please repeat again?")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def voiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print('Recognizing...')
            q = r.recognize_google(audio, language='en-in')
            # q = r.recognize_sphinx(audio, language='en-in')
            print(f'Your command was: {q}')
            speak(f"Recognised command as {q}")
        except Exception:
            print('Sorry, can you repeat it again?')
            return 'None'
        return q


def PlayMusic():
    pass


def playMovie():
    pass



if __name__ == '__main__':
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    curTime = greet()
    while True:
        command = voiceCommand().lower()
        if command in  info:
            pybot()
        
        if 'wikipedia' in command:
            Wiki(command)
        elif command in stopping:
            speak("It was good speaking with you. GoodBye Sir ")
            exit()
        elif 'open' in command:
            OpenBrowser(command)
        elif command == 'how are you':
            pybot(command)

# Need to complete the PlayMusic & PlayMovie Function and make some change in the structuring