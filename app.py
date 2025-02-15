import tkinter as tk
import game_logic as gl 

def update_ui():
    word_display.set(gl.update_display_word())
    attempts_label.config(text=f"Attempts left: {gl.attempts}")

def check_letter(event):
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    message = gl.check_letter(letter)
    message_label.config(text=message)

    update_ui()

    if gl.is_won():
        message_label.config(text="You won!")
    elif gl.is_lost():
        message_label.config(text=f"Game Over! Word was: {gl.word}")

def restart_game():
    gl.initialize_game()
    message_label.config(text="")
    update_ui()

# GUI setup
root = tk.Tk()
root.title("Hangman Game")

word_display = tk.StringVar()

label = tk.Label(root, textvariable=word_display, font=("Arial", 20))
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()
entry.bind("<Return>", check_letter)

message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts left: {gl.attempts}", font=("Arial", 14))  
attempts_label.pack()

restart_button = tk.Button(root, text="Restart", command=restart_game, font=("Arial", 14))
restart_button.pack(pady=10)

update_ui()

root.mainloop()
