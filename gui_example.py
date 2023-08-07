import tkinter as tk
import requests


def get_weather(api_query: str = 'Kampala,ug'):
    url = f"api.openweathermap.org/data/2.5/weather?q={api_query}&APPID={{key}}"
    response = requests.request("GET", url, headers={}, data={})
    print(response.text)
    return None


border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}


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


frame = tk.Frame(master=window, relief=border_effects['sunken'], borderwidth=5)
frame.pack()
label_frame = tk.Label(master=frame, text='Flat', width=120)
label_frame.pack()

window.mainloop()

