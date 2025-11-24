from tkinter import *
import tkinter as tk
from tkinter import font
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import requests, pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # Weather
    api = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.latitude)+"&units=metric&exclude=hourly&appid=63c08bc7df89446bbcd170000252311"

    json_data = requests.get(api).json()

    #current
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    
    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)

    #frist cell
    firstdayimage=json_data['daily'][0]['weather'][0]['icon']
    photo1=ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1=json_data['daily'][0]['temp']['day']
    tempnight=json_data['daily'][0]['temp']['night']
    day1temp.config(text=f"{tempday1}°C / {tempnight}°C")

    #second cell
    seconddayimage=json_data['daily'][1]['weather'][0]['icon']
    img=(Image.open("icon/{seconddayimage}@2x.png"))
    resize_image=img.resize((50,50))
    photo2=ImageTk.PhotoImage(resize_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    tempday2=json_data['daily'][1]['temp']['day']
    tempnight=json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"{tempday2}°C / {tempnight}°C")
    

    #third cell
    thirddayimage=json_data['daily'][2]['weather'][0]['icon']

    img=(Image.open("icon/{thirddayimage}@2x.png"))
    resize_image=img.resize((50,50))
    photo3=ImageTk.PhotoImage(resize_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo2

    tempday3=json_data['daily'][2]['temp']['day']
    tempnight=json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"{tempday3}°C / {tempnight}°C")
    
   

    #fouth cell
    fourthdayimage=json_data['daily'][3]['weather'][0]['icon']

    img=(Image.open("icon/{fourthdayimage}@2x.png"))
    resize_image=img.resize((50,50))
    photo4=ImageTk.PhotoImage(resize_image)
    forthimage.config(image=photo4)
    forthimage.image=photo4

    tempday4=json_data['daily'][3]['temp']['day']
    tempnight=json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"{tempday4}°C / {tempnight}°C")
  

    #fifth cell
    fifthdayimage=json_data['daily'][4]['weather'][0]['icon']

    img=(Image.open("icon/{fifthdayimage}@2x.png"))
    resize_image=img.resize((50,50))
    photo5=ImageTk.PhotoImage(resize_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5

    tempday5=json_data['daily'][4]['temp']['day']
    tempnight=json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"{tempday5}°C / {tempnight}°C")

   

   

    #sixth cell
    sixthdayimage=json_data['daily'][5]['weather'][0]['icon']

    img=(Image.open("icon/{sixthdayimage}@2x.png"))
    resize_image=img.resize((50,50))
    photo6=ImageTk.PhotoImage(resize_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6

    tempday6=json_data['daily'][5]['temp']['day']
    tempnight=json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"{tempday6}°C / {tempnight}°C")


    #seventh cell
    seventhdayimage=json_data['daily'][6]['weather'][0]['icon']

    img=(Image.open("icon/{seventhdayimage}@2x.png"))
    resize_image=img.resize((50,50))
    photo7=ImageTk.PhotoImage(resize_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7

    tempday7=json_data['daily'][6]['temp']['day']
    tempnight=json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"{tempday7}°C / {tempnight}°C")
    

    #days

    first=datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))



# App icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

# Rounded main box
Round_box = PhotoImage(file="Images/Rounded Rectangle 1.png")
label = Label(root, image=Round_box, bg="#57adff")
label.place(x=30, y=110)

