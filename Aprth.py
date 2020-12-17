"""

    + Afrikaans af
    + Basque eu
    + Bulgarian bg
    + Catalan ca
    + Arabic (Egypt) ar-EG
    +? Arabic (Jordan) ar-JO
    + Arabic (Kuwait) ar-KW
    +? Arabic (Lebanon) ar-LB
    + Arabic (Qatar) ar-QA
    + Arabic (UAE) ar-AE
    .+ Arabic (Morocco) ar-MA
    .+ Arabic (Iraq) ar-IQ
    .+ Arabic (Algeria) ar-DZ
    .+ Arabic (Bahrain) ar-BH
    .+ Arabic (Lybia) ar-LY
    .+ Arabic (Oman) ar-OM
    .+ Arabic (Saudi Arabia) ar-SA
    .+ Arabic (Tunisia) ar-TN
    .+ Arabic (Yemen) ar-YE
    + Czech cs
    + Dutch nl-NL
    + English (Australia) en-AU
    +? English (Canada) en-CA
    + English (India) en-IN
    + English (New Zealand) en-NZ
    + English (South Africa) en-ZA
    + English(UK) en-GB
    + English(US) en-US
    + Finnish fi
    + French fr-FR
    + Galician gl
    + German de-DE
    + Hebrew he
    + Hungarian hu
    + Icelandic is
    + Italian it-IT
    + Indonesian id
    + Japanese ja
    + Korean ko
    + Latin la
    + Mandarin Chinese zh-CN
    + Traditional Taiwan zh-TW
    +? Simplified China zh-CN ?
    + Simplified Hong Kong zh-HK
    + Yue Chinese (Traditional Hong Kong) zh-yue
    + Malaysian ms-MY
    + Norwegian no-NO
    + Polish pl
    +? Pig Latin xx-piglatin
    + Portuguese pt-PT
    .+ Portuguese (brasil) pt-BR
    + Romanian ro-RO
    + Russian ru
    + Serbian sr-SP
    + Slovak sk
    + Spanish (Argentina) es-AR
    + Spanish(Bolivia) es-BO
    +? Spanish( Chile) es-CL
    +? Spanish (Colombia) es-CO
    +? Spanish(Costa Rica) es-CR
    + Spanish(Dominican Republic) es-DO
    + Spanish(Ecuador) es-EC
    + Spanish(El Salvador) es-SV
    + Spanish(Guatemala) es-GT
    + Spanish(Honduras) es-HN
    + Spanish(Mexico) es-MX
    + Spanish(Nicaragua) es-NI
    + Spanish(Panama) es-PA
    + Spanish(Paraguay) es-PY
    + Spanish(Peru) es-PE
    + Spanish(Puerto Rico) es-PR
    + Spanish(Spain) es-ES
    + Spanish(US) es-US
    + Spanish(Uruguay) es-UY
    + Spanish(Venezuela) es-VE
    + Swedish sv-SE
    + Turkish tr
    + Zulu zu

"""
# https://www.lfd.uci.edu/~gohlke/pythonlibs/
# "start \"\" https://www.{0}.com/search?q={1}&source=lnms&tbm=nws"
# os.system('start \"\" https://www.'+a[0]+'.com/')
# https://codescracker.com/python/program/python-program-shutdown-restart-computer.htm
# https://cloud.google.com/speech-to-text/docs/languages

import pyttsx3
import os
import smtplib
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = datetime.datetime.now().hour
    if 0<=hour<12:
        speak("Good Morning, Sir")
    elif  12<=hour<18:
        speak("Good Afternoon, Sir")
    else:
        speak("Good Evening, Sir")
    speak("Hi Sir, I'm Aprth, How can I help you?")

