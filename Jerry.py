import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
##print(voices)
engine.setProperty("voice",voices[1].id)  #size of 'voices' list is 3, that is we have 3 types of voices only
                                          #hence indexing is 0,1,2

def talk(text):
    engine.say(text)
    engine.runAndWait()
    

##engine.say("I am your jerry")
##engine.say("What can I do for you")
##engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice) #using google speech recognition api - gives text
            command = command.lower()
            if 'jerry' in command:
    ##            engine.say(command)
    ##            engine.runAndWait()
                command = command.replace("jerry","")
                print(command)                
##                talk(command)
        
                
    except:
##        print("Sorry")
##        talk("Sorry jerry")
        talk("Sorry alexa".replace("alexa",""))    
        pass
    return command    

def run_jerry():
    command = take_command()
    if "play" in command:
        song = command.replace("play","")
        talk("playing" + song)
        print("playing" + song)
##        print(song)
        pywhatkit.playonyt(song)
    elif "time" in command:
##        time = datetime.datetime.now().strftime("%H: %M: %S")
        time = datetime.datetime.now().strftime("%I: %M: %S %p")
        print(time)
##        timelist = time.split(": ")
##        print(timelist)
        talk("Current time is " + time)
##        talk("Current time is " + str(int(time[0:2])) + "hours" +
##             str(int(time[4:6])) + "minutes" +
##             str(int(time[8:10])) + "seconds")
    elif "search" in command:
        searchthis = command.replace("search","")
        pywhatkit.search(searchthis)
    elif "date" in command:
        talk("Sorry! I have a headache")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "say" in command:
        say = command.replace("say","")
        talk(say)
    elif "stop" in command:
        print("Thank you dear!")
        talk("Thank you dear!")
        exit()
    else:
        talk("Please say the command again!")
        
while True:
    run_jerry()
##else:
##    talk("Thank you dear!")
