import random

class NumberGuessingGame:
    def __init__(self, difficulty='medium'):
        self.difficulty = difficulty
        self.reset()
    
    def set_theme(self, theme):
        self.theme = theme
        if self.theme == 'space':
            self.max_range = 1000
            self.score_multiplier = 2
        elif self.theme == 'ocean':
            self.max_range = 500
            self.score_multiplier = 1.5
        else:
            self.max_range = 100
            self.score_multiplier = 1

    def reset(self):
        self.target = random.randint(1, 100)
        self.guess_count = 0
        self.score = 0
        self.set_difficulty()

    def set_difficulty(self):
        if self.difficulty == 'easy':
            self.hint_range = 10
        elif self.difficulty == 'hard':
            self.hint_range = 2
        else:
            self.hint_range = 5

    def check_guess(self, guess):
        self.guess_count += 1
        if guess < self.target:
            self.score -= 1
            return f"Too low! Try again. Hint: ±{self.hint_range}"
        elif guess > self.target:
            self.score -= 1
            return f"Too high! Try again. Hint: ±{self.hint_range}"
        else:
            self.score += 10
            return f"Congratulations! You've guessed it in {self.guess_count} tries with a score of {self.score}."
