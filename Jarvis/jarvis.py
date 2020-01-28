import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import smtplib
import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!!")
        print("Good Morning Boss!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!!")
        print("Good Afternoon Boss!!")
    else:
        speak("Good Evening Boss!!")
        print("Good Evening Boss!!")


def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("How can I help you")
        speak("How can I help you")
        r.pause_threshold=1
        r.energy_threshold=200
        r.adjust_for_ambient_noise(source, duration=0.5)       
        audio=r.listen(source)

    try:
        print("Recognizing....")       
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Please Boss Say that again")
        speak("Please Boss Say that again")
        return "None"        
        
    return query


def sendMail(to, Content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("jiveshfav.gohan@gmail.com","jivesh13singh13")
    server.sendmail("jiveshfav.gohan@gmail.com",to, Content)
    server.close()


if __name__ == "__main__":
    wishMe()
    i=True
    while i==True:
        query = takecommand().lower()

        if "jarvis open google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss, The time is {time}")

        elif "fifa" in query:
            speak("Boss,Opening Fifa")
            Path = "E:\\FIFA14MW\\Game\\fifa14-3dm.exe"
            os.startfile(Path)
            
        elif "send an email" in query:
            try:
                speak("What Should I say Boss?")
                Content = takecommand()
                to = "abhi752476@gmail.com"
                sendMail(to, Content)
                speak("Email Sent!!")

            except Exception:
                print(Exception)
                print("Sorry Boss, Unable to sent ")

        elif "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "play song" in query:
            speak("Playing Song in youtube")
            webbrowser.open("youtube.com/watch?v=hmJLDo8nhP4")

        elif "sleep" in query:
            speak("Thank You")
            i=False

        elif "wait" in query:
            speak("Take your time")
