
import tkinter as tk
import datetime
import winsound as ws
from tkinter import PhotoImage

# Creating class
class Countdown(tk.Tk):
    def __init__(self):
        """ Declare all functions and variables """
        super().__init__()
        self.title('Timer')
        self.geometry("300x500+500+70")
        self.resizable(False, False)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False
        self.FONT1 = ('Tahoma', 22)
        self.FONT2 = ('Tahoma', 18)

    def create_widgets(self):
        """ create & design all widgets """
        self.canvas = tk.Canvas(self, bg = "#191845", height = 500, width = 300, bd = 0, highlightthickness = 0, relief = "ridge")
        self.image_image_1 = PhotoImage(file=("images/timer_img/image_1.png"))
        image_1 = self.canvas.create_image(162.0, 255.0, image=self.image_image_1)
        self.canvas.create_text(183.0, 141.0, anchor="nw", text="sec", fill="#FFFFFF", font=("Acme", 16 * -1))
        self.canvas.create_text(141.0, 141.0, anchor="nw", text="min", fill="#FFFFFF", font=("Acme", 16 * -1))
        self.canvas.create_text(108.0, 140.0, anchor="nw", text="hr", fill="#FFFFFF", font=("Acme", 16 * -1))
        self.canvas.create_text(106.5, 240.0, anchor="nw", text="enter the time", fill="#FFFFFF", font=("Acme", 18 * -1))
        # ********
        self.text_label = tk.Label(text="0:00:00", font=("TH sarabunPSK", 22), bg="#8b84ad")

        # ---------- hour ----------

        self.entry_hour_image = PhotoImage(file=("images/timer_img/entry_1.png"))
        self.entry_hr = tk.Entry(bd=0, bg="#747395", fg="#fff", highlightthickness=0, justify = "ce")

        # ---------- min ----------

        self.entry_min_image = PhotoImage(file=("images/timer_img/entry_2.png"))
        self.entry_min = tk.Entry(bd=0, bg="#797ba0", fg="#fff", highlightthickness=0, justify = "ce")

        # ---------- sec ----------

        self.entry_sec_image = PhotoImage(file=("images/timer_img/entry_3.png"))
        self.entry_sec = tk.Entry(bd=0, bg="#666da3", fg="#fff", highlightthickness=0, justify = "ce")
        self.entry_sec.focus_set()
        self.reset = tk.Button(self, text= "Reset Timer", font=('Concert One', 12), bg='#7048e8',fg='#f3f0ff',
        command=self.reset_button)
        self.stop = tk.Button(self, text= "Stop Timer", font=('Concert One', 12), bg='#845ef7',fg='#f3f0ff',
        command=self.stop_button)
        self.start = tk.Button(self, text= "Start Timer", font=('Concert One', 12), bg='#b197fc',fg='#f3f0ff',
        command=self.start_button)

    def show_widgets(self):
        """ pack all widgets """
        self.canvas.place(x = 0, y = 0)
        self.text_label.place(x = 103, y = 100.0)
        self.entry_min.place(x=137.5, y=220, width=35.0, height=15.0)
        self.entry_sec.place(x=192.5, y=220.0, width=35.0, height=15.0)
        self.entry_hr.place(x=82.5, y=220.0, width=35.0, height=15.0)
        self.start.place(x=110, y=280)
        self.stop.place(x=113, y=330)
        self.reset.place(x=109, y=380)

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
        self.start.place(x=110, y=280)
        self.stop.place(x=113, y=330)
        self.reset.place(x=109, y=380)

    def countdown(self):
        self.text_label["text"] = self.convert_seconds_left_to_time()
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
        self.text_label["text"] = "0:00:00"
        self.text_label.place(x = 103, y = 100.0) #get Label back in position
        self.after_button()

    def stop_button(self):
        self.seconds_left = self.get_time()
        self.stop_timer()
    
    def start_button(self):
        # get time from label
        self.seconds_left = self.get_time()
        self.stop_timer()
        self.countdown()
        self.after_button()
        self.text_label.place(x = 103, y = 100.0)

    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)

if __name__ == "__main__":
    countdown = Countdown()
    countdown.mainloop()
