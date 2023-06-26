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
engine.setProperty('rate', 150)


#engine start
engine.say("Hello sir! I'm Javiar. You can call me anytime by saying 'computer'!")
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
            if text3=="Yes" or text3=="yes": 
                webbrowser.open(cautarenet)
            else:
                engine.say("OK. Leaving the internet...")
                engine.runAndWait()
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

comenzi=["who are you", "who made you", "how are you", "Wikipedia", "internet", "display date", "display time", "shut down", "news"]

chemare=["computer", "shut down", "sleep", "", " ", "shut down "]

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

            if chem=="computer":

                aux=True

                engine.say("How may I assist you today?")
                engine.runAndWait()

                voce()

                if text=="who are you":
                    engine.say("i'm Javiar, your personal virtual assistant, version 0 point 3 point 6. I can automate your workflow while you spend more time doing what you love!")
                    engine.runAndWait()

                if text=="who made you":
                    engine.say("My creator is a young student who loves coding!")
                    engine.runAndWait()
            
                if text=="how are you":
                    engine.say("I'm fine sir. Waiting for your command. Call me anytime you need something!")
                    engine.runAndWait()

                if text=="Wikipedia": 
                    cautarefc()
                    
                if text=="internet":
                    internet()

                if text=="news":
                    googlenews()

                if text=="display date":
                    print(date.today())
                    engine.say("Today's date is " + str(date.today()))
                    engine.runAndWait()

                if text=="display time":
                    print(time.strftime("%H %M %S"))
                    engine.say("It's " + time.strftime("%H, %M, %S"))
                    engine.runAndWait()

                if text=="shut down" or text=="sleep":
                    break

                if text not in comenzi:
                    engine.say("Sorry I don't understand!")
                    engine.runAndWait()
                    voce()
            
            if chem=="shut down" or chem=="sleep" or chem=="shut down ":
                break

            if chem not in chemare:
                engine.say("Sorry to interupt you sir. Call me anytime you need my help.")
                engine.runAndWait()
            
    except speech_recognition.UnknownValueError:
        engine.say("Sorry! I don't understand. Call me anytime!")
        engine.runAndWait()