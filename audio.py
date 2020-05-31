import pyglet
import speech_recognition as sr
import subprocess

def say(text):
    #whit subpproccess we can pass console commands
    subprocess.call('say ' + text, shell=True)

r = sr.Recognizer()

def initSpeech():
    print("listening...")

    fileStart = pyglet.resource.media('audio/audio2.mp3')
    fileStart.play()


    with sr.Microphone() as source:
        print('Say someting')
        audio = r.listen(source)
    
    fileEnd = pyglet.resource.media('audio/audio1.mp3')
    fileEnd.play()

    # voice = pyglet.resource.media(audio)
    # voice.play()
    # pyglet.app.run()

    command = ""

    try:
        command = r.recognize_google(audio)

    except:
        print("Not recognition voice")

    print("your command")
    print(command)

    say('You said:' + command)

initSpeech()
    

