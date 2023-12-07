import tkinter as tk
import ttkbootstrap as ttk

def convert():
    """
    Converts miles to kilometers and updates the output label.
    """
    # Get the mile input from the entry widget
    mile_input = entry_int.get()

    # Convert miles to kilometers and round to 2 decimal places
    km_output = round(mile_input * 1.61, 2)

    # Update the output label with the result
    output_string.set(km_output)

# Create a Tkinter window using ttkbootstrap theme
window = ttk.Window(themename='simplex')
window.title("Demo")
window.geometry('300x150')

# Create and pack the title label
title_label = ttk.Label(master=window, text="Miles to kilometers", font="Calibri 24 bold")
title_label.pack()

# Create an input frame to hold the entry widget and button
input_frame = ttk.Frame(window)

# Variable to store the mile input from the entry widget
entry_int = tk.IntVar()

# Create entry widget and button, and pack them into the input frame
entry = ttk.Entry(input_frame, textvariable=entry_int)
button = ttk.Button(input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=10)
button.pack()

# Pack the input frame into the window with some padding
input_frame.pack(pady=10)

# Variable to store the converted kilometers for output label
output_string = tk.StringVar()

# Create and pack the output label
output_label = ttk.Label(window, text="Output", textvariable=output_string, font="Calibri 24 bold")
output_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
