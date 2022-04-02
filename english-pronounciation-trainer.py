import speech_recognition.speech_recognition as sr
print('Englisch Vokabeltrainer')
from random import randint

d = {
    'Behinderung':'disability', 'körperlich':'physical', 'geistig':'intellectual', 'Zeichen':'sign',
     'Blindenhund':'guide dog', 'Einbeziehung':'inclusion', 'einschließlich':'inclusive', 'Schulbildung':'schooling',
     'System':'system', 'unterschreiben':'to sign','richtig':'right',
    'Erfolg':'sucess', 'Artikel':'article', 'Kaktus':'cactus'
    }


antwort = ""
while antwort is not "Ende":
    zufall = randint(0,13)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Was bedeutet "' + list(d.keys())[zufall] + '"?')
        antwort=r.listen(source)
    try:
        if r.recognize_google(antwort,language='en-US') == list(d.values())[zufall]:
            print("Das ist richtig. ✔")
        else:
            print("Das ist leider falsch. ❌")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
print('Auf Wiedersehen!')