"""def message(text):
    text = takecommand(
        if text in ['hello','hi','gm','good morning']:
            return speak(response[text][random.randint(0,len(response[text]))])
        else:
            return speak(response[text])
    else:
        return speak(response["default"])

def bot():
    x = True
    while x:
        # text = input("USER: ").lower()
        if text in ['goodbye','bye','ta..ta..','bye bye','good bye','tata']:
            x = False
            return 'Bot: Good Bye!'
        else:
            x = True
            print("Bot: ",message(text))
"""
def takecommand():
    #take commmad from microphones and returns string
    r = sr.Recognizer()
    # if text in response:
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 0.8
        r.energy_threshold = 800
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="gu-in")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Can't get it, Can you be specific ?")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('patelparth20005@gmail.com','Parth2000')
    server.sendmail('patelparth20005@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    WishMe()
    flag = True
    while flag:
        query = takecommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia",'')
            answer = wikipedia.summary(query,sentences=3)
            speak("According to My Data...")
            print(answer)
            speak(answer)

        if "who is" in query:
            speak("Searching Wikipedia...")
            query = query.replace("who is",'')
            answer = wikipedia.summary(query,sentences=3)
            speak("According to My Data...")
            print(answer)
            speak(answer)

        if "tell me about" in query:
            speak("Searching Wikipedia...")
            query = query.replace("tell me about",'')
            answer = wikipedia.summary(query,sentences=3)
            speak("According to My Data...")
            print(answer)
            speak(answer)

        if 'open' in query:
            query = query.replace('open ','')
            webbrowser.open(query+".com")
            # os.system('start \"\" https://www.' + query + '.com/')

        if 'search google' in query:
            query = query.replace('search google ','')
            os.system(f"start \"\" https://www.google.com/search?q={query}&source=lnms&tbm=nws")

        if 'google' in query:
            query = query.replace('google ','')
            os.system(f"start \"\" https://www.google.com/search?q={query}&source=lnms&tbm=nws")

        if 'youtube' in query:
            query = query.replace('youtube ','')
            os.system(f"start \"\" https://www.youtube.com/results?search_query={query}")
        #     https://www.youtube.com/results?search_query=

        if 'say about' in query:
            query = query.replace('say about ','')
            webbrowser.open(query+".com")

        # in working condition...
        """
        if 'about' in query:
            query = query.replace('about ','').split()
            print(query)
            sleep(2)
            os.system("start \"\" https://www.google.com/search?q={0}&source=lnms&tbm=nws".format(query))
        """
        # still in progress
        if 'play music' in query:
            music_dir = "path"
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,song[0]))

        if 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir, The Time is {strtime}")

        if 'show me powerpoint' in query:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path)

        if 'show me firefox' in query:
            path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(path)

        if 'show me movie' in query:
            path = "C:\\movies\\the secret 2006 hindi dubbed [720p].mp4"
            os.startfile(path)

        # less secured app : ON (should be OFF )
        if 'email to' in query:
            try:
                speak("Which Message sir...")
                print("Which Message,sir ?")
                content = takecommand()
                to = 'patelaprth20005@gmail.com'
                to1 = 'aanalshah2001@gmail.com'
                to2 = 'jayjain33633434@gmail.com'
                to3 = 'dakshay4307@gmail.com'
                to4 = 'kalindiAdhiya241@gmail.com'
                to5 = 'yashpatel200021@gmail.com'
                to6 = 'parin.patel2003@gmail.com'
                to7 = 'merakesh1974@gmail.com'
                sendEmail(to, f'Aprth; {content}')
                # sendEmail(to1,f'Aanal; {content}')
                # sendEmail(to2,f'Jay; {content}')
                # sendEmail(to3,f'Dakshay; {content}')
                # sendEmail(to4,f'Kalindi; {content}')
                # sendEmail(to5,f'Yash; {content}')
                # sendEmail(to6,f'Parin; {content}')
                # sendEmail(to7,f'Papa; {content}')
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry! I can't able to do.")

        if 'goodbye' in query:
            speak("Goodbye Sir, Nice to talk you, meet you soon!")
            flag = False
