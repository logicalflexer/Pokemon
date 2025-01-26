import Pokemon
import queue
import random

from Moves import Moves


class PokemonColosseum:
    def __init__(self):
        self.pokemon_data = {}
        self.moves_data = {}
        self.pokemon_moves_mapping = {}
        self.load_data()

    def load_data(self):
        self.moves_data = Moves.load_moves()
        self.pokemon_data = Pokemon.load_pokemon()

    def team_builder(self):
        team = []
        for _ in range(3):
            pokemon = random.choice(self.pokemon_data)
            team.append(pokemon)
        return team

    def calculate_damage(self: Pokemon, move: Moves, defender: Pokemon) -> int:
        type_matchup = {
            'Normal': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1},
            'Fire': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1, 'Grass': 2},
            'Water': {'Normal': 1, 'Fire': 2, 'Water': 0.5, 'Electric': 1, 'Grass': 0.5},
            'Electric': {'Normal': 1, 'Fire': 1, 'Water': 2, 'Electric': 0.5, 'Grass': 0.5},
            'Grass': {'Normal': 1, 'Fire': 0.5, 'Water': 2, 'Electric': 1, 'Grass': 0.5},
            'Others': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1}
        }
        stab = 1.5 if move.type == self.type else 1.0

        effectiveness = type_matchup.get(move.type, {}).get(defender.type, 1.0)

        random_factor = random.uniform(0.5, 1.0)

        damage = (move.power * (self.attack / defender.defense) * stab * effectiveness * random_factor)

        return int(damage + 0.5)




    def main(self):
        print("Welcome to Pokemon Colosseum!")
        print("Enter Player Name: ")
        player_name = input()
        team_rocket = self.team_builder()
        print(f"Team Rocket enters with {team_rocket}")
        team_player = self.team_builder()
        print(f"Team {player_name} enters with {team_player}")

