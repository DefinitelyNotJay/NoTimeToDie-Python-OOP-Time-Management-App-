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
        self.configure(bg = "#191845")
        self.icon = PhotoImage(file="images/icon/home.png")
        self.iconphoto(False, self.icon)
        # widgets
        self.all_widgets()
        self.show_widgets()

    def all_widgets(self):
        self.canvas = tk.Canvas(self, bg = "#191845", height = 600, width = 400, bd = 0, highlightthickness = 0, relief = "ridge")
        self.image_image_1 = tk.PhotoImage(file="images/home_img/image_1.png")
        self.image_image_2 = tk.PhotoImage(file="images/home_img/button_timer.png")
        self.image_image_3 = tk.PhotoImage(file="images/home_img/button_todo.png")
        self.image_image_4 = tk.PhotoImage(file="images/home_img/button_weather.png")
        self.todo_btn = tk.Button(self, bg="#544d94", command=main, image=self.image_image_3, relief=tk.SUNKEN, cursor='hand2', border=0, borderwidth = 0, activebackground='#544d94')
        self.timer_btn = tk.Button(self, bg="#544d94", command=timer, image=self.image_image_2, relief=tk.SUNKEN, cursor='hand2', border=0, borderwidth = 0, activebackground='#544d94')
        self.weather_btn = tk.Button(self, bg="#544d94", command=weather_widget, image=self.image_image_4, relief=tk.SUNKEN, cursor='hand2', border=0, borderwidth = 0, activebackground='#544d94')
    def show_widgets(self):
        self.canvas.place(x = 0, y = 0)
        image_1 = self.canvas.create_image(200, 300, image=self.image_image_1)
        self.todo_btn.place(x=149.0, y=346.0, width=98.0, height=36)
        self.timer_btn.place(x=149.0, y=406.0, width=98.0, height=36)
        self.weather_btn.place(x=149.0, y=470.0, width=98.0, height=36)
homepage = Homepage()
homepage.mainloop()
