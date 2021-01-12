import random
import sys
sys.path.append("..\\")
from util import Util

utility = Util()
LOOP_LIMIT = 5000

"""
BfsDfs Class:
    Defininig all the functions which are used to find the shortest path between player and food
    using both Breadth First Search (BFS) and Depth First Search (DFS)
"""

class BfsDfs():

    def __init__(self):
        self.player_pos = utility.get_player_pos()
        self.wall_pos = utility.get_walls_pos()
        self.food_pos = utility.get_food_pos()
        self.num_moves = 0
        self.direction = "Right"


    """
    Function to find shortest path using BFS
    returns:
        moves_list (LIST) : list of path which player can follow to reach food
        visited_list (LIST) : list of positions which player has explored
    """
    def get_next_moves_bfs(self):
        loop_counter = 0
        # bfs requires queue implementations
        queue = []
        moves_list, visited_list = [], []

        queue.append([self.player_pos, []])

        while len(queue) > 0:
            loop_counter +=1
            current_node, current_path = queue.pop(0)
            if loop_counter > LOOP_LIMIT:
                break
            if utility.check_food_reached(current_node):
                return current_path, visited_list

            # avoiding already explored locatios
            if current_node not in visited_list:
                visited_list.append(current_node)

                near_by_pos = utility.near_by_pos(current_node)

                for direction in near_by_pos:
                    # changing directions to coordinate
                    location =  utility.direction_to_loc(direction, current_node)
                    move_next = current_path + [location]
                    queue.append([location, move_next])

            moves_list = current_path

        return moves_list, visited_list


    """
    Function to find shortest path using DFS
    returns:
        moves_list (LIST) : list of path which player can follow to reach food
        visited_list (LIST) : list of positions which player has explored
    """
    def get_next_moves_dfs(self):
        loop_counter = 0
        # dfs requires stack implementations
        stack = []
        visited_list , moves_list = [], []

        stack.append([self.player_pos, []])

        while len(stack) > 0:
            loop_counter +=1
            current_node, current_path = stack.pop()

            if loop_counter > LOOP_LIMIT:
                break
            if utility.check_food_reached(current_node):
                return current_path, visited_list

            # avoiding already explored locations
            if current_node not in visited_list:
                visited_list.append(current_node)

                # reteriving near by positions
                near_by_pos = utility.near_by_pos(current_node)

                for direction in near_by_pos:
                    # changing directions to coordinate
                    location =  utility.direction_to_loc(direction, current_node)
                    move_next = current_path + [location]
                    stack.append([location, move_next])

            moves_list = current_path

        return moves_list, visited_list
