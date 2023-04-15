import tkinter as tk
from playsound import playsound

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Temporizador CMFSA")

        self.label = tk.Label(master, font=("Arial", 80), text="00:00")
        self.label.pack(pady=20)

        #self.entry = tk.Entry(master, font=("Arial", 20))
        #self.entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Iniciar", font=("Arial", 20), command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.pause_button = tk.Button(master, text="Pausar", font=("Arial", 20), command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_button = tk.Button(master, text="Reiniciar", font=("Arial", 20), command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.rem_3min_button = tk.Button(master, text="3min", font=("Arial", 20), command=self.add_3min)
        self.rem_3min_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.rem_5min_button = tk.Button(master, text="5min", font=("Arial", 20), command=self.add_5min)
        self.rem_5min_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.rem_10min_button = tk.Button(master, text="10min", font=("Arial", 20), command=self.add_10min)
        self.rem_10min_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.add_30s_button = tk.Button(master, text="+ 30s", font=("Arial", 20), command=self.add_30s)
        self.add_30s_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.rem_30s_button = tk.Button(master, text="- 30s", font=("Arial", 20), command=self.rem_30s)
        self.rem_30s_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.running = False
        self.time_left = 0

    def start_timer(self):
        if not self.running:
            try:
                self.time_left = int(self.entry.get())
            except ValueError:
                self.label.configure(text="TEMPO EM SEGUNDOS")
                return

            self.running = True
            self.update_timer()            

            self.start_button.configure(state=tk.DISABLED)
            self.pause_button.configure(text="Pausar", state=tk.NORMAL)
            self.reset_button.configure(state=tk.NORMAL)

    def pause_timer(self):
        if self.running:
            self.running = False
            self.pause_button.configure(text="Continuar")
        else:
            self.running = True
            self.pause_button.configure(text="Pausar")
            self.update_timer()

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.label.configure(text="00:00")

        self.entry.delete(0, tk.END)

        self.start_button.configure(state=tk.NORMAL)
        self.pause_button.configure(text="Pausar", state=tk.DISABLED)
        self.reset_button.configure(state=tk.DISABLED)

    def update_timer(self):
        if self.time_left >= 0 and self.running:
            mins, secs = divmod(self.time_left, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.label.configure(text=timer)            

            self.master.after(1000, self.update_timer)
            self.time_left -= 1                   
            
        elif self.running:            
            self.label.configure(text="TEMPO \n ENCERRADO!")                        
            self.running = False            
            playsound('alarm.wav')

            self.start_button.configure(state=tk.NORMAL)
            self.pause_button.configure(text="Pausar", state=tk.DISABLED)
            self.reset_button.configure(state=tk.NORMAL)

    def add_3min(self):
        self.time_left = 180
        self.update_label() 

    def add_5min(self):
        self.time_left = 300
        self.update_label() 

    def add_10min(self):
        self.time_left = 600
        self.update_label() 

    def add_30s(self):
        self.time_left += 31
        self.update_label()  

    def rem_30s(self):
        self.time_left -= 29
        self.update.label()

root = tk.Tk()
app = TimerApp(root)
root.mainloop()