# Bottom labels (corrected positions)
label1 = Label(root, text="Temperature", font=('Helvetica', 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=('Helvetica', 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=('Helvetica', 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=('Helvetica', 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

# Search bar
Search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(root, image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weather_icon = PhotoImage(file="Images/Layer 7.png")
weatherimage = Label(root, image=weather_icon, bg="#203243")
weatherimage.place(x=290, y=127)

# Entry field (fixed)
textfield = tk.Entry(root, justify='center', width=15,
                     font=('Poppins', 25, 'bold'),
                     bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

# Search button
Search_icon = PhotoImage(file="Images/Layer 6.png")
myimage_icon = Button(root, image=Search_icon, borderwidth=0,
                      cursor="hand2", command=getWeather)
myimage_icon.place(x=645, y=125)

# Bottom frame
frame = Frame(root, width=900, height=180, bg='#212120')
frame.pack(side=BOTTOM)

firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

# Clock
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# Timezone text
timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

# Coordinates
long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

#thpwd
t = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
t.place(x=150, y=220)
h = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
h.place(x=150, y=140)
p = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
p.place(x=150, y=160)
w = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
w.place(x=150, y=180)
d = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
d.place(x=150, y=200)



#first cell
firstFrame= Frame(rootwidth=230,height=132,bg="#282829")
firstFrame.place(x=35,y=315)

day1=Label(firstFrame,font=("arial",20),bg="#282829",fg="white")
day1.place(x=100,y=5)

firstimage=Label(firstFrame,bg="#282829")
firstimage.place(x=1,y=15)

day1temp=Label(firstFrame,font=("arial",15),bg="#282829",fg="white")
day1temp.place(x=100,y=50)

#second cell
secondFrame= Frame(rootwidth=70,height=115,bg="#282829")
secondFrame.place(x=305,y=325)

day2=Label(firstFrame,font=("arial",20),bg="#282829",fg="white")
day2.place(x=100,y=5)

secondimage=Label(secondFrame,bg="#282829")
secondimage.place(x=7,y=20)

day2temp=Label(secondFrame,font=("arial",15),bg="#282829",fg="white")
day2temp.place(x=100,y=50)

#third cell
thirdFrame= Frame(rootwidth=230,height=132,bg="#282829")
thirdFrame.place(x=405,y=325)

day3=Label(firstFrame,font=("arial",20),bg="#282829",fg="white")
day3.place(x=100,y=5)

thirdimage=Label(thirdFrame,bg="#282829")
thirdimage.place(x=7,y=20)

day3temp=Label(thirdFrame,font=("arial",15),bg="#282829",fg="white")
day3temp.place(x=10,y=70)

#fouth cell
fouthFrame= Frame(rootwidth=230,height=132,bg="#282829")
fouthFrame.place(x=505,y=315)

day4=Label(firstFrame,font=("arial",20),bg="#282829",fg="white")
day4.place(x=100,y=5)

forthimage=Label(fouthFrame,bg="#282829")
forthimage.place(x=7,y=20)

day4temp=Label(fouthFrame,font=("arial",15),bg="#282829",fg="white")
day4temp.place(x=10,y=70)

#fifth cell
fifthFrame= Frame(rootwidth=230,height=132,bg="#282829")
fifthFrame.place(x=605,y=315)

day5=Label(firstFrame,font=("arial",20),bg="#282829",fg="white")
day5.place(x=100,y=5)

fifthimage=Label(fifthFrame,bg="#282829")
fifthimage.place(x=7,y=20)

day5temp=Label(fifthFrame,font=("arial",15),bg="#282829",fg="white")
day5temp.place(x=10,y=70)

#sixth cell
sixthFrame= Frame(rootwidth=230,height=132,bg="#282829")
sixthFrame.place(x=705,y=315)

day6=Label(firstFrame,font=("arial",20),bg="#282829",fg="white")
day6.place(x=100,y=5)

sixthimage=Label(sixthFrame,bg="#282829")
sixthimage.place(x=7,y=20)

day6temp=Label(sixthFrame,font=("arial",15),bg="#282829",fg="white")
day6temp.place(x=10,y=70)

#seventh cell
seventhFrame= Frame(rootwidth=230,height=132,bg="#282829")
seventhFrame.place(x=805,y=315)

day7=Label(firstFrame,font=("arial",20),bg="#282829",fg="white")
day7.place(x=100,y=5)

seventhimage=Label(seventhFrame,bg="#282829")
seventhimage.place(x=7,y=20)

day7temp=Label(seventhFrame,font=("arial",15),bg="#282829",fg="white")
day7temp.place(x=10,y=70)




root.mainloop()
