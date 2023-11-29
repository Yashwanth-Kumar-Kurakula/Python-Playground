import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = round(mile_input * 1.61, 2)
    output_string.set(km_output)

window = ttk.Window(themename= 'simplex')
window.title("Demo")
window.geometry('300x150')

title_label = ttk.Label(master = window, text = "Miles to kilometers", font = "Calibri 24 bold")
title_label.pack()

input_frame = ttk.Frame(window)
entry_int = tk.IntVar()
entry = ttk.Entry(input_frame, textvariable= entry_int)
button = ttk.Button(input_frame, text="Convert", command=convert)

entry.pack(side = "left", padx = 10)
button.pack()
input_frame.pack(pady=10)

output_string = tk.StringVar()
output_label = ttk.Label(window, text="Output", textvariable=output_string, font = "Calibri 24 bold")
output_label.pack(pady=10)

window.mainloop()
