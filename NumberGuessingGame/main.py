import pygame
from gui import NumberGuessingApp
from leaderboard import Leaderboard

def main():
    leaderboard = Leaderboard()
    app = NumberGuessingApp(leaderboard)
    app.run()

if __name__ == "__main__":
    main()
