import tkinter
from unicodedata import name
from bs4 import BeautifulSoup
import requests
from tkinter import *


class Info:
    def __init__(self):
        self.names = []
        self.description = []

    def get_info(self):
        url = "https://www.timeout.com/film/best-movies-of-all-time"

        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        self.names = soup.findAll('h3', class_="_h3_cuogz_1")
        self.description = soup.findAll('div', class_="_summary_1p2xe_21")

    def get_names(self):
        for i in self.names:
            print(i.text)

    def get_description(self):
        for i in self.description:
            print(i.text)

    def window(self):
        box = Tk()

        box.geometry("500x500")

        Text_box = Text(box, height= 15, width= 55)
        for i in self.names[:100]:
            label = Label(box, text=f"{i.text}")
            label.config(font=("Courier", 14))
        for g in self.description:
            Fact = f"{g.text}"

        label.pack()
        Text_box.pack()

        Text_box.insert(tkinter.END, Fact)
        tkinter.mainloop()


A = Info()
A.get_info()
A.window()



