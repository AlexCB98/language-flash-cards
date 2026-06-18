import tkinter as tk
import pandas
import random

data = pandas.read_csv('data/german_words.csv')
words = data.to_dict(orient= 'records')
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text= 'German', fill= 'black')
    canvas.itemconfig(card_word, text= current_card['German'], fill= 'black')
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text= 'English', fill= 'white')
    canvas.itemconfig(card_word, text= current_card['English'], fill= 'white')
    canvas.itemconfig(card_background, image= card_back_image)

window = tk.Tk()
window.title('Flashcards - German/English')
window.minsize(width=900, height=640)
window.config(padx=50, pady=50, bg="#B1DDC6")

flip_timer = window.after(3000, func= flip_card)

canvas = tk.Canvas(width=800, height=530)
card_front_image = tk.PhotoImage(file='images/card_front.png')
card_back_image = tk.PhotoImage(file= 'images/card_back.png')
card_background = canvas.create_image(400, 265, image=card_front_image)

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