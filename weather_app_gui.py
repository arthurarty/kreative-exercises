import os
import tkinter as tk
import requests
from dotenv import load_dotenv
from functools import partial
from datetime import datetime
from PIL import ImageTk, Image


# Assumes you have created a .env file with SMTP_USER and SMTP_PASSWORD
load_dotenv()  # take environment variables from .env.


OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')


def convert_kelvin_to_celsius(kelvin_temp: float):
    return kelvin_temp - 273.15


def get_weather(api_query: str = 'Kampala,ug') -> requests.Response:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={api_query}&APPID={OPEN_WEATHER_API_KEY}"
    return requests.request("GET", url, headers={}, data={})


def handle_button_click(tk_frame: tk.Frame, event):
    """
    Clicking the button triggers an api request to the Open Weather API
    Picks weather details and creates a new label widget with the details.
    """
    weather_resp = get_weather()
    weather_details = weather_resp.json()
    city = weather_details.get('name')
    weather = weather_details.get('weather')[0].get('main')
    temp = weather_details.get('main').get('temp')
    lbl_time = tk.Label(
        master=tk_frame,
        text=f"Date & Time: {datetime.now()}"
    )
    lbl_time.pack()
    lbl_weather_output = tk.Label(
        master=tk_frame,
        text=f"City: {city}, weather: {weather}, temp: {temp} Kelvin/ {convert_kelvin_to_celsius(temp):.2f} celsius"
    )
    lbl_weather_output.pack()
    return None


window = tk.Tk()

frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frame.pack()

label_frame = tk.Label(master=frame, text='Weather Application. Click button to get current weather', width=60)
label_frame.pack(side=tk.LEFT)

image = Image.open("storm.png")
photo = ImageTk.PhotoImage(image)
label_photo = tk.Label(master=frame, image=photo)
label_photo.pack(side=tk.LEFT)


second_frame = tk.Frame(master=window, borderwidth=5)
second_frame.pack()


button = tk.Button(
    master=second_frame,
    text="Fetch Weather!",
    width=40,
    height=2,
    bg="blue",
    fg="white",
)
button.pack()
button.bind("<Button-1>", partial(handle_button_click, second_frame))


window.mainloop()
