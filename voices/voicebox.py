import speech_recognition as sr
import os

r = sr.Recognizer()
m = sr.Microphone()
os.system('clear')

try:
    with m as source: r.adjust_for_ambient_noise(source)
    
    while True:        
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            value = r.recognize_google(audio)
            if str is bytes:
                print(u"You said {}".format(value).encode("utf-8"))
            else:
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
