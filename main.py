from unicodedata import name
from bs4 import BeautifulSoup
import requests
from tkinter import *

box = Tk()
box.geometry("800x800")
b = Button(box,text="sample")
b.pack()
box.mainloop()

url = "https://www.timeout.com/film/best-movies-of-all-time"
page = requests.get(url)

names = []
discription = []

soup = BeautifulSoup(page.text, "html.parser")

names = soup.findAll('h3', class_="_h3_cuogz_1")

discription = soup.findAll('div', class_="_summary_1p2xe_21")


# for i in discription:
#     print(i.text, end="\n")

# for i in names:
#     print(i.text)


    



