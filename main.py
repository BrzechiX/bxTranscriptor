import tkinter as tk
import speech_recognition as sr

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("bxTranscriptor")
        self.configure(bg="#303030")
        tk.Button(self, text = "Transcript" , height=1, width=20, bd=0, bg='#2222dd', fg='#ffffff', activebackground='#11ff11', activeforeground="#ffffff", command = self.transcript).grid(padx=20, pady=20)

    def transcript(self):
        with sr.Microphone() as source:
            try:
                audio = sr.Recognizer().listen(source)
                text = sr.Recognizer().recognize_google(audio, language='pl-PL')
                if text != "":
                    print(text)
                else:
                    return 0
            except:
                return 0

if __name__ == "__main__":
    App().mainloop()