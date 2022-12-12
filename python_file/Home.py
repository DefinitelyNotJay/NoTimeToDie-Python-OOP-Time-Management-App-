import tkinter as tk
from tkinter import PhotoImage
import requests
import json
import datetime
from PIL import ImageTk, Image
from weather import weather_widget
from todo import main
from final_timer import timer
# all widgets

# Creating class
class Homepage(tk.Tk):
    def __init__(self):
        """ All variables and GUI config """
        super().__init__()
        self.title("No Time To Die")
        self.geometry("400x600+450+25")
        self.resizable(False, False)
        # widgets
        self.all_widgets()
        self.show_widgets()

    def all_widgets(self):
        self.todo_btn = tk.Button(self, text="To Do", command=main)
        self.timer_btn = tk.Button(self, text="Timer", command=timer)
        self.weather_btn = tk.Button(self, text="Weather", command=weather_widget)
    
    def show_widgets(self):
        self.todo_btn.pack()
        self.timer_btn.pack()
        self.weather_btn.pack()
        
homepage = Homepage()
homepage.mainloop()
