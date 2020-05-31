import pyglet
import speech_recognition as sr
# import pyaudio
# import wave

# def play_audio(filename):
#     chunk = 1024
#     wf = wave.open(filename, 'rb')
#     pa = pyaudio.PyAudio()

#     stream = pa.open(
#         format = pa.get_format_from_width(wf.getsampwidth()),
#         channels = wf.getnchannels(),
#         rate = wf.getframerate(),
#         outout = True
#     )

#     data_stream = wf.readframes(chunk)

#     while data_stream:
#         stream.write(data_stream)
#         data_stream = wf.readframes(chunk)

#     stream.close()
#     pa.terminate()

# play_audio("./audio/promise.mp3")

# file = pyglet.resource.media('audio/promise.mp3')
# file.play()

# pyglet.app.run()



# r = sr.Recognizer()

# with sr.Microphone() as source:
# print('say something')
# audio = r.listen(source)
# voice_data = r.recognize_google(audio)
# print(voice_data)

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

    # pyglet.app.run()

    command = ""

    try:
        command = r.recognize_google(audio)

    except:
        print("Not recognition voice")

    print("your command")
    print(command)

initSpeech()
    

