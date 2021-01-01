import random
import sys
sys.path.append("..\\")
from util import Util

# calling util to import important functions
utility = Util()

# max number of moves to reach food
MOVES_LIMIT = 200

class RandomPath():

    # initalizing few imp variables, will be used later
    def __init__(self):
        print("Random path called")
        self.player_pos = utility.get_player_pos()
        self.wall_pos = utility.get_walls_pos()
        self.food_pos = utility.get_food_pos()
        self.num_moves = 0
        self.direction = "Right"

    # function to generate legal moves for the player
    def get_next_moves(self):
        num_moves = 0

        # list of moves, max size = MOVES_LIMIT, min = number of moves taken to reach food
        moves_list = []
        while not utility.check_food_reached(self.player_pos):
            # if player tries to collide with the walls
            if utility.check_collisions(self.player_pos):
                continue
            if num_moves > MOVES_LIMIT:
                break

            # getting all near by positions which are legal to move on
            near_by_pos = utility.near_by_pos(self.player_pos)
            num_pos = len(near_by_pos)

            # last element = len (list) -1 , thus genrating random btw it and 0
            random_pos = random.randint(0,num_pos-1)

            # near_by_pos stores directions, finding location based on direction
            new_position = utility.direction_to_loc(near_by_pos[random_pos], self.player_pos)

            # changin player pos to new position
            self.player_pos = new_position
            num_moves += 1
            moves_list.append(new_position)

        return moves_list
