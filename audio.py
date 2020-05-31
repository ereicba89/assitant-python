import pyglet
import speech_recognition as sr
import subprocess
from command import Commander

running = True

def say(text):
    #whit subpproccess we can pass console commands
    subprocess.call('say ' + text, shell=True)

r = sr.Recognizer()
cmd = Commander()

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
    if command in ['quit', 'exit', 'bye', 'goodbye']:
        global running
        running = False

    cmd.discover(command)
    # say('You said:' + command)

while running == True:
    initSpeech()
    

