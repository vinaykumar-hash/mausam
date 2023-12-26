import requests
import json
from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time

API_KEY = "f8ab625482b231795aa326ac377aaa6a"
base_url = "http://api.openweathermap.org/data/2.5/weather?"



def weathershow(city):
    try:
        if city == "" or city == "Enter City":
            city_label.config(text=f"Nothing to show ;)\nsearch your place")
            pressure_label.config(text= "")
            temperature_label.config(text=f"")
            wind_label.config(text=f"")
            pressure_label.config(text=f"")
            humidity.config(text=f"")
            sunset.config(text=f"")
            sunrise.config(text=f"")
        else:
            try:
                city_label.config(text=f"Fetching...")
                c_url = base_url + "appid=" + API_KEY + "&q=" + city
                response = requests.get(c_url)
                x = response.json()
                if x["cod"] != "404":
                    try:

                        # Update labels with weather information
                        city_label.config(text=f"{x['name']}, {x['sys']['country']}")
                        temperature_label.config(text=f"{round(x['main']['temp'] - 273.17)}°C"+f", {x['weather'][0]['main']}")
                        wind_label.config(text=f"Wind Speed: {round(x['wind']['speed'])} Km/h")

                        pressure_label.config(text=f"Pressure: {round(x['main']['pressure'])} mb")
                        humidity.config(text=f"Humidity: {round(x['main']['humidity'])}%")
                        sunrise.config(text=f"Sunrise: {datetime.utcfromtimestamp(x['sys']['sunrise'] + 5 * 3600 + 30 * 60)}")
                        sunset.config(text=f"Sunset: {datetime.utcfromtimestamp(x['sys']['sunset'] + 5 * 3600 + 30 * 60)}")
                    except:
                        pass
                else:
                    pressure_label.config(text= "")
                    city_label.config(text=f"Not Found :(")
                    temperature_label.config(text=f"")
                    wind_label.config(text=f"")
                    pressure_label.config(text=f"")
                    humidity.config(text=f"")
                    sunset.config(text=f"")
                    sunrise.config(text=f"")
            except:
                pass
    except:
        pass

def user():
    userr = user_entry.get()
    weathershow(userr)
    root.after(3000, user)
def on_entry_click(event):
    try:
        if user_entry.get() == 'Enter City':
            user_entry.delete(0, "end")
            user_entry.insert(0, '')
            user_entry.config(fg='black')
    except:
        pass

def on_focus_out(event):
    try:
        if user_entry.get() == '':
            user_entry.insert(0, 'Enter City')
            user_entry.config(fg='grey')
    except:
        pass

# Create the main application window
root = Tk()
root.title("Mausam")
root.configure(bg="white")
root.maxsize(500,600)
root.minsize(500,600)

style = ttk.Style()
style.configure("TEntry", borderwidth=10, relief="flat", padding=(20, 5))


input_frame = Frame(root, background="white")
input_frame.pack(pady=(0,20), fill="both", expand=True, padx=40)

user_entry = ttk.Entry(input_frame, style="TEntry", foreground='black', font=("Roboto", 12,"normal"))
user_entry.pack(side=LEFT, fill='x', expand=True, padx=(0, 5))
user_entry.insert(0, 'Enter City')
user_entry.bind('<FocusIn>', on_entry_click)
user_entry.bind('<FocusOut>', on_focus_out)



city_label = Label(root, text="Nothing to show ;)\nsearch your place", font=("Roboto", 20, "bold"), background="white", foreground="black")
city_label.pack(anchor='w', padx=40)

temperature_label = Label(root, text="", font=("Roboto", 20, "bold"), background="white", foreground="black")
temperature_label.pack(anchor='w', padx=40)

wind_label = Label(root, text="", font=("Roboto", 12, "bold"), background="white", foreground="#4d4d4d")
wind_label.pack(anchor='w', padx=40)

extra_info = Frame(root, background="#F2F2F2")
extra_info.pack(pady=(20,0), fill="both", expand=True)

pressure_label = Label(extra_info, text="", font=("Roboto", 12, "normal"), background="#F2F2F2", foreground="#4d4d4d")
pressure_label.pack(anchor='w', padx=40 , pady=(20,10))

humidity = Label(extra_info, text="", font=("Roboto", 12, "normal"), background="#F2F2F2", foreground="#4d4d4d")
humidity.pack(anchor='w', padx=40 , pady=10)

sunrise = Label(extra_info, text="", font=("Roboto", 12, "normal"), background="#F2F2F2", foreground="#4d4d4d")
sunrise.pack(anchor='w', padx=40 , pady=10)

sunset = Label(extra_info, text="", font=("Roboto", 12, "normal"), background="#F2F2F2", foreground="#4d4d4d")
sunset.pack(anchor='w', padx=40 , pady=(10,20))
user()

# Start the Tkinter event loop
root.mainloop()
