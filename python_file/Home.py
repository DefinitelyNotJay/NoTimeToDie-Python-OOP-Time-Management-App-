import tkinter as tk
from tkinter import PhotoImage
import requests
import json
import datetime
from PIL import ImageTk, Image
from weather import weather_widget
from todo import main
from timer import timer
# all widgets
# Creating class
class Homepage(tk.Tk):
    def __init__(self):
        """ All variables and GUI config """
        super().__init__()
        self.title("No Time To Die")
        self.geometry("400x600+450+25")
        self.resizable(False, False)
        self.config(background="#f3d9fa")
        # widgets
        self.all_widgets()
        self.show_widgets()

    def all_widgets(self):
        self.todo_btn = tk.Button(self, text="To Do", command=main)
        self.timer_btn = tk.Button(self, text="Timer", command=timer)
        self.weather_btn = tk.Button(self, text="Weather", command=weather_widget)
    def show_widgets(self):
        self.todo_btn.place(x=180, y=400)
        self.timer_btn.place(x=180, y=350)
        self.weather_btn.place(x=175, y=300)
homepage = Homepage()
homepage.mainloop()
