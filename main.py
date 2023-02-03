import tkinter as tk
import threading
from tkinter import ttk
import speech_recognition as sr

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("bxTranscriptor")
        self.resizable(False, False)
        self.style = ttk.Style()
        self.devicesListbox = ttk.Combobox(self)
        self.devicesListbox['values'] = sr.Microphone.list_microphone_names()
        self.devicesListbox['state'] = 'readonly'
        self.devicesListbox.set('Audio device')
        self.devicesListbox.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="WENS")
        self.transcriptButton = ttk.Button(self, text = "Start", style="transcriptButton.TButton", command = self.start).grid(row=0, column=2, padx=5, pady=5, sticky="WENS")
        self.output = tk.Text()
        self.output['state'] = 'disabled'
        self.output.grid(row=1, column=0, padx=5, pady=5, columnspan=3)
        
    def start(self):
        threading.Thread(target=self.transcript_worker, daemon=True).start()
        
    def transcript_worker(self):
        with sr.Microphone(device_index=sr.Microphone.list_microphone_names().index(self.devicesListbox.get())) as source:
            try:
                self.style.configure('transcriptButton.TButton', foreground="red")
                audio = sr.Recognizer().listen(source)
                self.text = sr.Recognizer().recognize_google(audio, language='pl-PL') # Language here!
                if self.text != "":
                    self.output['state'] = 'normal'
                    self.output.insert("end", str(self.text) + "\n\n")
                    self.output['state'] = 'disabled'
                    self.style.configure('transcriptButton.TButton', foreground="black")
                else:
                    self.style.configure('transcriptButton.TButton', foreground="black")
                    return 0
            except:
                self.style.configure('transcriptButton.TButton', foreground="black")
                return 0

if __name__ == "__main__":
    App().mainloop()