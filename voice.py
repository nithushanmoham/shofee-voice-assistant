
import pip
import speech_recognition as sr
import webbrowser
import smtplib
import random
import wikipedia
import datetime
import wolframalpha
import os
import sys
import subprocess
import pyttsx3
import gtts as gt 


engine = pyttsx3.init()

'''len(voices)-1'''
client = wolframalpha.Client(' IL 61820-7237, USA')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('shofee : ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe ():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 10 and currentH < 3:
        speak('Hi Sir,Good Morning! Im your assistant shofee. 3.0 your fine! The time is',currentH)

    elif currentH >= 3 and currentH < 15:
        speak('Hi Sir,Good Afternoon!')

    elif currentH >= 15 and currentH !=19:
        speak('Hi Sir,Good Evening!') 

    elif currentH >= 19 and currentH !=10:
        speak('Good Night sir! It is night')
        speak ('May i help you?')
    else:
        print("finish")
greetMe()

speak('I am your assistant shofee. 3.0 ,How may I help you?')



def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        r.pause_threshold =  0.5
    try:
        query = r.recognize_google(audio).lower()
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! TRY Writing your command Sir')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'hello' in query:
            speak('hello baby')

        elif 'do you want to destroy humans' in query:
            speak('i no is human sir')

        elif 'open gmail' in query:
            speak('okay sir')
            webbrowser.open('www.gmail.com')
            
        elif 'play song' in query:
            speak('okay sir your enjoi the song sir')
            webbrowser.open('yamma.mp3')

        elif 'please open your photo' in query:
            speak('okay sir ')
            webbrowser.open('facescan.gif')

        elif 'what is my gmail addres' in query:
            speak('okay sir your gmail addres')
            speak('nithushan014@gmail.com')
            
        elif 'what is my name' in query:
            speak('your name is Nithushan Mohan')
        
        elif 'what is your name' in query:
            speak('my name is shofee. 3.0')
        
        elif 'vankkam' in query:
            speak('vanakkam')

        elif 'what is your name' in query:
            speak('my name is shofee. 3.0')
            speak('iam no deth')
        
        elif 'what is your age' in query:
            speak('no age sir im computer')

        elif 'what is the 1+1' in query:
            speak('1+1=2 sir')

        elif 'what is the 1+2?' in query:
            speak('1+2=3 sir')

        elif 'what is the 1+3' in query:
            speak('1+3=4 sir')

        elif 'what is the 1+4' in query:
            speak('1+4=5 sir')

        elif 'what is the 1+5' in query:
            speak('1+5=6 sir')

        elif 'what is the 1+6' in query:
            speak('1+6=7 sir')

        elif 'what is the 1+7' in query:
            speak('1+7=8 sir')

        elif 'what is the 1+8' in query:
            speak('1+8=9 sir')

        elif 'what is the 1+9' in query:
            speak('1+9=10 sir')

        elif 'what is the 1+10' in query:
            speak('1+10=11')

        elif 'what is the 10+10-2' in query:
            speak('10+10-2=18 sir')

        elif 'what is the 9+1-8' in query:
            speak('9+1-8=2 sir')

        elif 'what is the 9+0-2' in query:
            speak('9+0-2=7 sir')

        elif 'what is the 3+1-2' in query:
            speak('3+1-2=2 sir')

        elif 'what is the 3+0-2' in query:
            speak('3+0-2=1 sir')

        elif 'shofee i love you' in query:
            speak('sory sir i no love sir')

        elif 'how are you' in query:
            speak('iam fine how are you sir')

        elif 'iam fine' in query:
            speak('okay sir')

        elif 'iam sad' in query:
            speak('what sir?')

        elif 'no iam jest jock' in query:
            speak('okay good jock sir')

        elif 'please open google map' in query:
            speak('okay sir')

        elif 'you ' in query:
            speak('okay sir')

        elif 'open google translate' in query:
            speak('okay sir')

        elif 'please open your photo' in query:
            speak('okay sir opening your photo')
            webbrowser.open('facescan.png')

        elif 'please open my photo' in query:
            speak('okay sir opening my photo')
            webbrowser.open('nithu.jpg')
        
        elif 'how are you' in query:
            speak('im fine sir')

        elif 'who are you' in query:
            speak('im your assistant shofee sir')

        elif 'your favorite food' in query:
            speak('rice sir')
        
        elif 'your favorite frut?' in query:
            speak('apple sir')

        elif 'your favorite song' in query:
            speak('my favorite song is tamil english songs and taml songs sir')

        elif 'father tamil meaning' in query:
            speak('appa')

        elif 'mother tamil meaning' in query:
            speak('amma')

        elif 'movie tamil meaning' in query:
            speak('scenima')

        elif 'speeching abcd' in query:
            speak('okey sir a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,p,w,x,y,z')

        elif 'speeching 123' in query:
            speak('1,2,3,4,5,6,7,8,9,10')

        elif 'what is my passwort' in query:
            speak('okey sir nithuSHAN@321!@#')

        elif 'hi shofi' in query:
            speak('hi sir how are you?')

        elif 'who are you' in query:
            speak('i am your assistant shofee 3.0')

        elif 'your favorite game?' in query:
            speak('my favorite game is video games sir')

        elif 'i am fine' in query:
            speak('good sir')

        elif 'what is your friends name' in query:
            speak('no friends only nithushan sir')

        elif 'play cartoon' in query:
            speak('okay baby')
            webbrowser.open('https://www.youtube.com/watch?v=zTk7G73kbHo')

        elif 'play learning video' in query:
            speak('ok opening learning video')
            webbrowser.open('abcd learning.mp4')
            
        elif 'open night song' in query:
            speak('okay enjoi the video song baby')
            webbrowser.open('https://www.youtube.com/watch?v=c-9XvIamKdM')

        elif 'play dora cartoon' in query:
            speak('okay baby enjoi the cartoon ')
            webbrowser.open('https://www.youtube.com/watch?v=N33ldfKwdLs')

        elif 'teaching 123' in query:
            speak('ok baby enjoi the 1 2 3 learning')
            webbrowser.open('https://www.youtube.com/watch?v=x6D51-pz2A4')

        elif 'open english video' in query:
            speak('ok baby go to the learning english')
            webbrowser.open('https://www.youtube.com/watch?v=by1QAoRcc-U')

        elif 'iam sleeping' in query:
            speak('wait im song play')
            webbrowser.open('https://www.youtube.com/watch?v=mSEYTJZ4N_c')

        elif 'tell me about you' in query:
            speak('my name is shofee vertion 3.0')
            

        elif 'open tamil learning video ' in query:
            speak('okay im teaching your baby')
            webbrowser.open('https://www.youtube.com/watch?v=hFbciVNxN0w')
        
        elif 'play animals song' in query:
            speak('wait im play song')
            webbrowser.open('https://www.youtube.com/watch?v=s7pcWnlwcjA')

        elif 'play tamil movie' in query:
            speak('wait im play tamil movie')
            webbrowser.open('https://www.youtube.com/watch?v=WY12sD4Rm-I&t=2233s')

        elif 'play english movie' in query:
            speak('wait im play english movie')
            webbrowser.open('https://www.youtube.com/watch?v=ABMsTsFVqB4')

        elif 'play tamil song' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/watch?v=0FsPYnmjkN4')

        elif 'play english song' in query:
            speak('okay sir')
            webbrowser.open('https://www.youtube.com/watch?v=Io0fBr1XBUA')

        elif 'about me' in query:
            speak('you are very kind and you are very beautiful')

        elif '' in query:
            speak('wait baby')
            webbrowser.open('g6.mp4')

        elif 'grade seven video' in query:
            speak('wait baby')
            webbrowser.open('g7.mp4')

        elif 'grade eight video' in query:
            speak('wait baby')
            webbrowser.open('g8.mp4')

        elif 'grade nine video' in query:
            speak('wait baby')
            webbrowser.open('9.mp4')

        elif 'grade ten video' in query:
            speak('wait baby')
            webbrowser.open('ga7.mp4')

        elif 'play the rock pepar sisser' in query:
            speak('okey sir im redy')

        elif 'rock pepar sisser' in query:
            speak('rock pepar sisser.')

        elif 'rock' in query:
            speak('paper')
            speak('sir you noob i am pro player so im winner.')

        elif 'pepar' in query:
            speak('sisser')
            speak('sir you noob i am pro player so im winner.')

        elif 'sisser' in query:
            speak('sir you noob i am pro player so im winner.')

        elif 'grade 9 video' in query:
            speak('wait im play video baby')
            webbrowser.open('g11.mp4')

        elif 'your girl' in query:
            speak('yes sir im girl')
        
        elif'you speech tamil' in query:
            speak('no im shpeeching tamil')
        
        elif'what is your father name' in query:
            speak('no father only nithushan sir')
   
        elif'play offline movie' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/watch?v=B5csN8gQY4E')

        elif'what is your copy ' in query:
            speak('my copy is speeching')
        
        elif'what is my father name' in query:
            speak('your father name is kanapathipillai mohan sir')

        elif'what is my mother name' in query:
            speak('your mother name is mohan yokalatsumi')

        elif'hi shofy' in query:
            speak('hi sir how are you?')

        elif'im fine' in query:
            speak('okey sir')

        elif'please tell me story' in query:
            speak('okey sir')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy how are yu sir']
            speak(random.choice(stMsgs))

        elif "Tell me motivation Quotes" in query or 'motivate me' in query:
            stMsgs = ['Failure will never overtake me if my determination to succeed is strong enough',
                      'The past cannot be changed. The future is yet in your power',
                      'Only I can change my life. No one can do it for me',
                      'Change your life today. Don\'t gamble on the future, act now, without delay',
                      'Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step',
                      'Either I will find a way, or I will make one',
                      'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time',
                      'Good, better, best. Never let it rest. Till your good is better and your better is best']
            highMsgs = ['Dont worry dude,every hard time comes to an end']
            speak(random.choice(stMsgs))
            speak('I think thins Motivated You sir ... if Not')
            speak(random.choice(highMsgs))
            
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'what time is it' in query or 'what is the time skava' in query or 'what time is it' in query or 'time' in query or 'current time' in query:
            speak('The current time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

        elif 'what date is it' in query or 'what is the date skava' in query or 'what date is it' in query or 'date' in query or 'current date' in query:
            speak('The current time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

        elif 'hello' in query:
            speak('Hello Sir how are you?')

                                    
        elif 'play music' in query or 'play songs' in query or 'play songs skava' in query:
            music_folder = 'C:/Users/nithu/Desktop/catch-the-ghost'
            music = ['Alex_Sparrow-sheiscrazybutsheismine','wedont','Konjam','stressedout']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'play english music' in query or 'play english songs' in query or 'play english songs skava' in query:
            music_folder = 'C:/Users/nithu/Desktop/catch-the-ghost'
            music = ['Alex_Sparrow-sheiscrazybutsheismine','wedont','Konjam','stressedout']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'play tamil music' in query or 'play tamil songs' in query or 'play tamil songs skava' in query:
            music_folder = 'C:/Users/nithu/Desktop/catch-the-ghost'
            music = ['Konjam']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'play hindi music' in query or 'play hindi songs' in query or 'play hindi songs skava' in query:
            music_folder = 'C:/Users/nithu/Desktop/catch-the-ghost'
            music = ['ikvaariaa']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('google says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('any Command! Sir!')