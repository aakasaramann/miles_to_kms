from tkinter import *


def button_clicked():
    new_text_in_km = str(round(float(miles_input.get()) * 1.609))
    output_label.config(text=new_text_in_km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_to_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

output_label = Label(text="0", font=("Arial", 12, "bold"))
output_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
