from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests, pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Weather App")
root.geometry("890*470+300+200")
root.configure(bg="#57adff")
root.resizable(False,False)

##icon
image_icon=PhotoImage(file="Images/logo.png")
root.iconPhoto(False,image_icon)

Round_box=PhotoImage(file="Images/Rounded Rectangle 1.png")
Label (root,image=Round_box="#57adff").place(x=30,y=110)

#label
label1=Label(root,text="Temprature",font=('Helvetiica'))

root.mainloop()
