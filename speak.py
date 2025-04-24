import pyttsx3
import datetime
import sys

def say(text):

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    
if __name__ == '__main__':
    say(sys.argv[1])