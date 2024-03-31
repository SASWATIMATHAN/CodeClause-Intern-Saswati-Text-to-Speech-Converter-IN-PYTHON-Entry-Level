from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os

mainwindow= Tk()
mainwindow.title('SAM Text-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='OliveDrab1')

def say(text1):
     language = 'en'
     speech = gTTS(text = text1, lang = language, slow = False)
     speech.save("text.mp3")
     os.system("start text.mp3")

def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text

def TextToSpeech():
    texttospeechwindow = Toplevel(mainwindow)
    texttospeechwindow.title('Text-to-Speech Converter by SAM')
    texttospeechwindow.geometry("500x500")
    texttospeechwindow.configure(bg='turquoise1')

    Label(texttospeechwindow, text='Text-to-Speech Converter by SAM', font=("Arial Black", 20), bg='SeaGreen1').place(x=50)

    text = Text(texttospeechwindow, height=5, width=30, font=14)
    text.place(x=7, y=60)
    
    speakbutton = Button(texttospeechwindow, text='LISTEN', bg='Peachpuff2', command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=140, y=200)

def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter by SAM')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='CadetBlue1')

    Label(speechtotextwindow, text='Speech-to-Text Converter by SAM', font=("Brush Script Std", 18), bg='cornflower blue').place(x=50)

    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.place(x=7, y=100)
    
    recordbutton = Button(speechtotextwindow, text='RECORD', bg='RosyBrown1', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=140, y=50)

Label(mainwindow, text='SAM Text-To-Speech and Speech-To-Text Converter',
     font=('Arial Black', 16), bg='SteelBlue1', wrap=True, wraplength=450).place(x=25, y=0)

texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='Coral1', command=TextToSpeech)
texttospeechbutton.place(x=100, y=150)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='Coral1', command=SpeechToText)
speechtotextbutton.place(x=100, y=250)

mainwindow.update()
mainwindow.mainloop()
