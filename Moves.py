import csv
import ast

moves_filename = 'moves-data.csv'


class Moves:

    def __init__(self, name: str, type: str, category: str, contest: str, pp: int, power: int, accuracy: int):
        self.name = name
        self.type = type
        self.category = category
        self.contest = contest
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.is_used = False
        self.current_pp = pp

    def __str__(self):
        return (f"{self.name} ({self.type}) - {self.category} - {self.pp} PP - {self.power} Power -"
                f" {self.accuracy} Accuracy")

    def use(self):
        self.is_used = True
        self.current_pp -= 1

    def reset(self):
        self.is_used = False
        self.current_pp = self.pp


def load_moves() -> list[Moves]:
    moves = []
    try:
        with open(moves_filename, 'r') as file:
            reader = csv.DictReader(file)
            next(reader)
        for row in reader:
            moves.append(Moves(row[0], row[1], row[2], row[3], int(row[4]),
                        int(row[5]), int(row[6])))
    except FileNotFoundError:
        print(f"File {moves_filename} not found")
    return moves
