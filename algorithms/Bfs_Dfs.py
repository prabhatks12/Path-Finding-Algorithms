import random
import sys
sys.path.append("..\\")
from util import Util

utility = Util()
LOOP_LIMIT = 5000

class BfsDfs():

    def __init__(self):
        self.player_pos = utility.get_player_pos()
        self.wall_pos = utility.get_walls_pos()
        self.food_pos = utility.get_food_pos()
        self.num_moves = 0
        self.direction = "Right"

    def get_next_moves_bfs(self):
        loop_counter = 0
        queue = []
        visited = []
        moves_list = []

        queue.append([self.player_pos, []])
        # visited.append(self.player_pos)
        here = 0
        # bfs is based on bath , not nodes, thus adding pos inside a list, which itself works as a path
        while len(queue) > 0:
            loop_counter +=1
            current_node, current_path = queue.pop(0)
            #print("current_node: ", current_node,", current_path: ",current_path)
            if loop_counter > LOOP_LIMIT:
                break
            if utility.check_food_reached(current_node):
                #print("here",here)
                return current_path, visited

            if current_node not in visited:
                visited.append(current_node)

                near_by_pos = utility.near_by_pos(current_node)

                for direction in near_by_pos:
                    location =  utility.direction_to_loc(direction, current_node)
                    #print("location", location)
                    move_next = current_path + location
                    queue.append([location, move_next])
                    #print("quue",queue)

            moves_list = current_path
        #print("moves_list",moves_list,"visited",visited)
        return moves_list, visited

    def get_next_moves_dfs(self):
        loop_counter = 0
        stack = []
        visited = []
        moves_list = []

        stack.append([self.player_pos, []])
        # visited.append(self.player_pos)
        here = 0
        # bfs is based on bath , not nodes, thus adding pos inside a list, which itself works as a path
        while len(stack) > 0:
            loop_counter +=1
            current_node, current_path = stack.pop()
            #print("current_node: ", current_node,", current_path: ",current_path)
            if loop_counter > LOOP_LIMIT:
                break
            if utility.check_food_reached(current_node):
                #print("here",loop_counter)
                return current_path, visited

            if current_node not in visited:
                visited.append(current_node)

                near_by_pos = utility.near_by_pos(current_node)

                for direction in near_by_pos:
                    location =  utility.direction_to_loc(direction, current_node)
                    #print("location", location)
                    move_next = current_path + location
                    stack.append([location, move_next])
                    #print("quue",queue)

            moves_list = current_path
        #print("moves_list",moves_list,"visited",visited)
        return moves_list, visited
