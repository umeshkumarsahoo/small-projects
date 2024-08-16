from tkinter import *
import requests as req
import random

# Function to get a random quote
def get_quote():
    try:
        response = req.get(url="https://api.quotable.io/random")
        response.raise_for_status()  # Raise an error for bad status codes
        response = req.get("https://zenquotes.io/api/random")
        data = response.json()

        quote = data[0]['q'] # Extracting the quote from the JSON response
        canvas.itemconfig(quote_text, text=quote)
    except req.exceptions.RequestException as e:
        canvas.itemconfig(quote_text, text="Failed to retrieve quote. Check your connection.")


# Setup window
window = Tk()
window.title("Quote Generator")
window.geometry("600x600")

# Background image setup
bg_img = PhotoImage(file="back.png")
bg_label = Label(window, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Canvas setup
canvas = Canvas(window, width=500, height=200, bg="white", highlightthickness=0)
canvas.grid(row=0, column=0, padx=50, pady=30)
quote_text = canvas.create_text(250, 100, text="Quote goes here", width=400, font=("Arial", 18, "bold"),fill="black")

# Button setup
meow_img = PhotoImage(file="cat.png")
btn = Button(image=meow_img, highlightthickness=0, command=get_quote)
btn.grid(row=1, column=0)

window.mainloop()
