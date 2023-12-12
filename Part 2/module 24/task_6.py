# Создайте программу, которая реализует игру «Крестики-нолики».
#
# Для этого напишите:

from enum import Enum
import random

class Cell_symbol(Enum):
    empty = 1
    cross = 2
    zero = 3


# 1. Класс, который будет описывать поле игры.
class Board:

    def __init__(self):
        self.board = [Cell(num) for num in range(9)]

    def change_cell_status(self, num, cell_symbol):
        if self.board[num].get_cur_symbol() == Cell_symbol.empty:
            self.board[num].occupy_cell(cell_symbol)
            return True
        return False

    def check_win(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in winning_combinations:
            if (self.board[combo[0]].symbol == self.board[combo[1]].symbol == self.board[combo[2]].symbol) and (
                    self.board[combo[0]].symbol != Cell_symbol.empty):
                return True
        return False


# 2. Класс, который будет описывать одну клетку поля:
class Cell:

    def __init__(self, num):
        self.num = num
        self.symbol = Cell_symbol.empty
        self.is_occupied = False

    def occupy_cell(self, cell_symbol):
        self.is_occupied = True
        self.symbol = cell_symbol

    def is_occupied(self):
        return self.is_occupied

    def get_cur_symbol(self):
        return self.symbol


# 3. Класс, который описывает поведение игрока:
class Player:

    def __init__(self, name):
        self.name = name
        self.count_victories = 0

    def make_move(self):
        return random.randint(0,8)

    def write_victory(self):
        self.count_victories += 1

    def get_count_victories(self):
        return self.count_victories

    def __str__(self):
        return f'Имя: {self.name}, Количество побед: {self.count_victories}.'

# 4. Класс, который управляет ходом игры:
class Game:

    def __init__(self, player1, player2):
        self.players = {player1: Cell_symbol.cross,
                        player2: Cell_symbol.zero}
        self.is_finish = False
        self.board = Board()

    def make_move(self, player, cell_symbol):
        num_cell = int(input(f'{player.name}, ваш ход: ')) - 1
        for move in range(9):
            if self.board.change_cell_status(num_cell, cell_symbol):
                return True
        return False

    def start_session(self):
        self.board = Board()
        while True:
            for player in self.players:
                if self.make_move(player, self.players[player]):
                    if self.board.check_win(): return player
                else: return None

    def start_game(self):
        while True:
            print('Игра началась!')
            win_player = self.start_session()
            print('Игра окончилась!')
            if win_player != None:
                print(f'Победитель {win_player.name}! Поздравим его.')
                win_player.write_victory()
            else:
                print('Результат - Ничья!')

            print(f'{self.players.popitem()[0]}\n{self.players.popitem()[0]}')

            is_continue = int(input('Хотите продолжить? (1 - да, 0 - нет): '))

            if not is_continue:
                print('Конец!')
                break

player1 = Player('Tom')
player2 = Player('Jack')
game = Game(player1, player2)
game.start_game()