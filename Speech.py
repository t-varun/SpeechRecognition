#https://cloud.google.com/speech-to-text/docs/languages


import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()
while(True):
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        with sr.Microphone() as source:
            print("Say Something")
            audio = r.listen(source)
            print("Time over, Thanks")
    try:
        print("TEXT :"+r.recognize_google(audio))
        #print("TEXT :"+r.recognize_google(audio, language = 'hi-IN'))
        #print("TEXT :"+r.recognize_google(audio, language = 'te-IN'))
    except:
        pass


