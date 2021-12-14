import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
listner =sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices") # to change voice to female
engine.setProperty("voice",voices[1].id)
'''engine.say("i am your alexa")
engine.say("what can i do for you")
engine.runAndWait()'''
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listning ....")
            voice=listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                #print(command)
    except:
        pass
    return command
def run_alexa():
    command=take_command()
    print(command)
    if "play" in command:
        song=command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p ")
        print(time)
        talk("current time is" + time)
    elif "day" in command:
        now=datetime.datetime.now()
        weekday=now.strftime("%A")
        print(weekday)
        talk("today is"+weekday)
    elif "what is" in command:
        person = command.replace("what is", "")
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif "date" in  command:
        talk("sorry i am having a headache")
    elif "are you single" in command:
        talk("i am in a relationship with wifi ")
    elif "headline" in command:
        responce = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2021-11-13&sortBy=publishedAt&apiKey=097575c06ecd4bc4b550fae79a2bd131")
        print(type(responce.json()))
        print(responce.json())
        talk(responce.json())
    elif "joke" in command:
        info = (pyjokes.get_joke())
        print(info)
        talk(info)
    elif "shut up" in command:
        talk("weather you are a boy or girl")
        command=take_command()
        if "boy" in command:
            talk("you son of a bitch, dont talk with me again")
        elif "girl" in command:
            talk("you are a beautiful bitch")
    elif "exit" in command:
        talk("i am going to sleep, press the button to wake me up again bye bye")
        quit()
    else:
        talk("i didnt get it")
while True:
    run_alexa()