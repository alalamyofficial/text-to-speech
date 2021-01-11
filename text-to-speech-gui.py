from tkinter import *
import pyttsx3

class Speech():
    def __init__(self, App):
        self.window = App
        self.window.title("Text To Speech")
        self.window.geometry("500x400")
        self.window.configure(bg="#EE3D17")
        self.window.iconbitmap(r'C:\python\text-to-speech\robot.ico')
        self.window.resizable(False, False) 


        self.inputText = StringVar()

        Label(App, text="Enter a Text",fg="white", font=("Times", 20), bg="#E74C3C").place(x=175,y= 30)
        self.speech = Entry(App,validate='all' , width=30, font=("Arial", 15), relief="flat",textvariable=self.inputText)
        self.male_button = Button(App, text="Male", bg="#22c1c3",font = ('Sans','15','bold'),command=self.ManVoice)
        self.female_button = Button(App, text="Female", bg="#22c1c3",font = ('Sans','15','bold'),command=self.WomanVoice)


        self.speech.place(x=90, y=120)
        self.speech.focus()
        self.male_button.place(x=150, y=220)
        self.female_button.place(x=300, y=220)


    def ManVoice(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate",150)
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice",self.voices[0].id)
        self.engine.say(self.inputText.get())
        self.engine.runAndWait() 

    def WomanVoice(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate",150)
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice",self.voices[1].id)
        self.engine.say(self.inputText.get())
        self.engine.runAndWait()



Ai_speech = Tk()
MyApp = Speech(Ai_speech)
Ai_speech.mainloop()