import random


class Field:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.hidden_ship = None
        self.visible_ship = None

    def put_hidden_ship_on_field(self, ship):
        self.hidden_ship = ship

    def reveal_ship(self):
        if self.visible_ship is None and self.hidden_ship is not None:
            self.visible_ship = self.hidden_ship
            self.hidden_ship = None

    def move_ship(self, field):
        sunken_ship = field.visible_ship
        field.visible_ship = self.visible_ship
        self.visible_ship = None
        return sunken_ship


class Ship:
    def __init__(self, side, power):
        self.side =  side #'Spaniard' or 'Pirates'
        self.direction = None # one of 'NSEW'
        self.power = power # one of 1, 2 or 3

    def turn(self, direction):
        self.direction = direction

    def draw_a_ship(self):
        pass


class OneShip(Ship):
    def  __init__(self, side):
        super().__init__(side, 1)

    def draw_a_ship(self):
        #this function should draw a ship
        pass


class TwoShip(Ship):
    def  __init__(self, side):
        super().__init__(side, 2)

    def draw_a_ship(self):
        #this function should draw a ship
        pass


class ThreeShip(Ship):
    def  __init__(self, side):
        super().__init__(side, 3)

    def draw_a_ship(self):
        #this function should draw a ship
        pass


class Arbiter:
    def __init__(self, spain_player, pirate_player):
        self.spain_player = spain_player
        self.pirate_player = pirate_player
        self.board_size = 4
        self.board = None
        self.game_result = (0,0)

    def prepare_game(self):
        #initiate the board
        self.board = [Field(x, y) for x in range(self.board_size) for y in range(self.board_size)
                      if (x, y) not in [(0, 0), (0,self.board_size-1), (self.board_size-1, 0), (self.board_size-1, self.board_size-1)]]
        ships = [OneShip('spaniards'), TwoShip('spaniards'), ThreeShip('spaniards'),
                 OneShip('pirates'), TwoShip('pirates'), ThreeShip('pirates')]*2
        random.shuffle(ships)
        for field, ship in zip(self.board, ships):
            field.put_hidden_ship_on_field(ship)

    def play_a_game(self):
        self.prepare_game()
        self.game_result = (0,0)
        active_player = self.spain_player
        while max(self.game_result)<7:
            move = active_player.make_a_move()
            if not self.verify_move_legality(move):
                raise ('Illegal move')
            elif move[0] == 'reveal':
                # reveal the ship on field(move[0],move[1]) and ask player for initial direction
                pass
            elif move[0] == 'turn':
                # change the ship direction
                pass
            elif move[0] == 'move':
                # initiate ship movement, then change the results
                pass
            if active_player == self.spain_player:
                active_player = self.pirate_player
            else:
                active_player = self.spain_player

    def verify_move_legality(self, move):
        return True

    def draw_a_board(self):
        # this method should print a board in a human-friendly form
        pass

    def show_visible_board(self):
        # this function should present the boardstate and game result to the player
        return self.board()

class Player():
    def __init__(self, name):
        self.name = name

    def make_a_move(self, boardstate):
        return None # should return a move in the dict: ['reveal',x,y], [turn,x,y,N/S/W/E], [sail,x,y, N/S/W/E/NE/NW/SE/SW)]

    def decide_initial_position(self):
        return None # should be one from 'NSWE'


if __name__ == '__main__':
    arbiter = Arbiter(Player('P1'), Player('P2'))
    print(arbiter.board)
    arbiter.prepare_game()
    print(arbiter.board)
    print([field.__dict__ for field in arbiter.board])
    arbiter.board[0].reveal_ship()
    print(arbiter.board[0].__dict__)
    print(arbiter.board[0].visible_ship.__dict__)