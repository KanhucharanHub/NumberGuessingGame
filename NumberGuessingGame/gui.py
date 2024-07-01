import tkinter as tk
from tkinter import messagebox, simpledialog
import pygame
from game_logic import NumberGuessingGame

class PowerUp:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect
class NumberGuessingApp:
    def __init__(self, leaderboard):
        self.game = NumberGuessingGame()
        self.leaderboard = leaderboard
        self.root = tk.Tk()
        self.root.title("Number Guessing Game")
        self.root.geometry("400x400")
        self.root.configure(bg='#282c34')
        pygame.mixer.init()
        self.create_widgets()
        self.available_powerups = [
            PowerUp("Narrow Range", self.narrow_range),
            PowerUp("Double Points", self.double_points),
            PowerUp("Second Chance", self.second_chance)
        ]
        self.active_powerup = []

    def narrow_range(self):
        self.hint_range = max(1, self.hint_range // 2)

    def double_points(self):
        self.score_multiplier *= 2

    def second_chance(self):
        self.guess_count = max(0, self.guess_count - 1)

    def use_powerup(self, powerup_name):
        for powerup in self.available_powerups:
            if powerup.name == powerup_name:
                powerup.effect()
                self.active_powerups.append(powerup)
                self.available_powerups.remove(powerup)
                return f"Power-up {powerup_name} activated!"
        return "Power-up not found."

    def create_widgets(self):
        self.instructions = tk.Label(self.root, text="Guess a number between 1 and 100", fg='#61dafb', bg='#282c34', font=('Helvetica', 14))
        self.instructions.pack(pady=10)

        self.entry = tk.Entry(self.root, font=('Helvetica', 14))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess, bg='#61dafb', fg='#282c34', font=('Helvetica', 14))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", fg='#ffffff', bg='#282c34', font=('Helvetica', 14))
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game, bg='#ff6f61', fg='#282c34', font=('Helvetica', 14))
        self.reset_button.pack(pady=10)

        self.leaderboard_button = tk.Button(self.root, text="Leaderboard", command=self.show_leaderboard, bg='#ff6f61', fg='#282c34', font=('Helvetica', 14))
        self.leaderboard_button.pack(pady=10)

        self.difficulty_button = tk.Button(self.root, text="Difficulty", command=self.set_difficulty, bg='#ff6f61', fg='#282c34', font=('Helvetica', 14))
        self.difficulty_button.pack(pady=10)

    def play_sound(self, sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            result = self.game.check_guess(guess)
            self.result_label.config(text=result)
            if "Too low" in result:
                self.play_sound('assets/sounds/low.wmp3')
            elif "Too high" in result:
                self.play_sound('assets/sounds/high.mp3')
            elif "Congratulations" in result:
                self.play_sound('assets/sounds/success.mp3')
                name = simpledialog.askstring("Name", "Enter your name for the leaderboard:")
                if name:
                    self.leaderboard.add_score(name, self.game.score)
                messagebox.showinfo("Result", result)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def reset_game(self):
        self.game.reset()
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

    def show_leaderboard(self):
        scores = self.leaderboard.get_leaderboard()
        leaderboard_text = "\n".join([f"{entry['name']}: {entry['score']}" for entry in scores])
        messagebox.showinfo("Leaderboard", leaderboard_text)

    def set_difficulty(self):
        difficulty = simpledialog.askstring("Difficulty", "Enter difficulty (easy, medium, hard):")
        self.game = NumberGuessingGame(difficulty)
        self.reset_game()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NumberGuessingApp()
    app.run()
