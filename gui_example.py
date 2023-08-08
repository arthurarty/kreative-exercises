import os
import tkinter as tk
import requests
from dotenv import load_dotenv
from functools import partial


# Assumes you have created a .env file with SMTP_USER and SMTP_PASSWORD
load_dotenv()  # take environment variables from .env.


OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')


def get_weather(api_query: str = 'Kampala,ug'):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={api_query}&APPID={OPEN_WEATHER_API_KEY}"
    response = requests.request("GET", url, headers={}, data={})
    print(response.text)
    return None


def handle_button_click(tk_frame: tk.Frame, event):
    print('Event received, getting weather now')
    lbl_weather_output = tk.Label(master=tk_frame, text='The weather is')
    lbl_weather_output.pack()
    return get_weather()


window = tk.Tk()
frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frame.pack()
label_frame = tk.Label(master=frame, text='Weather Application. Click button to get weather', width=120)
label_frame.pack()

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
