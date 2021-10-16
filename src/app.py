from dataclasses import dataclass
from enum import Enum


class States(Enum):
    EMPTY = "_"
    X = "X"
    O = "0"


@dataclass(frozen=True, eq=True)
class Player:
    name: str
    state: States


class Field:
    _cell_to_coordinates = {x + y * 3: (y, x) for x in range(3) for y in range(3)}

    def __init__(self) -> None:
        row = [States.EMPTY, States.EMPTY, States.EMPTY]
        self.matrix = [row.copy() for _ in range(3)]

    def __str__(self) -> str:
        return "\n\n".join(
            [
                "  ".join([str(item.value) for item in row])
                + "\n"
                + "  ".join(
                    [str(col_index + row_index * 3) for col_index in range(len(row))]
                )
                for row_index, row in enumerate(self.matrix)
            ]
        )

    def turn(self, state, cell_number):
        i, j = self._cell_to_coordinates[cell_number]
        self.matrix[i][j] = state

    def is_game_finished(self):
        return False

    def validate_input(self, cell_number_str):
        if not cell_number_str.isdigit():
            print("Invalid input. Please input a number from 0 to 8 (including).")
            return -1, False
        cell_number = int(cell_number_str)
        if not 0 <= cell_number <= 8:
            print("Invalid cell number. Please input a number from 0 to 8 (including).")
            return -1, False
        i, j = self._cell_to_coordinates[cell_number]
        if self.matrix[i][j] != States.EMPTY:
            print("Invalid cell value. The call is already set.")
            return -1, False
        return cell_number, True


def game_step(field, player):
    while True:
        cell_number_str = input(
            f"Player {player.name} ({player.state}), please choice a number of cell > "
        )
        cell_number, valid = field.validate_input(cell_number_str)
        if valid:
            field.turn(player.state, cell_number)
            print(field)
            break


def game_loop(field, player1, player2):
    winner = None
    players = {player1, player2}
    current_player = player1

    while not field.is_game_finished():
        game_step(field, current_player)
        # Changing a current player
        current_player = (players - {current_player}).pop()

    if winner:
        print(f"The winner is {player1}")
    else:
        print("Draw!")


if __name__ == "__main__":
    first_player_name = input("Please, type first player's name (X) > ")
    second_player_name = input("Please, type first player's name (0) > ")
    player1 = Player(first_player_name, States.X)
    player2 = Player(second_player_name, States.O)
    field = Field()
    print(field)
    game_loop(field, player1, player2)
