# Flash Cards - German Learning App

A simple flashcard application built with Python and Tkinter to help learn German vocabulary through active recall and repetition.

This project was built as part of my Python learning journey and combines GUI development, data handling, timers, and file persistence.

---

## Features

* Display random German words from a CSV file
* Automatically flip cards after 3 seconds
* Show the English translation on the back of the card
* Mark words as known
* Save learning progress between sessions
* Load previously saved progress automatically

---

## What I practiced

* Tkinter GUI development
* Working with Canvas widgets
* Using images in Tkinter
* Event handling with buttons
* Timers using `after()` and `after_cancel()`
* Reading CSV files with Pandas
* Converting DataFrames to dictionaries
* File persistence
* Exception handling with `try` and `except`
* Managing application state with global variables
* Working with lists and dictionaries

---

## Project structure

```

main.py

data/
├── german_words.csv
├── words_to_learn.csv

images/
├── card_front.png
├── card_back.png
├── right.png
└── wrong.png

```

---

## How to run

Run the project with:

`bash
python main.py
`

---

## Technologies used

* Python
* Tkinter
* Pandas
* CSV files

---

## Note

This project was created as part of my Python learning journey through Angela Yu’s Udemy course.

The application keeps track of learned words and removes them from future study sessions, allowing progress to persist between runs.

---

## Author

Alex — Aspiring Python developer improving step by step through daily practice and small projects.
