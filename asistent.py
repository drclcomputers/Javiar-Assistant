#modules, apis, etc
import pyttsx3
import speech_recognition
import wikipedia
from datetime import date
import time
import webbrowser
from playsound import playsound
import requests
from bs4 import BeautifulSoup
import random
import json

#json voice stuff
f=open("setari.json", "r")
data=json.load(f)
voicenr=data['voice']
ratenr=data['rate']
volum=data['volume']
name=data['name']


#bbc database connect
url="https://www.bbc.com/news"
response=requests.get(url)
test=" "
y=0


#voice
text=" "
recognizer=speech_recognition.Recognizer()


#engine initialising
engine=pyttsx3.init()
engine.setProperty('rate', ratenr)
voices=engine.getProperty('voices')
engine.setProperty('volume', volum)
engine.setProperty('voice', voices[voicenr].id)


#engine start
engine.say("Hello sir! I'm " + name + ". You can call me anytime by saying 'computer'!")
engine.runAndWait()


#wikipedia api
def cautarefc():
    global text1, text, audio
    engine.say("What do you want me to search sir?")
    engine.runAndWait()
    playsound("sunet2.mp3")
    audio=recognizer.listen(mic, phrase_time_limit=5)
    cautare=recognizer.recognize_google(audio, language="en")
    cautare.lower()
    print("Cautare: " + cautare)
    engine.say(wikipedia.search(cautare))
    engine.runAndWait()
    print(wikipedia.search(cautare))
    engine.say("Please specify the exact article you want to acces sir!")
    engine.runAndWait()

    #wikipedia error
    def invalid():
        engine.say("Sorry! I didn't understand. Here are some potential articles you may be interested in: " + wikipedia.search(cautare))
        engine.runAndWait()
        engine.say("Please provide the article name. ")
        engine.runAndWait()

    #wikipedia article
    def verificare():
        global text1
        try:
            with speech_recognition.Microphone() as mic:
                playsound("sunet2.mp3")
                audio=recognizer.listen(mic, phrase_time_limit=3)
                text1=recognizer.recognize_google(audio, language="en")
                text1.lower()
                if wikipedia.exceptions==True:
                    invalid()
                    verificare()
                else:
                    engine.say(wikipedia.summary(text1, sentences=3))
                    engine.runAndWait()
        except speech_recognition.UnknownValueError:
            invalid()
            verificare()
    verificare()


#browsing the internet
def internet():
    try:
        with speech_recognition.Microphone() as mic:
            engine.say("What do you want me to search sir?")
            engine.runAndWait()
            playsound("sunet2.mp3")
            audio=recognizer.listen(mic, phrase_time_limit=5)
            cautarenet=recognizer.recognize_google(audio, language="en")
            cautarenet.lower()
            print("Cautare net: " + cautarenet)
            cautarenet=cautarenet+".com"
            engine.say("I have found the following website : " + cautarenet)
            engine.runAndWait()
            engine.say("Do you want me to open it sir?")
            engine.runAndWait()
            playsound("sunet2.mp3")
            audio=recognizer.listen(mic, phrase_time_limit=3)
            text3=recognizer.recognize_google(audio, language="en")
            text3.lower()
            for word in afirmativ:
                if word in text3:
                    webbrowser.open(cautarenet)
                    break
                else:
                    engine.say("OK. Leaving the internet...")
                    engine.runAndWait()
                    break
    except speech_recognition.UnknownValueError:
        engine.say("Sorry I don't understand!")
        engine.runAndWait()
        internet()


#news search                      
def googlenews():
    global y, test
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    for x in headlines:
        y+=1
        if y<=7 and not test==x:
            engine.say(x.text.strip())
            engine.runAndWait()
            test=x

#speaking
def voce():
    global text, audio
    playsound("sunet2.mp3")
    audio=recognizer.listen(mic, phrase_time_limit=5)
    text=recognizer.recognize_google(audio, language="en")
    text.lower()
    print(text)

#joke
def gluma():
    a=random.randint(1, 10)
    print(a)
    match a:
        case 1:
            engine.say("I'm afraid for the calendar. Its days are numbered.")
            engine.runAndWait()
            playsound("gluma.mp3")

        case 2:
            engine.say("What do you call a factory that makes okay products? A satisfactory.")
            engine.runAndWait()
            playsound("gluma.mp3")
        
        case 3:
            engine.say("Dear Math, grow up and solve your own problems.")
            engine.runAndWait()
            playsound("gluma.mp3")

        case 4:
            engine.say("Have you heard about the chocolate record player? It sounds pretty sweet.")
            engine.runAndWait()
            playsound("gluma.mp3")

        case 5:
            engine.say("What did the ocean say to the beach? Nothing, it just waved.")
            engine.runAndWait()
            playsound("gluma.mp3")

        case 6:
            engine.say("What did one wall say to the other? I'll meet you at the corner.")
            engine.runAndWait()
            playsound("gluma.mp3")

        case 7:
            engine.say("What did the zero say to the eight? That belt looks good on you.")
            engine.runAndWait()
            playsound("gluma.mp3")

        case 8:
            engine.say("I asked my dog what's two minus two. He said nothing.")
            engine.runAndWait()
            playsound("gluma.mp3")

        case 9:
            engine.say("I don't trust those trees. They seem kind of shady.")
            engine.runAndWait()
            playsound("gluma.mp3")
    
        case 10:
            engine.say("I don't trust stairs. They're always up to something.")
            engine.runAndWait()
            playsound("gluma.mp3")


