import csv
import ast
from Moves import Moves

pokemon_filename = 'pokemon-data.csv'


class Pokemon:

    def __init__(self, name: str, type: str, hp: int, attack: int, defense: int, height: int, weight: int,
                 current_hp: int, moves: list[Moves]):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.height = height
        self.weight = weight
        self.moves = moves
        self.current_hp = current_hp

    def __str__(self):
        return (f"{self.name} (Type - {self.type}) - {self.hp} HP - {self.attack} Attack - {self.defense} Defense - "
                f"{self.height} Height - {self.weight} Weight")

    def get_available_moves(self) -> list[Moves]:
        if all(move.is_used for move in self.moves):
            for move in self.moves:
                move.reset()
        return [move for move in self.moves if not move.is_used]

    def use_move(self, move: Moves, defender: 'Pokemon') -> int:
        if move.is_used:
            raise ValueError(f"This move has already been used")

        damage = self.calculate_damage(move, defender)

        move.use()

        return damage




def load_pokemon() -> list[Pokemon]:
    pokemon = []

    try:
        with open(pokemon_filename, 'r') as file:
            reader = csv.DictReader(file)
            next(reader)
        for row in reader:
            moves = ast.literal_eval(row[8])
            pokemon.append(Pokemon(row[0], row[1], int(row[2]), int(row[3]), int(row[4]),
                                   int(row[5]), int(row[6]), int(row[7]), moves))
    except FileNotFoundError:
        print(f"File {pokemon_filename} not found")
    return pokemon
