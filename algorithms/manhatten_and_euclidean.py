import random
import sys
# sys.path.append("..\\")
# from util import Util

MOVES_LIMIT = 100

"""
ManhattenEuclidean Class:
    Defininig all the functions which are used to find the shortest path between player and food
    using both Manhattan distance and Euclidean distance
"""

class ManhattenEuclidean():
    # reteriving board data
    def __init__(self, utility):
        self.utility = utility
        self.player_pos = self.utility.get_player_pos()
        self.wall_pos = self.utility.get_walls_pos()
        self.food_pos = self.utility.get_food_pos()
        self.num_moves = 0
        self.direction = "Right"


    """
    Function to find shortest path using Manhatten distance
    returns:
        moves_list (LIST) : list of path which player can follow to reach food
        explored_list (LIST) : list of positions which player has explored
    """
    def get_next_moves_manhatten(self):
        num_moves = 0
        # list to store shortest path and explored path
        moves_list , explored_list = [], []

        while not self.utility.check_food_reached(self.player_pos):

            if self.utility.check_collisions(self.player_pos):
                break
            if num_moves > MOVES_LIMIT:
                break

            # reteriving near by positions
            near_by_pos = self.utility.near_by_pos(self.player_pos)

            # list to store near by pos and their distance from food
            manhattan_dist = []
            # print(self.player_pos)
            for each_pos in near_by_pos:
                # changing directions to coordinate
                pos_coordinate = self.utility.direction_to_loc(each_pos, self.player_pos)
                # avoiding path repetition
                if len(explored_list) > 0 and pos_coordinate in explored_list:
                    continue
                # caluclating distaance between food and this position
                distance = self.utility.manhattan_dist(pos_coordinate, self.food_pos)
                manhattan_dist.append((distance,each_pos))
                # adding the poistion to exlpored list
                explored_list.append(pos_coordinate)

            # sorting the list to find the location which is closest to the food
            manhattan_dist.sort()

            # 0 is for first entry after sorting and 1 is for position in (distance, position)
            if len(manhattan_dist) > 0:
                new_position = self.utility.direction_to_loc(manhattan_dist[0][1], self.player_pos)
            else:
                new_position = self.utility.direction_to_loc(near_by_pos[0], self.player_pos)

            self.player_pos = new_position
            num_moves += 1
            moves_list.append(new_position)


            # updating the player position
            self.player_pos = new_position
            num_moves += 1
            moves_list.append(new_position)

        return moves_list, explored_list


    """
    Function to find shortest path using Euclidean
    returns:
        moves_list (LIST) : list of path which player can follow to reach food
        explored_list (LIST) : list of positions which player has explored
    """
    def get_next_moves_euclidean(self):
        num_moves = 0
        moves_list, explored_list = [], []

        while not self.utility.check_food_reached(self.player_pos):

            if self.utility.check_collisions(self.player_pos):
                break
            if num_moves > MOVES_LIMIT:
                break

            # if self.player_pos in explored_list :
            #     continue

            near_by_pos = self.utility.near_by_pos(self.player_pos)

            # list to store near by pos and their distance from food
            euclidean_dist = []

            for each_pos in near_by_pos:
                # changing directions to coordinate
                pos_coordinate = self.utility.direction_to_loc(each_pos, self.player_pos)
                # avoiding path repetition
                if len(explored_list) > 0 and pos_coordinate in explored_list:
                    continue
                # caluclating distaance between food and this position
                distance = self.utility.euclidean_dist(pos_coordinate, self.food_pos)
                euclidean_dist.append((distance,each_pos))
                # adding the poistion to exlpored list
                explored_list.append(pos_coordinate)

            # sorting the list to find the location which is closest to the food
            euclidean_dist.sort()

            # 0 is for first entry after sorting and 1 is for position in (distance, position)
            if len(euclidean_dist) > 0:
                new_position = self.utility.direction_to_loc(euclidean_dist[0][1], self.player_pos)
            else:
                new_position = self.utility.direction_to_loc(near_by_pos[0], self.player_pos)

            self.player_pos = new_position
            num_moves += 1
            moves_list.append(new_position)

        return moves_list, explored_list
