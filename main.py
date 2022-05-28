import tkinter
from tkinter import ttk
from unicodedata import name
from bs4 import BeautifulSoup
import requests
from tkinter import *


class Info:
    def __init__(self):
        self.names = []
        self.description = []
        self.c = 0

    def get_info(self):
        url = "https://www.timeout.com/film/best-movies-of-all-time"

        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        self.names = soup.findAll('h3', class_="_h3_cuogz_1")
        self.description = soup.findAll('div', class_="_summary_1p2xe_21")

    def window(self):
        box = Tk()

        box.geometry("500x500")

        Text_box = Text(box, height=15, width=55)

        self.label = Label(box, text=f"{self.names[self.c].text}")
        self.label.config(font=("Courier", 14))

        self.Fact = f"{self.description[self.c].text}"

        next_button = Button(box, command=self.next_clicked(), text="Next")
        previous_button = Button(box, command=self.prev_clicked(), text="Prev")

        previous_button.pack()
        next_button.pack()
        self.label.pack()
        Text_box.pack()

        Text_box.insert(tkinter.END, self.Fact)
        tkinter.mainloop()

    def next_clicked(self):
        self.c += 1
        self.label["text"] = self.names[self.c]



    def prev_clicked(self):
        if self.c < 0:
            quit()
        else:
            self.c -= 1
            self.Fact = self.description[self.c]


A = Info()
A.get_info()
A.window()
