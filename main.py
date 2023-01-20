import tkinter as tk
from tkinter import ttk
import speech_recognition as sr

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("bxTranscriptor")
        self.resizable(False, False)
        self.name_var = tk.StringVar()
        self.devicesListbox = ttk.Combobox(self)
        self.devicesListbox['values'] = sr.Microphone.list_microphone_names()
        self.devicesListbox['state'] = 'readonly'
        self.devicesListbox.set('Audio device')
        self.devicesListbox.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="WENS")
        ttk.Button(self, text = "Transcript", command = self.transcript).grid(row=0, column=2, padx=5, pady=5, sticky="WENS")
        self.output = tk.Text()
        self.output['state'] = 'disabled'
        self.output.grid(row=1, column=0, padx=5, pady=5, columnspan=3)
        print(sr.AudioSource)
        
    def transcript(self):
        print(sr.Microphone.list_microphone_names().index(self.devicesListbox.get()))
        with sr.Microphone(device_index=sr.Microphone.list_microphone_names().index(self.devicesListbox.get())) as source:
            try:
                audio = sr.Recognizer().listen(source)
                self.text = sr.Recognizer().recognize_google(audio, language='pl-PL') # Language here!
                if self.text != "":
                    self.output['state'] = 'normal'
                    self.output.insert('2.0', str(self.text) + "\n\n")
                    self.output['state'] = 'disabled'
                else:
                    return 0
            except:
                return 0

if __name__ == "__main__":
    App().mainloop()