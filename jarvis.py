import pyttsx3  # type: ignore
import speech_recognition as sr # type: ignore
import datetime
import wikipedia # type: ignore
import webbrowser
import pipwin 




engine = pyttsx3.init('sapi5')#voice lene ke liye sapi5
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir! ")

    else:
        speak("Good evening sir !")

    
speak("I am jarvis Sir ..please tell me how may I help you")

def takeCommand():#microphone take input in user

   r = sr.Recognizer()
   with sr.Microphone() as source:
     print("Listening...")
     r.pause_threshold = 1 # timeing gap for speaking
     audio = r.listen(source)
       
   try:
     print("Recognizing...")
     query = r.recognize_google(audio, language='en-in')
     print(f"User said:{query}\n")


   except Exception as e:
     # print(e)
     print("Say that again please... ")
     return "None"
   return query

#def sendEmail(to,content):



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()#logic for query
        if 'wikipedia' in query:
            speak("Searching Wikipedia.... ")
            query  = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube'in query:
            webbrowser.open("youtube.com")

        elif 'open gooogle'in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")

        elif 'open gooogle'in query:
            webbrowser.open("google.com")
        
        elif 'open classroom'in query:
            webbrowser.open("classroom.google.com")
        
        elif 'chatgpt'in query:
            webbrowser.open("openaicom/chatgpt")
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        #elif 'email to harry'in query:
            #try:
                #speak("What should I say?")
                #content = takeCommand()
                #to ="gauravsharma14042005@gmail.com"
                #speak("Email has been sent!")
            #except Exception as e:
                #print(e)
                #speak("Soory my friend div bhai  i am not able for sent this massage ")
 