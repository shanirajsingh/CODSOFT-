import tkinter as tk
import ttkbootstrap
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

#FUNCTIONS

def get_weather(city):
    try:
        API_KEY = "a1035dc252249594a43e3e60977082c7"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        res = requests.get(url)

        if res.status_code == 404:
            messagebox.showerror("Error", "City not found")
            return None
        # get weather information
        weather = res.json()
        icon_id = weather['weather'][0]['icon']
        location_label.configure(text=f"{weather['name']},{weather['sys']['country']}")
        temperature_label.configure(text=f"Temperature: {weather['main']['temp'] - 273.15:.2f}°C")
        feels_like_label.configure(text=f"FeelsLike: {weather['main']['feels_like'] - 273.15:.2f}°C")
        description_label.configure(text=f"Description: {weather['weather'][0]['description']}")
        min_label.configure(text=f"Minimum Temperature: {weather['main']['temp_min'] - 273.15:.2f}°C")
        max_label.configure(text=f"Maximum Temperature: {weather['main']['temp_max'] - 273.15:.2f}°C")
        pressure_label.configure(text=f"Pressure: {str(weather['main']['pressure'])}")
        humidity_label.configure(text=f"Humidity: {str(weather['main']['humidity'])}%")
        wind_label.configure(text=f"Wind: {str(weather['wind']['speed'])}km/h")
        
        # icon for weather
        icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
        image = Image.open(requests.get(icon_url, stream=True).raw)
        img = image.resize((130, 130))
        icon = ImageTk.PhotoImage(img)
        icon_label.configure(image=icon)
        icon_label.image = icon

    except:
        messagebox.showerror("Error", "There was a problem retrieving that information")

def search():
    city = city_entry.get()
    if not city:
       return messagebox.showerror("Error", "Please enter a city name")   
    get_weather(city)

win = ttkbootstrap.Window(themename="superhero")
win.title("weather_forcast")
win.geometry("500x650")

heading = tk.Label(win, text="Weather App", font="Arial,30,bold")
heading.pack(pady=20, padx=130)

#  city names.
city_list=["Indore","Bhopal","Mumbai","Delhi","lucknow","Bangalore","Chennai","Pune"]
city_entry = ttkbootstrap.Combobox(win, font="helvetica,18",values=city_list)
city_entry.pack(pady=10)

# search button
search_btn = ttkbootstrap.Button(win, text="Search", command=search, bootstyle="SUCCESS")
search_btn.pack(pady=10)

# labels
location_label = tk.Label(win, font="helvetica,25")
location_label.pack(pady=15)

icon_label = tk.Label(win)
icon_label.pack()

temperature_label = tk.Label(win, font="helvetica,20")
temperature_label.pack()

feels_like_label = tk.Label(win, font="helvetica,20")
feels_like_label.pack()

description_label = tk.Label(win, font="helvetica,20")
description_label.pack()

min_label = tk.Label(win, font="helvetica,20")
min_label.pack()

max_label = tk.Label(win, font="helvetica,20")
max_label.pack()

pressure_label = tk.Label(win, font="helvetica,20")
pressure_label.pack()

humidity_label = tk.Label(win, font="helvetica,20")
humidity_label.pack()

wind_label = tk.Label(win, font="helvetica,20")
wind_label.pack()


win.mainloop()