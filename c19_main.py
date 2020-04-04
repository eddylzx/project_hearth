import speech_recognition as SR

# get audio from the microphone
recognizer = SR.Recognizer()
with SR.Microphone() as source:
    print("Speak:")
    audio = recognizer.listen(source)

try:
    print("You said: " + recognizer.recognize_google(audio))
except SR.UnknownValueError:
    print("Could not understand audio")
except SR.RequestError as e:
    print("Could not request results; {0}".format(e))

