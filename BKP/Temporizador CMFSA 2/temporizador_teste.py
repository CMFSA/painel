import tkinter as tk
import time

class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Temporizador CMFSA")

        self.time_left = 0
        self.paused = False

        self.time_label = tk.Label(master, text="00:00", font=("Arial", 70))
        self.time_label.pack()

        self.start_button = tk.Button(master, text="Iniciar", font=("Arial", 20), command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(master, text="Pausar", font=("Arial", 20), command=self.pause, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(master, text="Reiniciar", font=("Arial", 20), command=self.reset, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT)
        
        """self.thirty_button = tk.Button(master, text="+ 30s", command=self.add_thirty_seconds)
        self.thirty_button.pack(side=tk.LEFT)"""
        
        self.one_minute_button = tk.Button(master, text="1 minuto", command=lambda: self.set_time(60))
        self.one_minute_button.pack(side=tk.LEFT)
        
        self.three_minutes_button = tk.Button(master, text="3 minutos", command=lambda: self.set_time(180))
        self.three_minutes_button.pack(side=tk.LEFT)
        
        self.five_minutes_button = tk.Button(master, text="5 minutos", command=lambda: self.set_time(300))
        self.five_minutes_button.pack(side=tk.LEFT)
        
        self.ten_minutes_button = tk.Button(master, text="10 minutos", command=lambda: self.set_time(600))
        self.ten_minutes_button.pack(side=tk.LEFT)

    def start(self):
        if self.time_left > 0 and self.paused:
            self.paused = False
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
            self.countdown(self.time_left)
        elif not self.paused:
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
            self.countdown(self.time_left)

    def pause(self):
        self.paused = True
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def reset(self):
        self.time_left = 0
        self.time_label.config(text="00:00")
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

    def countdown(self, seconds):
        self.time_left = seconds
        while self.time_left > 0:
            if not self.paused:
                mins, secs = divmod(self.time_left, 60)
                time_format = '{:02d}:{:02d}'.format(mins, secs)
                self.time_label.config(text=time_format)
                time.sleep(1)
                self.time_left -= 1
            else:
                break
        else:
            self.time_label.config(text="00:00")
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)

    def set_time(self, seconds):
        self.time_left = seconds
        mins, secs = divmod(self.time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        self.time_label.config(text=time_format)
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

root = tk.Tk()
app = Timer(root)
root.mainloop()
