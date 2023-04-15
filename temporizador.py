import tkinter as tk

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Temporizador CMFSA")

        self.label = tk.Label(master, font=("Arial", 30), text="")
        self.label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Arial", 20))
        self.entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Iniciar", font=("Arial", 20), command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.pause_button = tk.Button(master, text="Pausar", font=("Arial", 20), command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_button = tk.Button(master, text="Reiniciar", font=("Arial", 20), command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.running = False
        self.time_left = 0

    def start_timer(self):
        if not self.running:
            try:
                self.time_left = int(self.entry.get())
            except ValueError:
                self.label.configure(text="Digite um número válido!")
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
        self.label.configure(text="")

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
            self.label.configure(text="Tempo esgotado!")
            self.running = False

            self.start_button.configure(state=tk.NORMAL)
            self.pause_button.configure(text="Pausar", state=tk.DISABLED)
            self.reset_button.configure(state=tk.NORMAL)

root = tk.Tk()
app = TimerApp(root)
root.mainloop()




