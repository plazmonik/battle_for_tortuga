#To będzie super ekstra projekt ale całkowicie go zmienię już wkrótce, jak mi się będzie chciało (a jak nie, to będę korzystać z głównego brancha)

class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hidden_ship = None
        self.seen_ship = None


class Board:
    def __init__(self, board_size):
        self.board = [Field(x, y) for x in range(board_size) for y in range(board_size)]

    def show_board(self):
        pass

class Ship:
    def __init__(self, side, direction, power):
        self.side =  None #'Spanish' or 'Pirates'
        self.direction = None # one of 'NSEW'
        self.power = None # one of 1, 2 or 3
        self.pos_x = None
        self.pos_y = None

     def move(self, direction):
        pass


class OneShip(Ship):
    def  __init__(self, side, direction):
        super().__init__(side, direction, 1)

    def move(self, direction):
        pass


class TwoShip(Ship):
    def  __init__(self, side, direction):
        super().__init__(side, direction, 2)

    def move(self, direction):
        pass


class ThreeShip(Ship):
    def  __init__(self, side, direction):
        super().__init__(side, direction, 3)

    def move(self, direction):
        pass

class Arbiter:
    def __init(self, spain_player, pirate_player):
        self.spain_player = spain_player #
        self.pirate_player = pirate_player
