import tkinter as tk
import datetime
import winsound as ws
from tkinter import ttk

# Creating class
class Countdown(tk.Frame):
    def __init__(self, master):
        """ all functions """
        self.root = master
        self.root.title('Timer')
        self.root.geometry("300x500")
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False

    def show_widgets(self):
        """ pack all widgets """
        self.label.pack()
        self.entry_hr.pack()
        self.entry_min.pack()
        self.entry_sec.pack()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def create_widgets(self):
        """ create & design all widgets """
        self.label = tk.Label(self, text = "Enter the time in seconds.")
        self.entry_hr = tk.ttk.Entry(self, width = 3, justify="center")
        self.entry_min = tk.ttk.Entry(self, width = 3, justify="center")
        self.entry_sec = tk.ttk.Entry(self, width = 3, justify="center")
        self.entry_sec.focus_set()
        self.reset = tk.ttk.Button(self, text= "Reset Timer",
        command=self.reset_button)
        self.stop = tk.ttk.Button(self, text= "Stop Timer",
        command=self.stop_button)
        self.start = tk.ttk.Button(self, text= "Start Timer",
        command=self.start_button)

    def get_time(self):
        hr = int(self.entry_hr.get())*3600 if self.entry_hr.get() != "" else 0
        minutes = int(self.entry_min.get())*60 if self.entry_min.get() != "" else 0
        sec = int(self.entry_sec.get()) if self.entry_sec.get() != "" else 0
        return hr + minutes + sec

    def countdown(self):
        self.label["text"] = self.convert_seconds_left_to_time()
        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False
            # ws.PlaySound("", ws.SND_FILENAME)

    def reset_button(self):
        self.seconds_left = 0
        self.stop_timer()
        self._timer_on = False
        self.label["text"] = "Enter the time in seconds."
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def stop_button(self):
        self.seconds_left = self.get_time()
        self.stop_timer()
    
    def start_button(self):
        # get time from label
        self.seconds_left = self.get_time()
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)
    
    def showing_cat(self):
        cat_list = []
        # divide 4

# Main loop
def main():
    root = tk.Tk()
    countdown = Countdown(root)
    countdown.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
