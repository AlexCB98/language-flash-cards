import tkinter as tk
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title('Flashcards - German/English')
window.minsize(width=1000, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = tk.PhotoImage(file='images/card_front.png')
canvas.create_image(400, 265, image=card_front)
canvas.pack()

window.mainloop()