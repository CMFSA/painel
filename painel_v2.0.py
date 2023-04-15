import tkinter as tk
from tkinter import *
from playsound import playsound
import time


class App(tk.Tk):
    def __init__(self, master):
        super().__init__()
        
        self.masterframe = Frame(master)
        self.masterframe.pack(side = TOP)

        self.bottomframe = Frame(master)
        self.bottomframe.pack(side = BOTTOM)

        self.title("Temporizador CMFSA")
        master.title("Temporizador CMFSA")
        self.geometry('300x200')
        self.running = False

        try:
            if getattr(self, "time_to_reset") > 0:
                self.time_left = self.time_to_reset
        except AttributeError:
            print("erro time_to_reset")
            self.time_left = 0
            self.time_to_reset = 0

        self.masterframe.label = tk.Label(self.master, font=("Arial", 80), text="00:00")
        self.masterframe.label.pack(pady=20)

        self.label = tk.Label(self, font=("Arial", 80), text="00:00")
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Iniciar", font=("Arial", 20), fg="green", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.pause_button = tk.Button(self.master, width=10, text="Pausar", font=("Arial", 20), command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.restore_button = tk.Button(self.master, width=10, text="Restaurar", font=("Arial", 20), command=self.restore_timer, state=tk.DISABLED)
        self.restore_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_button = tk.Button(self.master, width=5, text="Zerar", font=("Arial", 20), command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.rem_3min_button = tk.Button(self.master, width=5, text="3min", font=("Arial", 20), command=lambda: self.set_time(180, True))
        self.rem_3min_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.rem_5min_button = tk.Button(self.master, width=5, text="5min", font=("Arial", 20), command=lambda: self.set_time(300, True))
        self.rem_5min_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.rem_10min_button = tk.Button(self.master, width=5, text="10min", font=("Arial", 20), command=lambda: self.set_time(600, True))
        self.rem_10min_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.add_30s_button = tk.Button(self.master, width=5, text="+ 30s", font=("Arial", 20), command=self.add_30s)
        self.add_30s_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.rem_30s_button = tk.Button(self.bottomframe, width=5, text="- 30s", font=("Arial", 20), command=self.rem_30s)
        self.rem_30s_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.start_button.configure(state=tk.DISABLED)
        self.pause_button.configure(state=tk.DISABLED)
        self.restore_button.configure(state=tk.DISABLED)
        self.reset_button.configure(state=tk.DISABLED)

    # atualiza o timer
    def update_timer(self):
        if self.time_left >= 0 and self.running:
            mins, secs = divmod(self.time_left, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.label.configure(text=timer)
            self.masterframe.label.configure(text=timer)
            self.after(1000, self.update_timer)
            self.time_left -= 1
        elif self.time_left <= 0 and self.running:            
            self.label.configure(text="00:00")
            self.masterframe.label.configure(text="00:00")
            self.running = False            
            playsound('sounds/alarm.wav')
            self.start_button.configure(state=tk.DISABLED)
            self.pause_button.configure(text="Pausar", state=tk.DISABLED)
            self.restore_button.configure(state=tk.NORMAL)
            self.reset_button.configure(state=tk.DISABLED)

    # inicia a contagem do tempo
    def start_timer(self):
        if self.time_left > 0 and not self.running:
            self.running = True
            self.update_timer()
        elif self.running:
            self.update_timer()
        self.start_button.configure(state=tk.DISABLED)
        self.pause_button.configure(state=tk.NORMAL)
        self.restore_button.configure(state=tk.NORMAL)
        self.reset_button.configure(state=tk.DISABLED)

    # pausa a contagem do tempo
    def pause_timer(self):
        if self.running:
            self.running = False
            self.pause_button.configure(text="Continuar")
            self.start_button.configure(state=tk.DISABLED)
            self.pause_button.configure(state=tk.NORMAL)
            self.restore_button.configure(state=tk.NORMAL)
            self.reset_button.configure(state=tk.NORMAL)
        else:
            self.running = True
            self.pause_button.configure(text="Pausar")
            self.start_button.configure(state=tk.DISABLED)
            self.pause_button.configure(state=tk.NORMAL)
            self.restore_button.configure(state=tk.NORMAL)
            self.reset_button.configure(state=tk.DISABLED)
            self.update_timer()

    # reinicia o tempo para a última definição
    def restore_timer(self):
        self.time_left = self.time_to_reset
        mins, secs = divmod(self.time_left, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        self.label.configure(text=timer)
        self.masterframe.label.configure(text=timer)
        self.start_button.configure(state=tk.NORMAL)
        self.pause_button.configure(text="Pausar", state=tk.DISABLED)
        self.restore_button.configure(state=tk.NORMAL)
        self.reset_button.configure(state=tk.NORMAL)
        self.running = False

    # zera o timer
    def reset_timer(self):
        self.time_left = 0
        mins, secs = divmod(self.time_left, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        self.label.configure(text=timer)
        self.masterframe.label.configure(text=timer)
        self.start_button.configure(state=tk.DISABLED)
        self.pause_button.configure(text="Pausar", state=tk.DISABLED)
        self.reset_button.configure(state=tk.DISABLED)
        self.restore_button.configure(state=tk.DISABLED)
        self.running = False       

    # define o tempo para contagem
    def set_time(self, seconds, get_time):
        self.time_left = seconds
        if get_time:
            self.time_to_reset = seconds
        mins, secs = divmod(self.time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        self.label.configure(text=time_format)
        self.masterframe.label.configure(text=time_format)
        if self.time_left <= 0 and not self.running:
            self.start_button.configure(state=tk.DISABLED)
            self.pause_button.configure(state=tk.DISABLED)
            self.restore_button.configure(state=tk.DISABLED)
            self.reset_button.configure(state=tk.DISABLED)
        elif self.time_left > 0 and not self.running:
            self.start_button.configure(state=tk.NORMAL)
            self.pause_button.configure(state=tk.DISABLED)
            self.restore_button.configure(state=tk.NORMAL)
            self.reset_button.configure(state=tk.NORMAL)
        else:
            self.start_button.configure(state=tk.DISABLED)
            self.pause_button.configure(state=tk.NORMAL)
            self.restore_button.configure(state=tk.NORMAL)
            self.reset_button.configure(state=tk.DISABLED)

    # acrescenta 30 segundos ao tempo atual
    def add_30s(self):
        self.time_left += 30
        self.set_time(self.time_left, False)

    # remove 30 segundos do tempo atual
    def rem_30s(self):
        if self.time_left >= 30:
            self.time_left -= 30
            self.set_time(self.time_left, False)


if __name__ == "__main__":
    root = tk.Tk()

    # frame = Frame(root)
    # frame.pack()

    # bottomframe = Frame(root)
    # bottomframe.pack( side = BOTTOM )

    app = App(root)
    app.mainloop()