#List of vocal commands

creare=["creator", "made", "creation", "maker"]

cunoastere=["who are you", "purpose", "what are you"]

conversatie=["how are you", "what are you doing", "how is life"]

om_trist=["sad", "angry", "not in mood", "cry", "yell", "divorc"]

om_happy=["fine", "good", "happy"]

afirmativ=["yes", "Yes", "Go ahead", "go ahead", "Affirmative", "affirmative"]

joke=["joke", "something funny", "laugh"]

clock=["time", "clock", "hour", "minutes"]

day=["date", "day", "month", "year"]

comenzi=["shut down"]+ cunoastere, conversatie, om_happy, om_trist, afirmativ, joke, clock, day

chemare=["computer", "computers"]

inchidere=["shut down", "sleep", "goodbye", "leave", "go away", "you are fired"]


#assitant root
while True:
    try:
        with speech_recognition.Microphone() as mic:
            aux=False
            playsound("sunet2.mp3")
            audio=recognizer.listen(mic, phrase_time_limit=6)
            chem=recognizer.recognize_google(audio, language="en")
            chem.lower()
            print(chem)

            if chem in chemare:

                aux=True
                alfa=False

                engine.say("How may I assist you today?")
                engine.runAndWait()

                voce()

                for word in cunoastere:
                    alfa=True
                    if word in text:
                        engine.say("i'm Javiar, your personal virtual assistant, version 0 point 5 point 2. I can automate your workflow while you spend more time doing what you love!")
                        engine.runAndWait()
                        break

                for word in creare:
                    alfa=True
                    if word in text:
                        engine.say("My creator is a young student who loves coding!")
                        engine.runAndWait()
                        break
            
                for word in conversatie:
                    alfa=True
                    aux=False
                    if word in text:
                        engine.say("I'm fine sir. What are you doing in this fine day?")
                        engine.runAndWait()
                        voce()
                        for sentiment in om_trist:
                            if sentiment in text:
                                aux=True
                                engine.say("I'm sorry sir. I'll do my best to cheer you up. Do you want to hear a joke?")
                                engine.runAndWait()
                                voce()
                                for aff in afirmativ:
                                    if aff in text:
                                        gluma()
                                        engine.say("I hope I cheered you up just a little bit sir. Call me anytime you need something!")
                                        engine.runAndWait()
                                        break
                                    else:
                                        engine.say("Ok sir. I'll leave. Call me anytime you need something!")
                                        engine.runAndWait()
                                        break
                        for sentiment in om_happy:
                            if sentiment in text:
                                aux=True
                                engine.say("I'm glad sir. Do you want to hear a joke?")
                                engine.runAndWait()
                                voce()
                                for aff in afirmativ:
                                    if aff in text:
                                        gluma()
                                        engine.say("I hope i made your day better sir. Call me anytime you need something!")
                                        engine.runAndWait()
                                        break
                                    else:
                                        engine.say("Ok sir. I'll leave. Call me anytime you need something!")
                                        engine.runAndWait()
                                        break
                        if aux==False:
                            engine.say("Ok sir. I'll leave. Call me anytime you need something!")
                            engine.runAndWait()
                        break

                for word in joke:
                    alfa=True
                    if word in text:
                        engine.say("OK. Here it is.")
                        engine.runAndWait()
                        gluma()
                        break

                if "Wikipedia" in text: 
                    alfa=True
                    cautarefc()
                    
                if "internet" in text:
                    alfa=True
                    internet()

                if "news" in text:
                    alfa=True
                    googlenews()

                for word in day:
                    if word in text:
                        alfa=True
                        print(date.today())
                        data=date.today()
                        zi=data.weekday()
                        match zi:
                            case 0:
                                zi="Monday"
                            case 1:
                                zi="Tuesday"
                            case 2:
                                zi="Wednesday"
                            case 3:
                                zi="Thursday"
                            case 4:
                                zi="Friday"
                            case 5:
                                zi="Saturday"
                            case 6:
                                zi="Sunday"
                        engine.say("Today's date is " + zi + str(data))
                        engine.runAndWait()

                for word in clock:
                    if word in text:
                        alfa=True
                        print(time.strftime("%H %M %S"))
                        engine.say("It's " + time.strftime("%H, %M, %S"))
                        engine.runAndWait()

                if text=="shut down" or text=="sleep":
                    exit()

                if alfa==False:
                    engine.say("Sorry I don't understand!")
                    engine.runAndWait()
            
            if chem in inchidere:
                exit()

            if (chem not in chemare) and (chem not in inchidere):
                engine.say("Sorry to interupt you sir. Call me anytime you need my help.")
                engine.runAndWait()
            
    except speech_recognition.UnknownValueError:
        pass