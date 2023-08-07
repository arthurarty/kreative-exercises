import tkinter as tk

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
