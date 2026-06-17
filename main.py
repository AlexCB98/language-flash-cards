import tkinter as tk
import pandas
import random

data = pandas.read_csv('data/german_words.csv')
words = data.to_dict(orient= 'records')

def next_card():
    card = random.choice(words)
    canvas.itemconfig(card_title, text= 'German')
    canvas.itemconfig(card_word, text= card['German'])


window = tk.Tk()
window.title('Flashcards - German/English')
window.minsize(width=900, height=640)
window.config(padx=50, pady=50, bg="#B1DDC6")

canvas = tk.Canvas(width=800, height=530)
card_front_image = tk.PhotoImage(file='images/card_front.png')
canvas.create_image(400, 265, image=card_front_image)

card_title = canvas.create_text(400, 100, text= '', font= ('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 265, text= '', font= ('Arial', 70, 'bold'))

canvas.config(highlightthickness=0, bg="#B1DDC6")
canvas.grid(row= 0, column= 0, columnspan= 2)

right_button_image = tk.PhotoImage(file= 'images/right.png')
wrong_button_image = tk.PhotoImage(file= 'images/wrong.png')

right_button = tk.Button(image= right_button_image, highlightthickness= 0, command= next_card)
right_button.grid(row= 1, column= 1)

wrong_button = tk.Button(image= wrong_button_image, highlightthickness= 0, command= next_card)
wrong_button.grid(row= 1, column= 0)

next_card()


window.mainloop()