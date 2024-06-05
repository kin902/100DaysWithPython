from tkinter import *

window = Tk()
window.minsize(400, 200)
window.title(" Mile to Km Converter")
window.config(padx=30, pady=30)

label = Label(text="is equal to", font=("Courier", 16, "normal"))
label.grid(column=0, row=1)

mile = Label(text="Mile", font=("Courier", 16, "normal"))
mile.grid(column=2, row=0)

km = Label(text="Km", font=("Courier", 16, "normal"))
km.grid(column=2, row=1)

km_output = Label(text="0", font=("Courier", 16, "normal"))
km_output.grid(column=1, row=1)

mile_input = Entry(width=16, font=("Courier", 16, "normal"))
mile_input.grid(column=1, row=0)


def calculate_mile_into_km():
    km_output.config(text=int(mile_input.get()) * 1.6093, font=("Courier", 16, "normal"))


calculate_button = Button(text="Calculate", font=("Courier", 16, "normal"), command=calculate_mile_into_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
