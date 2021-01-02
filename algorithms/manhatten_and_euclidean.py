import random
import sys
sys.path.append("..\\")
from util import Util

utility = Util()
MOVES_LIMIT = 100

class ManhattenEuclidean():
    def __init__(self):
        self.player_pos = utility.get_player_pos()
        self.wall_pos = utility.get_walls_pos()
        self.food_pos = utility.get_food_pos()
        self.num_moves = 0
        self.direction = "Right"

    def get_next_moves_manhatten(self):
        num_moves = 0
        moves_list = []
        while not utility.check_food_reached(self.player_pos):
        # for i in range(50):
            if utility.check_collisions(self.player_pos):
                break
            if num_moves > MOVES_LIMIT:
                break

            near_by_pos = utility.near_by_pos(self.player_pos)
            #print("near_by_pos", near_by_pos)
            manhattan_dist = []
            for each_pos in near_by_pos:
                pos_coordinate = utility.direction_to_loc(each_pos, self.player_pos)
                distance = utility.manhattan_dist(pos_coordinate)
                manhattan_dist.append((distance,each_pos))

            manhattan_dist.sort()
            #print("manhattan_dist", manhattan_dist)

            new_position = utility.direction_to_loc(manhattan_dist[0][1], self.player_pos)
            #print("new_position: ", manhattan_dist[0][1] , new_position)
            self.player_pos = new_position
            num_moves += 1
            moves_list.append(new_position)
        return moves_list

    def get_next_moves_euclidean(self):
        num_moves = 0
        moves_list = []
        visited_list = []
        while not utility.check_food_reached(self.player_pos):
        # for i in range(50):
            if utility.check_collisions(self.player_pos):
                break
            if num_moves > MOVES_LIMIT:
                break

            near_by_pos = utility.near_by_pos(self.player_pos)
            #print("near_by_pos", near_by_pos)
            euclidean_dist = []
            for each_pos in near_by_pos:
                pos_coordinate = utility.direction_to_loc(each_pos, self.player_pos)
                distance = utility.euclidean_dist(pos_coordinate)
                euclidean_dist.append((distance,each_pos))
                visited_list.append(pos_coordinate)

            euclidean_dist.sort()
            #print("manhattan_dist", manhattan_dist)

            new_position = utility.direction_to_loc(euclidean_dist[0][1], self.player_pos)
            #print("new_position: ", manhattan_dist[0][1] , new_position)
            self.player_pos = new_position
            num_moves += 1
            moves_list.append(new_position)
        return moves_list, visited_list
