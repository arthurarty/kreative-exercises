import tkinter as tk

window = tk.Tk()
greeting = tk.Label(
    text='Python rocks!',
    foreground="red",
    width=30,
    height=15,
)
greeting.pack()
window.mainloop()
