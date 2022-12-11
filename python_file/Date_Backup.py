import tkinter as tk
import datetime
import winsound as ws
from tkinter import ttk

# Creating class
class Countdown(tk.Tk):
    def __init__(self):
        """ Declare all functions and variables """
        super().__init__()
        self.title('Timer')
        self.geometry("300x500+800+200")
        self.resizable(False, False)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False
        self.FONT1 = ('Tahoma', 22)
        self.FONT2 = ('Tahoma', 18) 

    def show_widgets(self):
        """ pack all widgets """
        self.label.place(x=80, y=60)
        self.entry_hr.place(x=90, y=120)
        self.entry_min.place(x=130, y=120)
        self.entry_sec.place(x=170, y=120)
        self.start.place(x=100, y=180)
        self.stop.place(x=100, y=220)
        self.reset.place(x=100, y=260)

    def create_widgets(self):
        """ create & design all widgets """
        self.label = tk.Label(self, text = "Enter the time in seconds.", font=('Arial', 10))
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
    
    def after_button(self):
        """ get all buttons back from pressing reset or start """
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.place(x=100, y=180)
        self.stop.place(x=100, y=220)
        self.reset.place(x=100, y=260)

    def countdown(self):
        self.label["text"] = self.convert_seconds_left_to_time()
        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False
            # ws.PlaySound("", ws.SND_FILENAME)

    def reset_button(self):
        """ Reset to 00:00:00 """
        self.seconds_left = 0
        self.stop_timer()
        self._timer_on = False
        self.label["text"] = "Enter the time in seconds."
        self.label.place(x=80, y=60) #get Label back in position
        self.after_button()

    def stop_button(self):
        """ Stop time """
        self.seconds_left = self.get_time()
        self.stop_timer()
    
    def start_button(self):
        # get time from label and start counting down the time
        self.seconds_left = self.get_time()
        self.stop_timer()
        self.countdown()
        self.after_button()
        self.label.place(x=120, y=60)

    def stop_timer(self):
        """ Stop time function() """
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)
    
    def showing_cat(self):
        cat_list = []
        # divide 4

if __name__ == "__main__":
    countdown = Countdown()
    countdown.mainloop()
