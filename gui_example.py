import tkinter as tk
import requests


def get_weather(api_query: str = 'Kampala,ug'):
    url = f"api.openweathermap.org/data/2.5/weather?q={api_query}&APPID={{key}}"
    response = requests.request("GET", url, headers={}, data={})
    print(response.text)
    return None


window = tk.Tk()
greeting = tk.Label(
    text='Python rocks!',
    foreground="red",
    width=30,
    height=15,
)
greeting.pack()


button = tk.Button(
    text="Click here!",
    width=40,
    height=15,
    bg="blue",
    fg="white",
)
button.pack()
window.mainloop()
