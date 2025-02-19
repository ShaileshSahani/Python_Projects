import mysql.connector
from tkinter import messagebox as msg
from tkinter import *
from tkinter import messagebox as m
from datetime import datetime
import requests
import pytz
import timezonefinder
from geopy.geocoders import Nominatim

def control():
    try:
        root1 = Tk()
        root1.title('Weather App')
        root1.wm_minsize(1100, 800)
        root1.wm_maxsize(1100, 800)

        def getWeather():
            try:
                city = text.get()
                geolocator = Nominatim(user_agent='geoapiExercises')
                location = geolocator.geocode(city)
                o = timezonefinder.TimezoneFinder()
                result = o.timezone_at(lng=location.longitude, lat=location.latitude)
                print(result)

                home = pytz.timezone(result)
                local_time = datetime.now(home)
                current_time = local_time.strftime('%I : %M %p')
                clock.config(text=current_time)
                n.config(text='CURRENT WEATHER')

                data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city +
                                    "&appid=8c5483ca81e4064fd0c7bb62bca9b8b3").json()
                temp = int(data['main']['temp'] - 273.15)
                condition = data['weather'][0]['main']
                w.config(text=data['wind']['speed'])
                h.config(text=data['main']['humidity'])
                d.config(text=data['weather'][0]['description'])
                p.config(text=data['main']['pressure'])

                temp1.config(text=f"{temp} °")
                con.config(text=f'{condition} | FEELS LIKE {temp}°')

            except Exception as e:
                m.showerror(title='Weather app', message='Invalid Entry')
                print(e)

        c1 = Canvas(root1, height=800, width=1100, bg='powder blue')
        c1.grid()

        label = Label(root1, text='WEATHER APP', font=('comic sans', 25, 'bold'), bg='deepskyblue2', fg='black', bd=7,
                      relief='raised', padx=30, pady=10, width=19)
        label.place(x=270, y=10)

        label1 = Label(root1, text='Enter the City Name Here', fg='black', bg='powder blue', font=('bold', 19))
        label1.place(x=100, y=150)

        searchBar = PhotoImage(file="search_bar.png")
        search_bar = Label(image=searchBar, width=300, bg="powder blue")
        search_bar.place(x=100, y=190)
        text = Entry(root1, justify="center", width=17, font=("poppins", 18, "bold"), bg="#147886", border=0,
                     fg="white")
        text.place(x=120, y=200)
        text.focus()

        icon = PhotoImage(file="search_icon.png")
        search_icon = Button(image=icon, borderwidth=0, cursor="hand2", bg="#147886", command=getWeather)
        search_icon.place(x=350, y=200)

        imageLogo = PhotoImage(file="weather_logo1.png")
        weather_logo1 = Label(image=imageLogo, bg='powder blue')
        weather_logo1.place(x=450, y=230)

        imageBox = PhotoImage(file="information_box2.png")
        information_box = Label(image=imageBox, padx=10, pady=10, bg='powder blue')
        information_box.place(x=100, y=570)

        n = Label(root1, font=('arial', 23, 'bold'), bg='powderblue')
        n.place(x=90, y=280)
        clock = Label(root1, font=('Merriweather', 23), bg='powderblue')
        clock.place(x=150, y=330)

        # Label
        wind = Label(root1, text="WIND", font=("Merriweather", 20, "bold"), fg="black", bg="#5AC9D9")
        wind.place(x=140, y=576)

        humidity = Label(root1, text="HUMIDITY", font=("Merriweather", 20, "bold"), fg="black", bg="#5AC9D9")
        humidity.place(x=290, y=576)

        description = Label(root1, text="DESCRIPTION", font=("Merriweather", 20, "bold"), fg="black", bg="#5AC9D9")
        description.place(x=490, y=576)

        pressure = Label(root1, text="PRESSURE", font=("Merriweather", 20, "bold"), fg="black", bg="#5AC9D9")
        pressure.place(x=790, y=576)

        temp1 = Label(root1, text="", font=("arial", 50, "bold"), fg="#ee666d", bg='powder blue')
        temp1.place(x=750, y=300)
        con = Label(font=("arial", 20, "bold"), bg='powder blue')
        con.place(x=700, y=400)

        w = Label(text="...", font=("arial", 16, "bold"), bg="#5AC9D9")
        w.place(x=160, y=630)
        h = Label(text="...", font=("arial", 16, "bold"), bg="#5AC9D9")
        h.place(x=350, y=630)
        d = Label(text="...", font=("arial", 16, "bold"), bg="#5AC9D9")
        d.place(x=540, y=630)
        p = Label(text="...", font=("arial", 16, "bold"), bg="#5AC9D9")
        p.place(x=850, y=630)

        root1.mainloop()
    except Exception as e:
        print(e)
try:
    db = mysql.connector.connect(host='localhost', user='root', password='root')
    cu = db.cursor()
    database = []
    cu.execute("SHOW databases")
    for i in cu:
        database.append(i[0])
    if 'login' in database:
        cu.execute('USE login')
    else:
        cu.execute('CREATE DATABASE login')
        cu.execute("USE login")

    table = []
    cu.execute('SHOW tables')
    for i in cu:
        table.append(i[0])
    if 'info' in table:
        pass
    else:
        cu.execute("create table info(USER_NAME char(30) primary key not null,PASSWORD varchar(20))")

except Exception as e:
    print(e)


try:
    root = Tk()
    root.title('Login Page')
    root.wm_minsize(400, 500)
    root.wm_maxsize(400, 500)


    def login():
        user1 = 'insert into info values(%s,%s)'
        u = u1.get()
        p = p1.get()

        cu.execute('select * from info')
        d1 = []
        for dt in cu:
            d1.append(dt[0])
        if u == '' and p == '':
            msg.showerror(message='Fields cannot be empty!!')
        elif u == '':
            msg.showerror(message='Username cannot be empty')
        elif p == '':
            msg.showerror(message='Password cannot be empty')
        else:
            value = msg.askyesno(message='Submit info')
            if value is True:
                user2 = (u, p)
                try:
                    cu.execute(user1, user2)
                    db.commit()
                    cu.execute('Select * from info')
                    for dt in cu:
                        print(dt)
                    print('\n\n')
                    root.destroy()
                    control()
                except Exception as e:
                    db.rollback()
                    print(e)
            elif value is False:
                val = msg.askokcancel(message="Do You want To Exit")
                if val is True:
                    db.close()
                    root.destroy()
    c = Canvas(root, height=500, width=400,  bg='lightskyblue')
    c.grid()

    login1 = Label(root, text='LOGIN FORM', fg='black', font=('Arial', 20, 'bold'), borderwidth=2, relief='solid' , bg='lightblue')
    login1.place(x=110,y=30)

    user = Label(root, text='Username', font=('Arial', 20), borderwidth=2, relief='solid', bg='snow3')
    user.place(x=19, y=120)
    u1 = StringVar()
    entry1 = Entry(root, textvariable=u1, font=('Arial', 20), borderwidth=2, relief='solid')
    entry1.place(x=19, y=170)

    password = Label(root, text='Password', font=('Arial', 20), borderwidth=2, relief='solid', bg='snow3')
    password.place(x=19, y=250)
    p1 = StringVar()
    entry2 = Entry(root, show='*', textvariable=p1, font=('Arial', 20), borderwidth=2, relief='solid')
    entry2.place(x=19, y=300)

    button = Button(root, text='Login', fg='red', bg='grey', command=login, width=10, font=15, bd=10)
    button.place(x=50., y=370)

    root.mainloop()

except Exception as e:
    print(e)