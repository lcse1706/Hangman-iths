import random

WORDS = ["python", "tkinter", "developer", "hangman", "programming", "code", "computer", "software", "django", "javascript"]

HANGMAN_PICS = [
    r"""
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

guessed_letters = set()
attempts = 6
word = ""

def initialize_game():
    global word, guessed_letters, attempts
    word = random.choice(WORDS).lower()
    guessed_letters.clear()
    attempts = 6

def update_display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def check_letter(letter):
    global attempts

    if len(letter) != 1 or not letter.isalpha():
        return "Enter a single letter!"
    
    if letter in guessed_letters:
        return "You already guessed that letter!"

    guessed_letters.add(letter)

    if letter in word:
        return "Correct!"
    else:
        attempts -= 1
        return "Wrong!"

def get_hangman_stage():
    return HANGMAN_PICS[6 - attempts]

def is_won():
    return "_" not in update_display_word()

def is_lost():
    return attempts == 0

# Inicjalizacja gry na start
initialize_game()