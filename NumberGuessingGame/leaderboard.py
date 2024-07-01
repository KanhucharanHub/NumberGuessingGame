import json

class Leaderboard:
    def __init__(self, filename='leaderboard.json'):
        self.filename = filename
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                self.leaderboard = json.load(file)
        except FileNotFoundError:
            self.leaderboard = []

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.leaderboard, file)

    def add_score(self, name, score):
        self.leaderboard.append({'name': name, 'score': score})
        self.leaderboard.sort(key=lambda x: x['score'], reverse=True)
        self.leaderboard = self.leaderboard[:10]
        self.save()

    def get_leaderboard(self):
        return self.leaderboard
