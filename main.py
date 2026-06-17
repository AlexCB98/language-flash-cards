import tkinter as tk
import pandas

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 50, 'Italic')
WORD_FONT = ('Arial', 60, 'Bold')

window = tk.Tk()
window.title('Flashcards - German/English')
window.minsize(width=900, height=640)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = tk.PhotoImage(file='images/card_front.png')
canvas.create_image(400, 265, image=card_front)
canvas.grid(row= 0, column= 0, columnspan= 2)

right_button_image = tk.PhotoImage(file= 'images/right.png')
wrong_button_image = tk.PhotoImage(file= 'images/wrong.png')

right_button = tk.Button(image= right_button_image, highlightthickness= 0)
right_button.grid(row= 1, column= 1)

wrong_button = tk.Button(image= wrong_button_image, highlightthickness= 0)
wrong_button.grid(row= 1, column= 0)


window.mainloop()