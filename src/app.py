from dataclasses import dataclass
from enum import Enum

class States(Enum):
    EMPTY = '_'
    X = 'X'
    O = '0'

@dataclass
class Player:
    name: str
    state: States


class Field:
    def __init__(self) -> None:
        row = [States.EMPTY, States.EMPTY, States.EMPTY]
        self.matrix = [row for _ in range(3)]

    def __str__(self) -> str:
        return "\n\n".join(
            ["  ".join([str(item) for item in row]) for row in self.matrix]
        )

    def turn(self, state, x, y):
        pass

    def is_game_finished(self):
        pass

    def validate_input(self, state, x, y):
        pass

def game_loop():
    pass

if __name__ == "__main__":
    first_player_name = input("Please, type first player's name (X)")
    second_player_name = input("Please, type first player's name (0)")
    player1 = Player(first_player_name, States.X)
    player2 = Player(second_player_name, States.O)
    field = Field()
    winner = player1
    current_player = player1
    #while not field.is_game_finished():

    print(f'Player {current_player.name}, please make your choice')
    if winner:
        print(f'The winner is {player1}')
    else:
        print('Draw!')
