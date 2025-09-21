import speech_recognition as sr
import pyttsx3 
import webbrowser
import musiclibrary
import openai

openai.api_key = "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"    

recognizer = sr.Recognizer() #first we have created a recognizer object where whatever we speak it will recognize
ttsx = pyttsx3.init() #always use parathesis and then we initializepyttsx

def speak (text):
    ttsx.say(text)
    ttsx.runAndWait()


def process_command(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open ("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open ("https://facebook.com")

    elif "open linkedin" in c.lower():
        webbrowser.open ("https://linkedin.com")

    elif "open youtube" in c.lower():
        webbrowser.open ("https://youtube.com")

    elif c.lower().startswith ("play"):
        song = c.lower().split(" ") [1]
        link = musiclibrary.music[song] # we will always use brackets to get access to dictionary
        webbrowser.open(link)


speak("initializing")
while True:

    print ("recognizing") # whatever we are printing in a particular block it works for it only

    try:
        with sr.Microphone() as source:
            print("listening")
            audio = recognizer.listen(source) # by using using timeout it will listen only for 2 times only

        command= recognizer.recognize_google(audio) #this is command as well #recognizer.recognize convert the audio into text
        if (command.lower()=="jarvis"):
            print (f"You said {command}")
            speak ("ya anil")
            try:
                with sr.Microphone() as source:
                    print("active")
                    audio = recognizer.listen(source)
                    command= recognizer.recognize_google(audio)
                    process_command(command)

            except Exception as e:
                print (f"an error occured {e}")
            #listen for wake command
    except Exception as e: # we changed the unknown value error to exception because it will handle all kind of errors not unknownevlaue error
        print("error; {0}".format(e))

  



    






