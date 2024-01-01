import requests
from tkinter import *

def get_quote():
    """
    Function to fetch a Kanye West quote from the Kanye Rest API and update the displayed quote on the canvas.
    """
    # Send a GET request to the Kanye Rest API
    response = requests.get(url="https://api.kanye.rest")
    
    # Parse the response as JSON
    data = response.json()
    
    # Extract the quote from the JSON data
    temp_quote = data["quote"]
    
    # Update the displayed quote on the canvas
    canvas.itemconfigure(quote_text, text=temp_quote)

# Create the main Tkinter window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create a canvas to display background image and text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

# Create a text item on the canvas to display Kanye's quote
quote_text = canvas.create_text(150, 207, text="Click Kanye for Quotes", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Create a button with Kanye's image to trigger the quote fetching
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start the Tkinter event loop
window.mainloop()
