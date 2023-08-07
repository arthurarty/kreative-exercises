import tkinter as tk



import requests

url = "api.openweathermap.org/data/2.5/weather?q=Kampala,ug&APPID={{key}}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


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
