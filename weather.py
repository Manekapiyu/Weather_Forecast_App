from email.mime import image
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
label1=Label(root,text="Temprature",font=('Helvetiica',11), fg="white" , bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity",font=('Helvetiica',11), fg="white" , bg="#203243")
label2.place(x=50,y=120)

label3=Label(root,text="Pressure",font=('Helvetiica',11), fg="white" , bg="#203243")
label3.place(x=50,y=120)

label4=Label(root,text="Wind Speed",font=('Helvetiica',11), fg="white" , bg="#203243")
label4.place(x=50,y=120)

label5=Label(root,text="Description",font=('Helvetiica',11), fg="white" , bg="#203243")
label5.place(x=50,y=120)

##search box
Sreach_image=PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage=Label(image=Sreach_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="Images/Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0 , fg="white")
textfield.place(x=370)


root.mainloop()
