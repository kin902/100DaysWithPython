import time
import tkinter as tk

window = tk.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)
my_label = tk.Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.pack()

Input = tk.Entry(width=10)
Input.pack()


def button_clicked():
    """
    my_label.config(text="I got clicked")
    window.update()
    time.sleep(1)
    my_label.config(text="I'm a label")
    window.update()
    """
    my_label.config(text=Input.get())


button = tk.Button(text="Click Me", command=button_clicked)

button.pack()

window.mainloop()

"""
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(6, 34, 7, 4, 79, 4, 6, 8))


def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


calculate(a=6, b=4, c=7)
"""
