from __future__ import annotations  # avoids issues with forward references i.e we can use a refernce to class without any error even when it's not created 
from abc import ABC, abstractmethod
from collections import deque



# to get type of symbol you wanna use
class Symbol:
    def __init__(self, mark):
        self.mark = mark

    def get_mark(self):
        return self.mark
    
# oberver abstract class for in app notification
class IObserver(ABC):
    @abstractmethod
    def update(self, msg: str):
        pass

# concrete class of iobserver abstarct class

class ConsoleNotifier(IObserver):
    
    def update(self, msg: str):
        print(f"[Notification] - {msg}")

# player class

class TicTacToe_player:

    def __init__(self, id: int, name: str, player_symbol: str):
        self.id = id
        self.name = name
        self.player_symbol = Symbol(player_symbol)
        self.score = 0

    def get_player_name(self):
        return self.name
    
    def get_player_symbol(self):
        return self.player_symbol
    
    def get_score(self):
        return self.score
    
    def increment_score(self):
        self.score + 1


# board class

class Board:
    def __init__(self, size_board: int):
        self.size_board = size_board
        self.emptyCell = Symbol('_')
        self.grid = [[self.emptyCell for _ in range(size_board)] for _ in range(size_board)]

    def is_cell_empty(self, row, column):
        if 0<= row < self.size_board and 0<= column < self.size_board:
            if self.grid[row][column] == self.emptyCell:
                return True
        return False
    
    def PlaceMark(self, row, column, symbol: Symbol):
        if self.is_cell_empty(row, column):
            self.grid[row][column] = symbol
            return True
        return False
    
    def get_cell(self, row, column):
        if 0<= row < self.size_board and 0<= column < self.size_board:
            return self.grid[row][column]
        return self.emptyCell
    
    def get_size(self):
        return self.size_board
    
    def display(self):

        print("\n  ", end="")
        for i in range(self.size_board):
            print(i, end=" ")
        print()

        for i, row in enumerate(self.grid):
            print(i, end=" ")
            for symbol in row:
                print(symbol.get_mark(), end = " ")    # get_mark() is not working 
            print()
        print()

# Stratergy pattern :  Rules abstract class

class Rules(ABC):

    @abstractmethod
    def isValidMove(self, board: Board, row, column):
        pass

    @abstractmethod
    def checkWin(self, board: Board, symbol: Symbol):
        pass

    @abstractmethod
    def checkDraw(self, board: Board):
        pass

# concrete classes of rules abstract class

class Standard_rules(Rules):

    def isValidMove(self, board, row, column):
        return board.is_cell_empty(row, column)

    def checkWin(self, board, symbol):
        size = board.size_board
        mark = symbol.get_mark()
        
        # row wise
        for row in board.grid:
            if all(cell.get_mark() == mark for cell in row):
                return True
            
        # column wise
        for col in range(size):
            if all(board.grid[row][col].get_mark() == mark for row in range(size)):
                return True
            
        # Diagonal
        if all(board.grid[i][i].get_mark() == mark for i in range(size)):
            return True

        # Anti-diagonal
        if all(board.grid[i][size - 1 - i].get_mark() == mark for i in range(size)):
            return True

        return False

    def checkDraw(self, board):
        for r in board.grid:
            for cell in r:
                if cell.get_mark() == board.emptyCell.get_mark():     # get_mark() is not working 
                    return False
        return True


# main games class

class TicTacToe_game:

    def __init__(self, board_size):
        self.board = Board(board_size)
        self.players = deque()
        self.rules = Standard_rules()
        self.observers = []
        self.gameOver = False

    def add_player(self, player: TicTacToe_player):
        self.players.append(player)

    def add_Observer(self, observer: IObserver):
        self.observers.append(observer)

    def notify(self, msg: str):
        for observer  in self.observers:
            observer.update(msg)                                     # update function not working here


    def play(self):
        
        if len(self.players) < 2:
            print("Need at least 2 players!")
            return
        
        self.notify("Tic Tac Toe game has started!!")

        while not self.gameOver:
            self.board.display()
            current_player = self.players[0]

            print(f"{current_player.get_player_name()} [{current_player.get_player_symbol().get_mark()}] - Enter row and column ", end=" ")
            try:
                row, col = map(int, input().split())
            except ValueError:
                print("Invalid input! Try again.")
                continue

            if self.rules.isValidMove(self.board, row, col):
                self.board.PlaceMark(row, col, current_player.get_player_symbol())
                self.notify(f"{current_player.get_player_name()} played ({row},{col})")

                if self.rules.checkWin(self.board, current_player.get_player_symbol()):
                    self.board.display()
                    print(f"{current_player.get_player_name()} wins!")
                    current_player.increment_score()
                    # self.notify(f"{current_player.get_player_name()} wins!")
                    self.gameOver = True
                elif self.rules.checkDraw(self.board):
                    self.board.display()
                    print("It's a draw!")
                    self.notify("Game is Draw!")
                    self.gameOver = True
                else:
                    self.players.rotate(-1)
            else:
                print("Invalid move! Try again.")



# 🏗️ Factory Pattern
class TicTacToeGameFactory:
    @staticmethod
    def create_game(game_type, board_size):
        if game_type == "STANDARD":
            return TicTacToe_game(board_size)
        return None

# 🚀 Start the Game
if __name__ == "__main__":
    print("=== TIC TAC TOE GAME ===")
    board_size = int(input("Enter board size (e.g., 3 for 3x3): "))
    game = TicTacToeGameFactory.create_game("STANDARD", board_size)

    notifier = ConsoleNotifier()
    game.add_Observer(notifier)

    player1_name = input("Enter player1 name: ")
    player2_name = input("Enter player2 name: ")
    player1 = TicTacToe_player(1, player1_name, 'X')
    player2 = TicTacToe_player(2, player2_name, 'O')

    game.add_player(player1)
    game.add_player(player2)

    game.play()







        
